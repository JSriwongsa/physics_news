#!/usr/bin/env python3

import arxiv
import argparse
import sys

parser = argparse.ArgumentParser(description='Search for a title on arxiv.')
parser.add_argument('-q', '--query', help='Search term or query.', required=True)
args = vars(parser.parse_args())

if len(sys.argv) < 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

query = args['query']

print(f"Search Query Term: {query}")
print("--" * 4)

find = arxiv.Search(
    query = query,
    max_results=10,
    sort_by = arxiv.SortCriterion.SubmittedDate
)

for result in find.results():

    print(f"Title:\n {result.title}")
    print(f"Authors:\n { [ author.name for author in result.authors ]}")
    print(" ")
    print(f"Abstract:\n {result.summary}")
    print('--' * 40)

    for link in result.links:
        print(link)
    
    print('--' * 40)


