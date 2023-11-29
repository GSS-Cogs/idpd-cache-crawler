from .models import BaseCrawler

class DatasetApiCrawler(BaseCrawler):

    # TODO - implement in full
    def crawl(self):
        """
        Crawl the web resources this crawler is desgined to crawl.
        """

        # We want to:
        # - send a get request with a cache-control no cache header (to refresh
        # the cached response seen by the public).
        # use the self.no_cache_get(url) method from the base call to do this.
        # delay before next request then next request.
        # USE A LOCAL API RUNNING while developing, that way you can remove the
        # delay and speed up the dev process. DONT just rinse the api in
        # staging please.

        # TODO - pseudocode follows:
        #
        # get /datasets
        #     for each dataset:
        #         get datasets/{dataset_id}:
        #              for each datasets/{dataset_id}
        #                   get all datasets/{dataset_id}/editions
        #                      for each edition
        #                          get /datasets/{dataset_id}/editions/{edition_id}
        #                               get /datasets/{dataset_id}/editions/{edition_id}/versions
        #                                  for each version
        #                                       get /datasets/{dataset_id}/editions/{edition_id}/versions
        #
        # Repeat similar steps
        # /topics
        # /topics/{topic_id}
        # /topics/{topic_id}/subtopic
        # /publisher
        # /publishers/{publisher_id}
        #
        # Use the self.no_cache_get() you've created elsewhere to make
        # the request, but remember to try catch in case any errors raise
        # (again, log not raise them).
        # Also, check the default settings for requests and explicitly tell it not to cache
        # response (if it does), we want genuine crawler to api traffic on each call.
        ...