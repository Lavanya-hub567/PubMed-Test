# Project Report: PubMed Fetcher

## Project Overview
The PubMed Fetcher project is a Python-based tool designed to interact with the PubMed API to search for academic-affiliated research papers based on a user-defined query. The tool fetches detailed information about relevant publications and allows the user to either display the results on the console or save them as a CSV file. The program specifically filters the results to include only those affiliated with academic institutions such as universities, colleges, research institutes, and similar entities.

## Key Features
- Fetches up to 500 relevant PubMed articles per search query.
- Filters papers to include only those from academic-affiliated institutions.
- Displays results in the console or saves them as a CSV file.
- Uses robust error handling and logging for reliability.
- Implements retry logic with exponential backoff to handle API request failures.

## Methodology
1. **Search Query Input:** The program prompts the user to enter a search term and an optional filename for CSV output.
2. **Fetching PubMed IDs:** It sends a request to the PubMed API to retrieve unique article IDs matching the query.
3. **Batch Processing:** Article IDs are processed in batches to avoid request overloads.
4. **Filtering Academic Papers:** The program filters articles based on the 'Company' or 'Source' field, checking for keywords associated with academic institutions.
5. **Data Output:** The results are either displayed on the console or saved as a CSV file with fields including PubMed ID, Title, Publication Date, Authors, and Affiliation.

## Technical Implementation
- **Programming Language:** Python
- **Libraries Used:**
  - `requests` for API calls
  - `csv` for file handling
  - `logging` for system logging
  - `time` for managing request delays
  - `requests.adapters` for retry strategies

## Challenges and Solutions
- **Rate Limiting:** Introduced a delay (`time.sleep(1)`) between batch requests to avoid being blocked by the API.
- **Request Failures:** Implemented a retry strategy using `HTTPAdapter` and `Retry` from `requests.adapters`.
- **Filtering for Academic Papers:** Created a list of keywords (`ACADEMIC_KEYWORDS`) to identify academic institutions from the 'source' field of the API response.

## Results
The program successfully extracts academic-affiliated papers from PubMed and outputs them in the desired format. It ensures reliability through error handling and logging, and the filtering mechanism effectively narrows down results to academically relevant content.

## Future Improvements
- Enhance the filtering logic to support more complex patterns and improve accuracy.
- Add a graphical user interface (GUI) for easier use.
- Enable support for more output formats, such as JSON or Excel files.
- Introduce advanced search features like date range filtering and sorting options.

## Conclusion
The PubMed Fetcher project provides a robust and effective solution for researchers and academics to gather relevant literature from PubMed efficiently. The targeted filtering of academic institutions ensures the integrity and relevance of the fetched data, making this tool a valuable resource for research purposes.

