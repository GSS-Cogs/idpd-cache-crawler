from typing import List
import os

from src.crawlers.base import BaseCrawler
from crawlers import DatasetApiCrawler
from logger import logger

def crawl(crawlers: List[BaseCrawler]):
    """
    Call the various web crawlers
    """

    for crawler in crawlers:
        try:
            crawler.crawl()
        except Exception as err:
            logger.exception(err)
            

def main(crawler_list: List[BaseCrawler]):

    DOMAIN_ROOT = os.environ.get("DOMAIN_ROOT")
    if not DOMAIN_ROOT:
        raise ValueError("DOMAIN_ROOT not found, please ensure environment variable is correct.")

    # Initiate the crawlers in a controlled way so
    # we can make sure none of them error during this
    # Note: "dataset api" is the real/post-poc name for
    # the api we built.
    instanitated_crawler_list = []
    for crawler in crawler_list:
        try:
            instanitated_crawler_list.append(
                crawler(DOMAIN_ROOT)
            )
        except Exception as err:
            logger.error(f"Error occured while attempting to instantiate and initiate crawler {crawler}")
            raise err

    crawl(instanitated_crawler_list)

if __name__  == "__main__":
    # Add more when we have more, just dataset to begin with
    crawler_list = [DatasetApiCrawler]
    main(crawler_list)