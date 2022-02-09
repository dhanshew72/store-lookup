import time
from store import Store


class StoreDriver:

    def __init__(self, product_id, store_ids):
        self.product_id = product_id
        self.store_ids = store_ids
        self.time_between_requests = 2

    def check(self):
        results = []
        for store_id in self.store_ids:
            """
            Used to avoid spamming the Lowe's API services
            """
            time.sleep(self.time_between_requests)
            result = Store(store_id, self.product_id).check()
            results.append(result)
        return results
