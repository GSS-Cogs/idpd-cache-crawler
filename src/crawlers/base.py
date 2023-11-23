from abc import ABCMeta, abstractmethod

class BaseCrawler(mata=ABCMeta):

    def __init__(self, domain: str):
        # TODO: You'll want to make sure this is reachable and
        # error the instantiation if not.
        # This is true for anything you do at this stage, either
        # (a) you've confirmed it works or (b) you've error'd so
        # it doesnt get deployed in a non functional state.
        self.domain = domain

    @abstractmethod
    def crawl(self):
        """
        Crawl the web resources this crawler is desgined to crawl.
        """

        ...

    # Note: the "between each request" delay we're using.
    # This sets the DEFAULT of 10 seconds where no other value
    # has been specified.
    # To finesses an individual crawler we just want to pass
    # in a suitable env var (some apps will require a lighter
    # touch than others).
    def get_delay_from_env(env_var_for_crawler: str) -> int:
        # TODO - see if said env var exists on the system
        # and is an interger.
        # If yes and yes, return that number, else use
        # the default of 10.
        # If its there but it cannot be case as int() then
        # log an error before you use the default.
        return 10
    
    # TODO - not an abstract, implement this here.
    # Note: the "something" below will be some variation of log
    # out a useful message (basic logs to being with, structured
    # logs can follow once the crawlers built).
    # The main this is THE CRAWLER SHOULD NEVER EVER RAISE an 
    # uncontrolled error, as it needs ti keep going.
    def handle_error(self, url: str, msg: str, error: Exception):
        """
        Do something where a crawl encounters an error.
        """

    # NOTE - not an abstract, a get (with a no cache header) is
    # the same for all crawlers
    # so implement it here. 
    # TODO 1 - should take a url and make a request.get() at it
    # with NO CACHE headers (use self.domain here).
    # TODO 2 - should have exponential backoff to retry in the
    # event of errors - see https://pypi.org/project/backoff/
    # NOTE - you can let this raise an error but you will need
    # to catch and control it in the calling code 
    # NOTE - do not put the delay between gets in the implemented crawl()
    # function not here, we want to be able to finsesse the delay
    # base on the crawler (some services will want a lighter touch
    # than others).
    # Note: you dont need to do anything with the get or return
    # anything, just make sure its an acceptable (i.e it worked)
    # status code. If you don't get an acceptable code, log the
    # error but keep on going.
    def no_cache_get(self, url: str):
        """
        
        """
        ...