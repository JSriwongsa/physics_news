# physics_news
Pulling article data from physics news sites

- `physics_news.py` - This program will pull article data from physics rss feeds. You can add new websites by modifying what is in `urls`.
It will output the `title`,`link`, and `published` date if there is one.
- `phys585_arvix.py` - This program will enter a search query on arxiv and give back the output of: `Title`, `Author`, and `Abstract`.

### Usage (physics_news.py):
```python

python3 physics_news.py

# sample output:
    {
        "title": "How silicides impact the performance of transmon qubits",
        "link": "https://phys.org/news/2023-01-silicides-impact-transmon-qubits.html",
        "published": "Fri, 27 Jan 2023 09:59:04 EST"
    },
    {
        "title": "Researchers find ways to improve the storage time of quantum information in a spin rich material",
        "link": "https://phys.org/news/2023-01-ways-storage-quantum-rich-material.html",
        "published": "Thu, 26 Jan 2023 16:42:32 EST"
    }
```
### Usage (phys585_arxiv.py):
```python

./phys585_arxiv.py 'superconductors'
Search Query Term: superconductors
--------------------------------------------------------------------------------
Title:
 Influence of Local Correlations on the "Homogeneous Insulator-Superconductor" Transition in the Domain Boundaries of the Charge-Order Phase of a 2D System of a Mixed Valence
Authors:
 ['V. V. Konev', 'V. A. Ulitko', 'D. N. Yasinskaya', 'Yu. D. Panov', 'A. S. Moskvin']

Abstract:
 It is demonstrated in the (pseudo)spin S=1 formalism that the structure of
antiphase domain boundaries in the phase of charge ordering of a mixed-valence
system of the Cu1+, 2+, 3+ "triplet" type in cuprates on a two-dimensional
square lattice depends to a considerable extent on on-site correlation
parameter U. The results of computer modeling on large square lattices
illustrate the change in the boundary structure (from a homogeneous monovalent
nonconducting structure of the Cu2+ type to a filamentary superconducting one)
induced by a relatively small variation of positive U values.
--------------------------------------------------------------------------------
http://dx.doi.org/10.1134/S1063783418110136
http://arxiv.org/abs/2301.11876v1
http://arxiv.org/pdf/2301.11876v1
--------------------------------------------------------------------------------

```