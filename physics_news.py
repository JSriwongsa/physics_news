import feedparser
import json

class PhysicsNews():
    def __init__(self, url):
        self.url = url

    def parse_url(self):
        return feedparser.parse(self.url)

    def items(self):
        data = self.parse_url()
        items = []

        for item in data['entries']:
            title = item.get('title', None)
            link = item.get('link', None)
            published = item.get('published', None)
            data_dict = {
                'title': title,
                'link': link,
                'published': published
            }
            items.append(data_dict)

        return items

    def main(self):
        return self.items()

if __name__ == '__main__':

        urls = [
                'https://phys.org/rss-feed/physics-news/quantum-physics/',
                'https://phys.org/rss-feed/physics-news/physics/',
                'https://www.aip.org/fyi/opportunities/feed',
                'https://aip.scitation.org/action/showFeed?type=etoc&feed=rss&jc=apl',
                'https://aip.scitation.org/action/showFeed?type=etoc&feed=rss&jc=ltp',
                'https://www.newscientist.com/subject/physics/feed/',
                'https://www.pnas.org/action/showfeed?type=searchTopic&taxonomyCode=topic&tagCode=app-phys',
                'https://www.pnas.org/action/showfeed?type=searchTopic&taxonomyCode=topic&tagCode=phys',
                'http://feeds.rsc.org/rss/ya',
                'https://scipost.org/rss/submissions/phys-he',
                'https://scipost.org/rss/submissions/phys-ht',
                'https://scipost.org/rss/submissions/phys-hp',
                'https://scipost.org/rss/submissions/phys-qp',
                'https://www.compadre.org/osp/services/rss/aggregate.cfm',
                'http://feeds.feedburner.com/edp_epjap_news?format=xml',
                'http://feeds.feedburner.com/edp_epjqt_news?format=xml',
                'https://www.sciencedaily.com/rss/matter_energy/quantum_physics.xml',
                'https://www.sciencedaily.com/rss/matter_energy/quantum_computing.xml',
                'https://www.sciencedaily.com/rss/matter_energy/physics.xml',
                #'https://media.rss.com/friendlyphysics/feed.xml'
                ]

        print("RSS FEED URLS:")
        print("--" * 14 )

        for url in urls:
            print(url)

        print("--" * 14)

        for url in urls:
            news = PhysicsNews(url)
            json_news = json.dumps(news.main(), indent=4)
            print(json_news)

        print("--" * 14)
