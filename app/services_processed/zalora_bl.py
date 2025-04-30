from app.services import zalora
from app.utils import common_func, common_class
from typing import Dict, Any
import urllib.parse
from dotenv import load_dotenv
import os

load_dotenv()
IMAGEFORMAT = os.getenv("image_format")
IMAGEQUALITY = os.getenv("image_quality")
IMAGERESIZE = os.getenv("image_resize")


def safe_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return 0.0

def safe_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0


def zalora_dataresponse(raw: Dict[str, Any]) -> common_class.DataResponse:
    raw_products = raw["ItemList"]
    items = []

    for product in raw_products:
        items.append(common_class.ProductList(
            Name=product.get("Name", ""),
            NormalPrice=product.get("Price", ""),
            SpecialPrice=product.get("SpecialPrice", ""),
            Brand=product.get("Brand", ""),
            ImageList=product.get("ImageList", []),
            MainImageUrl=product.get("MainImageUrl"),
            Category=product.get("Breadcrumbs", []),
            AvgRating=safe_float(product["ReviewStatistics"].get("AvgRating", 0)),
            ReviewCount=safe_int(product["ReviewStatistics"].get("ReviewCount", 0)),
            ProductUrl= "https://www.zalora.sg/" + product.get("ProductUrl", ""),
            Seller = "Zalora"
        ))


    return common_class.DataResponse(
        items=items
    )

def GET_zaloraproductlist(query = "",sort = "", sort_dir = "desc",image_format = "webp", image_quality = "70", image_resize = "533.4x770"):
    query_encoded = urllib.parse.quote(query)
    zalora_raw = zalora.zalora_search(query_encoded,"true","true",image_format,image_quality,image_resize,"m",sort, sort_dir)
    zalora_processed = common_func.productlist_limit_2lvl(zalora_raw,"data","Products")
    
    return zalora_dataresponse(zalora_processed)