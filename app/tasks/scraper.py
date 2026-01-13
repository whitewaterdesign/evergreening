# python
import re
from typing import List, Optional

import httpx
from bs4 import BeautifulSoup

from app.models.input import EvergreenYamlInput


def fetch_page_text(url: str, *, http2: bool = False, timeout: int = 10) -> str:
    """
    Fetch a URL and return the visible text content.
    """
    with httpx.Client(http2=http2, timeout=timeout) as client:
        resp = client.get(url)
        resp.raise_for_status()
        html = resp.text

    soup = BeautifulSoup(html, "html.parser")

    # remove scripts, styles, and irrelevant elements
    for tag in soup(["script", "style", "noscript", "header", "footer", "svg"]):
        tag.decompose()

    text = soup.get_text(separator=" ")

    # normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def chunk_text(text: str, chunk_size: int = 2000, overlap: int = 200) -> List[str]:
    """
    Split text into overlapping chunks suitable for sending to an agent or embedding model.
    """
    if chunk_size <= overlap:
        raise ValueError("`chunk_size` must be larger than `overlap`")
    chunks = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunks.append(text[start:end])
        if end == text_len:
            break
        start = end - overlap
    return chunks


def fetch_and_prepare(url: str, chunk_size: Optional[int] = None) -> List[str] | str:
    """
    Convenience function: fetch page text and return chunks ready for the agent.
    """
    text = fetch_page_text(url, http2=True)

    if chunk_size:
        return chunk_text(text, chunk_size=chunk_size)
    return text


def fetch_and_prepare_candidate(evergreen_candidate: EvergreenYamlInput) -> str:
    """
    Fetches and prepares the candidate's changelog or release notes for processing.
    """
    url = evergreen_candidate["link"]
    return fetch_and_prepare(url)


# Example usage:
# asyncio.run(fetch_and_prepare("https://example.com"))
if __name__ == "__main__":
    print(fetch_and_prepare("https://github.com/agno-agi/agno/releases"))