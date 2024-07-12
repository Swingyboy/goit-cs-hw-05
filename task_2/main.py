import argparse
import requests
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
import re


def fetch_text(url: str) -> str:
    response = requests.get(url)
    return response.text


def tokenize(text: str) -> list[str]:
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    words = text.lower().split()
    return words


def mapper(word: str) -> tuple[str, int]:
    return (word, 1)


def reducer(mapped_word_counts: list[tuple[str, int]]) -> Counter[str]:
    reduced = Counter()
    for word, count in mapped_word_counts:
        reduced[word] += count
    return reduced


def map_reduce(text: str) -> Counter[str]:
    words = tokenize(text)

    with ThreadPoolExecutor() as executor:
        mapped = list(executor.map(mapper, words))

    reduced = reducer(mapped)
    return reduced


def visualize_top_words(word_counts: Counter[str], top_n: int=10) -> None:
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words, counts = zip(*sorted_words)

    plt.figure(figsize=(10, 5))
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top {} Words by Frequency'.format(top_n))
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Word frequency counter.")
    parser.add_argument("--url", type=str, help="URL to fetch text", default="https://www.gutenberg.org/files/1342/1342-0.txt")
    args = parser.parse_args()
    url = args.url
    text = fetch_text(url)
    word_counts = map_reduce(text)
    visualize_top_words(word_counts, top_n=10)
