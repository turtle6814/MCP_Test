from main import download_webpage_as_markdown


def test_download_webpage():
    """Test the download_webpage_as_markdown function"""
    url = "https://github.com/alexeygrigorev/minsearch"

    print(f"Testing download_webpage_as_markdown with URL: {url}")
    print("-" * 80)

    content = download_webpage_as_markdown(url)

    if content.startswith("Error"):
        print(f"Failed: {content}")
    else:
        print("Success! Here's a preview of the downloaded content:")
        print("-" * 80)
        # Print first 500 characters as a preview
        print(content[:500])
        print("-" * 80)
        print(f"Total content length: {len(content)} characters")

        # Save to file for inspection
        with open("downloaded_content.md", "w", encoding="utf-8") as f:
            f.write(content)
        print("\nFull content saved to 'downloaded_content.md'")


if __name__ == "__main__":
    test_download_webpage()
