from typing import List

from src.crawlers.models import BaseCrawler
from crawlers import DatasetApiCrawler

# TODO - this needs to come from an env var.
BASE_DOMAIN = "https://staging.idpd.uk"


def crawl(crawlers: List[BaseCrawler]):
    """
    Call the various web crawlers
    """

    for crawler in crawlers:
        try:
            crawler.crawl()
        except Exception as err:
            
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
            

if __name__  == "__main__":

    # TODO - get the domain from an env var, eg:
    # DOMAIN_ROOT="staging.idpd.uk"
    DOMAIN_ROOT = "" # get it from an env var

    # Initiate the crawlers in a controlled way so
    # we can make sure none of them error during this
    # Note: "dataset api" is the real/post-poc name for
    # the api we built.
    instanitated_crawler_list = []
    for crawler in [DatasetApiCrawler]: # Add more when we have more, just dataset to begin with
        try:
            instanitated_crawler_list.append(
                crawler(BASE_DOMAIN)
            )
        except Exception as err:
           # NOTE - you CAN (and should) raise here, if it
           # wont start it wont get deployed which is the correct
           # behaviour for failed instantiation.
           # Beyond this level you do NOT want to 
           # be raising uncontroled errors as we dont
           # want a dployed app falling over.
            ...

    crawl(instanitated_crawler_list)