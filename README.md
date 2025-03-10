# PubMed Fetcher Project Report

## 1. Introduction
The PubMed Fetcher project is designed to interact with the PubMed API to retrieve research paper details based on user queries. The tool allows fetching PubMed IDs, retrieving detailed paper metadata, and saving the results to a CSV file. This solution is intended for researchers, academics, and professionals who need to access PubMed data efficiently.

## 2. Objective
The main objective of this project is to provide a simple and effective method to search PubMed, retrieve relevant research papers, and export them for offline analysis or further use.

## 3. Approach
The project comprises two main components:
1. **Main Script (`main.py`)**: Manages user input, fetches data, and handles output options (console or CSV file).
2. **Helper Module (`pubmed_fetcher.py`)**: Contains functions to interact with the PubMed API, fetch data in batches, and save results.

### 3.1 API Integration
- Utilized **NCBI's E-utilities**: The `esearch` endpoint to get PubMed IDs and the `esummary` endpoint to fetch detailed metadata.
- Implemented **requests session with retries** using `HTTPAdapter` and `Retry` from the `requests` library.
- Configured a maximum of 5 retries with exponential backoff to handle transient errors (502, 503, 504).

### 3.2 Data Fetching Strategy
- Batched requests in groups of 100 IDs to avoid rate limiting and manage large datasets.
- Introduced a **1-second delay** between requests using `time.sleep` to further reduce API load.
- Handled empty responses and request exceptions gracefully with error logging.

### 3.3 Data Handling
- Extracted relevant fields including Title, Publication Date, Authors, and Source.
- Handled missing data with `'N/A'` defaults.
- Allowed data output either to the console or to a CSV file using the `csv` module.

## 4. Methodology
1. **Fetching PubMed IDs:**
   - Input: User search query.
   - Output: List of relevant PubMed IDs.

2. **Fetching Paper Details:**
   - Input: List of PubMed IDs.
   - Output: List of dictionaries containing paper details.
   - Batch processing to handle up to 500 IDs per query safely.

3. **Saving to CSV:**
   - Input: Filename and data.
   - Output: CSV file with structured paper metadata.

## 5. Results
- The script successfully fetched research papers based on a variety of test queries.
- Demonstrated robustness by handling network errors and avoiding API rate limits.
- The CSV export functionality allowed easy data storage and offline use.

## 6. Challenges
- **API Rate Limiting:** Addressed by implementing delays and request retries.
- **Data Quality:** Handled missing data with default values.
- **Error Handling:** Improved resilience through try-except blocks and informative logging.

## 7. Conclusion
The PubMed Fetcher tool is a valuable resource for efficiently accessing and exporting PubMed data. With robust error handling, batch processing, and flexible output options, it provides a practical solution for research needs. Future improvements could include support for advanced query parameters, multi-threading for faster data retrieval, and a graphical user interface (GUI).

## 8. Future Improvements
- **Asynchronous Requests:** To improve performance on large datasets.
- **User Interface:** Adding a GUI or web interface for non-technical users.
- **Advanced Search Options:** Support for Boolean operators and filters in search queries.
- **Data Visualization:** Adding basic analytics or visualization features for the fetched data.

## 9. References
- NCBI E-utilities documentation: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- Requests library documentation: https://docs.python-requests.org/en/latest/

---
End of Report

