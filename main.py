from store_driver import StoreDriver
from locator_driver import LocatorDriver


def main():
	store_ids = LocatorDriver("98406").check(4)
	result = StoreDriver("5001928007", store_ids).check()
	print(result)
	print(len(result))


if __name__ == '__main__':
	main()
