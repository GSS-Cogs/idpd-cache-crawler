from abc import ABC, ABCMeta, abstractmethod
from typing import Optional
import os

def _get_delay_from_env(env_var_for_crawler: Optional[str]) -> int:
        # TODO - check for the specified env var
        # if env_var_for_crawler is None return a default
        # of 30 seconds.
        # Otherwise, RAISE an error if:
        # - the env var does not exist
        # - the env var cannot be cast to an int
        # - the end var is less than 5 seconds or greater
        #   than 120 (this number is in seconds)
        return 30

def _get_headers() -> dict:
        # This is where we set the headers for all request for this
        # crawler. For example cache control no cache.
        # There will be times where we'll want to specifiy additional
        # headers to to be included in requests as well.
        # For example the username and password where 
        # the service in question is behing a basic auth wall.

        # declaring header with cache control no cache
        headers = {
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
        }

        ADDITIONAL_HEADERS = os.getenv('ADDITIONAL_HEADERS')
        if ADDITIONAL_HEADERS:
            # remove white spaces and consecutive white spaces from ADDITIONAL_HEADERS
            "".join(ADDITIONAL_HEADERS.split())
            
            HEADERS = ADDITIONAL_HEADERS.split(",")
            for values in HEADERS:
                if "=" not in values:
                    raise Exception(f'''
                        Some HEADERS in ADDITIONAL_HEADERS are not key value pairs
                        
                        HEADERS: {HEADERS}
                        ADDITIONAL_HEADERS: {ADDITIONAL_HEADERS}
                        ''')
            for header in HEADERS:
                key_and_value = header.split("=")
                if len(key_and_value)==2:
                    headers.update({key_and_value[0] : key_and_value[1]})
                else:
                    raise Exception(str(f'''
                        Malformed entry, eg: key=value=typo or key==value
                                    
                        HEADER: {key_and_value}
                        '''))
        
        return headers
        

      
    
class BaseCrawler(ABC):

    def __init__(self, domain: str, delay_from_env_var: str = None):
        # TODO: You'll want to make sure this is reachable and
        # error the instantiation if not.
        # This is true for anything you do at this stage, either
        # (a) you've confirmed it works or (b) you've error'd so
        # it doesnt get deployed in a non functional state.
        self.domain = domain
        self.delay = _get_delay_from_env(delay_from_env_var)
        self.request_headers = _get_headers()

    @abstractmethod
    def crawl(self):
        """
        Crawl the web resources this crawler is desgined to crawl.
        """
        # Implemented in the inheriting class, not here.
        ...

    # NOTE - not an abstract, a get (with a no cache header) is
    # the same for all crawlers
    # so implement it here. 
    # TODO 1 - should take a url and make a request.get() at it
    # with NO CACHE headers (use self.domain here).
    # TODO 2 - should have exponential backoff to retry in the
    # event of errors - see https://pypi.org/project/backoff/
    # NOTE - do not put the delay between gets in the implemented crawl()
    # function not here.
    # Note: you dont need to do anything with the get or return
    # anything, just make sure its an acceptable (i.e it worked)
    # status code. If you don't get an acceptable code, log the
    # error but keep on going.
    def no_cache_get(self, url: str):
        """
        
        """
        ...