import requests


class Store:

    def __init__(self, id, product_id):
        self.product_id = product_id
        self.base_url = 'https://lowes.com'
        self.url = "{}/pd/{}/productdetail/{}/Guest".format(self.base_url, self.product_id, id)
        """
        Lowes checks for user agent and other headers that need to be added to requests call
        My guess is to avoid abuse on the API with spam.
        Reference: https://stackoverflow.com/a/58266926
        """
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Upgrade-Insecure-Requests": "1"
        }
        self.result = requests.get(self.url, headers=self.headers).json()

    def check(self):
        return {
            "availability": self.get_availability(),
            "url": self.get_product_url(),
            "address": self.get_address()
        }

    def get_availability(self):
        availabilities = []
        field_checks = [
            {
                "field": "parcel",
                "msg": "Available via delivery"
            },
            {
                "field": "pickup",
                "msg": "Available via pickup at store"
            }
        ]
        inventory = self.result['inventory']
        for field_check in field_checks:
            field = field_check['field']
            if inventory['analyticsData'][field]['isAvlSts']:
                availabilities.append(field_check['msg'])
        return availabilities

    def get_product_url(self):
        return self.base_url + self.result['productDetails'][self.product_id]['product']['pdURL']

    def get_address(self):
        store_details = self.result['storeDetails']
        return {
            'address': store_details['address'],
            'city': store_details['city'],
            'state': store_details['state'],
            'zip': store_details['zip']
        }
