import time
from locator import Locator


class LocatorDriver:

    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.time_between_requests = 2

    def check(self):
        time.sleep(self.time_between_requests)
        result = Locator(self.zipcode).get_store_ids()
        return result
