# search.py - Test implementation
from index_docs import (
    create_search_index,
    download_file_if_needed,
    extract_md_files,
    search,
)


def test_search():
    """Test the search implementation"""
    # Download and index
    zip_url = "https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip"
    zip_filename = "fastmcp-main.zip"

    download_file_if_needed(zip_url, zip_filename)
    documents = extract_md_files(zip_filename)
    index = create_search_index(documents)

    # Test with query "demo"
    print("=" * 80)
    print("TESTING SEARCH WITH QUERY: 'demo'")
    print("=" * 80)

    results = search(index, "demo", num_results=5)

    print(f"\nFirst file returned: {results[0]['filename']}")
    print("\nAll top 5 results:")
    for i, doc in enumerate(results, 1):
        print(f"{i}. {doc['filename']}")

    return results


if __name__ == "__main__":
    results = test_search()
