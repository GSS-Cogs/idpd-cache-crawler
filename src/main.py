from typing import List
from unittest.mock import Base
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
            logger.error(f"Error occured while attempting to call crawler {crawler}")
            
            # TODO
            # Something with this error, the key point
            # is the crawler cannot fall over.
            # Make this error LOUD as an exception from
            # a crawler means ALL links its responisble
            # for crawling are potentially not updated, but
            # do not block or knock over the cache crawler
            # itself (if needs to keep going and try and 
            # next crawler).
            # Ideally errors would be caught before this
            # point but this is our safety.
            ...
            

def main(crawler_list: List[BaseCrawler]):

    # TODO - get the domain from an env var, eg:
    # DOMAIN_ROOT="staging.idpd.uk"
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
            raise
           # NOTE - you CAN (and should) raise here, if it
           # wont start it wont get deployed which is the correct
           # behaviour for failed instantiation.
           # Beyond this level you do NOT want to 
           # be raising uncontroled errors as we dont
           # want a dployed app falling over.
            ...

    crawl(instanitated_crawler_list)

if __name__  == "__main__":
    # Add more when we have more, just dataset to begin with
    crawler_list = [DatasetApiCrawler]
    main(crawler_list)