# physics_news
Pulling article data from physics news sites

`physics_news.py` - This program will pull article data from physics rss feeds. You can add new websites by modifying what is in `urls`.
It will output the `title`,`link`, and `published` date if there is one.

### Usage:
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