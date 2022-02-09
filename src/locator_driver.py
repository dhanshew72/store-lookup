import time
from locator import Locator


class LocatorDriver:

    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.time_between_requests = 2

    def check(self, max_stores=3):
        time.sleep(self.time_between_requests)
        result = Locator(self.zipcode, max_stores).get_store_ids()
        return result
