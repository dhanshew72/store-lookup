import requests


class Locator:

    def __init__(self, zipcode, max_stores=3):
        self.url = "https://www.lowes.com/store/nearbystoredetails"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41",  # noqa
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Upgrade-Insecure-Requests": "1"
        }
        self.result = requests.get(
            self.url,
            headers=self.headers,
            params={"maxResults": max_stores, "responseGroup": "large", "searchTerm": zipcode}
        ).json()

    def get_store_ids(self):
        store_ids = []
        for store in self.result['suggestions']:
            store_ids.append(store['store']['id'])
        return store_ids
