#!/usr/bin/env python3

import arxiv
import sys

query = sys.argv[1]

print(f"Search Query Term: {query}")
print("--" * 40)

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


