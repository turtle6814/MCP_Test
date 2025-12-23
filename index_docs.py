# index_docs.py - Main implementation
import os
import zipfile

import minsearch
import requests


def download_file_if_needed(url, filename):
    """Download file if it doesn't exist"""
    if os.path.exists(filename):
        print(f"File {filename} already exists, skipping download")
        return filename

    print(f"Downloading {url}...")
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded to {filename}")
    return filename


def extract_md_files(zip_path):
    """Extract md and mdx files from zip, removing the first part of path"""
    documents = []

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        for file_info in zip_ref.filelist:
            filename = file_info.filename

            # Only process .md and .mdx files
            if filename.endswith(".md") or filename.endswith(".mdx"):
                # Remove the first part of the path (fastmcp-main/)
                parts = filename.split("/", 1)
                if len(parts) > 1:
                    new_filename = parts[1]
                else:
                    new_filename = filename

                # Read file content
                with zip_ref.open(file_info) as f:
                    content = f.read().decode("utf-8", errors="ignore")

                documents.append({"filename": new_filename, "content": content})
                print(f"Extracted: {new_filename}")

    return documents


def create_search_index(documents):
    """Create minsearch index with documents"""
    index = minsearch.Index(text_fields=["content", "filename"], keyword_fields=[])

    index.fit(documents)
    print(f"Indexed {len(documents)} documents")
    return index


def search(index, query, num_results=5):
    """Search the index and return top results"""
    boost_dict = {
        "filename": 2.0,  # Boost filename matches
        "content": 1.0,
    }

    results = index.search(query=query, boost_dict=boost_dict, num_results=num_results)

    return results


def main():
    # Step 1: Download the zip file
    zip_url = "https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip"
    zip_filename = "fastmcp-main.zip"

    download_file_if_needed(zip_url, zip_filename)

    # Step 2: Extract md and mdx files
    print("\nExtracting markdown files...")
    documents = extract_md_files(zip_filename)

    # Step 3: Create search index
    print("\nCreating search index...")
    index = create_search_index(documents)

    # Step 4: Test search
    print("\nTesting search with query 'demo'...")
    results = search(index, "demo", num_results=5)

    print("\nTop 5 results:")
    for i, doc in enumerate(results, 1):
        print(f"{i}. {doc['filename']}")
        print(f"   Preview: {doc['content'][:100]}...")
        print()

    return index, documents


if __name__ == "__main__":
    index, documents = main()
