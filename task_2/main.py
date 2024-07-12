import argparse
import requests
from collections import defaultdict
import matplotlib.pyplot as plt
import re


def fetch_text(url):
    response = requests.get(url)
    return response.text


def tokenize(text):
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    words = text.lower().split()
    return words


def mapper(word):
    return (word, 1)


def reducer(count1, count2):
    return count1 + count2


def map_reduce(text):
    words = tokenize(text)
    mapped = list(map(mapper, words))

    grouped = defaultdict(list)
    for word, count in mapped:
        grouped[word].append(count)

    reduced = {word: sum(counts) for word, counts in grouped.items()}
    return reduced


def visualize_top_words(word_counts, top_n=10):
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
