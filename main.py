from store_driver import StoreDriver
from locator import Locator


def main():
	store_ids = Locator("98406").get_store_ids()
	result = StoreDriver("5001928007", store_ids).check()
	print(result)
	print(len(result))


if __name__ == '__main__':
	main()
