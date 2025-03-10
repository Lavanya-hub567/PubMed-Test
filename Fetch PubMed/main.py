from pubmed_fetcher import fetch_pubmed_ids, fetch_paper_details, save_to_csv

def main() -> None:
    query = input("Enter the query to search for research papers: ")
    filename = input("Enter the filename to save the results as a CSV file: ")

    paper_ids = fetch_pubmed_ids(query)
    if not paper_ids:
        print("No papers found for the given query.")
        return

    papers = fetch_paper_details(paper_ids)
    save_to_csv(filename, papers)
    print(f"Results saved to {filename}")

if __name__ == '__main__':
    main()
