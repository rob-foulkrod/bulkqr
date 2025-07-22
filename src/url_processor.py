from typing import List

def read_urls_from_file(file_path: str) -> List[str]:
    """
    Reads URLs from a text file, one per line.
    Returns a list of URLs.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]
    return urls
