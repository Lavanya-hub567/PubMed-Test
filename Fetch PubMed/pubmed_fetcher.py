import csv
import requests
import logging
import time
from requests.adapters import HTTPAdapter, Retry
from typing import List, Dict

# PubMed API URLs
PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Setup requests session with retries
session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))
session.mount('https://', HTTPAdapter(max_retries=retries))

# Function to fetch PubMed IDs based on a query
def fetch_pubmed_ids(query: str) -> List[str]:
    logger.info(f"Fetching PubMed IDs for query: {query}")
    params = {
        'db': 'pubmed',
        'term': query,
        'retmode': 'json',
        'retmax': 500
    }
    try:
        response = session.get(PUBMED_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('esearchresult', {}).get('idlist', [])
    except requests.exceptions.RequestException as e:
        logger.error(f'Failed to fetch PubMed IDs: {e}')
        return []

# Function to fetch detailed paper information without affiliation filter
def fetch_paper_details(pubmed_ids: List[str], batch_size: int = 100) -> List[Dict[str, str]]:
    if not pubmed_ids:
        return []
    results = []
    for i in range(0, len(pubmed_ids), batch_size):
        batch_ids = pubmed_ids[i:i + batch_size]
        logger.info(f"Fetching details for batch {i // batch_size + 1}")
        params = {
            'db': 'pubmed',
            'id': ','.join(batch_ids),
            'retmode': 'json'
        }
        try:
            response = session.get(PUBMED_SUMMARY_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            for pid, details in data.get('result', {}).items():
                if pid != 'uids':
                    results.append({
                        'PubmedID': pid,
                        'Title': details.get('title', 'N/A'),
                        'Publication Date': details.get('pubdate', 'N/A'),
                        'Authors': ', '.join([author['name'] for author in details.get('authors', [])]),
                        'Institution': details.get('source', 'N/A')
                    })
        except requests.exceptions.RequestException as e:
            logger.error(f'Failed to fetch paper details for batch: {e}')
        time.sleep(1)
    return results

# Function to save results as CSV
def save_to_csv(filename: str, papers: List[Dict[str, str]]) -> None:
    logger.info(f"Saving results to {filename}")
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['PubmedID', 'Title', 'Publication Date', 'Authors', 'Institution'])
        writer.writeheader()
        writer.writerows(papers)
