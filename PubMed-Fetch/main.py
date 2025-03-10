# main.py
from pubmed_fetcher import fetch_pubmed_ids, fetch_paper_details, save_to_csv
import time

# Main function to get input from user
def main() -> None:
    query = input("Enter search query for PubMed: ")
    filename = input("Enter filename to save as CSV (leave blank to print on console): ")

    pubmed_ids = fetch_pubmed_ids(query)
    papers = fetch_paper_details(pubmed_ids)

    if filename:
        save_to_csv(filename, papers)
    else:
        for paper in papers:
            print(paper)

if __name__ == '__main__':
    main()

