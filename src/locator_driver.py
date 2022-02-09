import time

import settings
from locator import Locator


class LocatorDriver:

    def __init__(self, zipcode):
        self.zipcode = zipcode

    def check(self, max_stores=3):
        time.sleep(settings.SECONDS_BETWEEN_REQUESTS)
        result = Locator(self.zipcode, max_stores).get_store_ids()
        return result
