# -*- utf-8 -*-
#
# Download image for google image search
#

from icrawler.builtin import GoogleImageCrawler


google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': 'cat-images'})


cat_breeds = open('data.txt').readlines()
cat_breeds = [x.strip().rstrip() for x in cat_breeds]

for keyword in cat_breeds:
	google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': 'cat-images/' + keyword})
	google_crawler.crawl(keyword=keyword, max_num=1000,
			     date_min=None, date_max=None,
			     min_size=(100,100), max_size=None)




