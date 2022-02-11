from fastapi import APIRouter
from fastapi import Depends

from models.search import SearchIn
from services.locator_driver import LocatorDriver
from services.store_driver import StoreDriver

router = APIRouter()


@router.get("")
def read(search_in: SearchIn = Depends()):
    store_ids = LocatorDriver(search_in.zipcode).check(search_in.max_stores)
    result = StoreDriver(search_in.product_id, store_ids).check()
    return result
