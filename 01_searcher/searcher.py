import argparse
import csv
import json

import requests
from bs4 import BeautifulSoup


class Searcher:
    def __init__(self, engine, output):
        self.engine = engine
        self.output = output
        self.filename = "latest_links"
        self.query_template = {
            "yandex": "https://{}.com/search/?text={}",
            "google": "https://{}.com/search?q={}"
        }

    def _load(self, query):
        data = requests.get(
            self.query_template[self.engine].format(self.engine, query))
        return data.text

    def _export(self, links):
        if self.output == "console":
            [print(link) for link in links]
            print()
        elif self.output == "csv":
            with open(f'{self.filename}.csv', 'w') as f:
                writer = csv.writer(f)
                [writer.writerow([link]) for link in links]
        elif self.output == "json":
            with open(f'{self.filename}.json', 'w') as f:
                json.dump(links, f)

    def get_links(self, query):
        data = self._load(query)
        soup = BeautifulSoup(data, "html.parser")
        links = [link.get('href') for link in soup.findAll('a')]
        self._export(links)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('query', metavar='query', type=str, help='query')
    parser.add_argument('-e', '--engine',
                        help='source engine: yandex|google(default)',
                        default="google",
                        type=str)
    parser.add_argument('-o', '--output',
                        help='output format: json|csv|console(default)',
                        default="console",
                        type=str)
    args = parser.parse_args()

    searcher = Searcher(args.engine, args.output)
    searcher.get_links(args.query)
