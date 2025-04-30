from app.services import lazada
from app.utils import common_func, common_class
from typing import Dict, Any


def lazada_dataresponse(raw: Dict[str, Any]) -> common_class.DataResponse:
    raw_products = raw["ItemList"]
    items = []

    for product in raw_products:
        items.append(common_class.ProductList(
            Name=product.get("name", ""),
            NormalPrice=product.get("originalPriceShow", ""),
            SpecialPrice=product.get("priceShow", ""),
            Brand=product.get("brandName", ""),
            ImageList=[product.get("image")] if product.get("image") else [],
            MainImageUrl=product.get("image"),
            Category=[],
            #Category=product.get("Breadcrumbs", []),
            AvgRating=float(product.get("ratingScore") or 0),
            ReviewCount=int(product.get("review") or 0),
            ProductUrl= product.get("itemUrl", ""),
            Seller = "Lazada"
        ))

    return common_class.DataResponse(
        items=items
    )


def GET_lazadaproductlist(query = "",sort = ""):
    lazada_raw = lazada.lazada_search(query, sort)
    lazada_processed = common_func.productlist_limit_2lvl(lazada_raw,"mods","listItems")

    return lazada_dataresponse(lazada_processed)

    
print(GET_lazadaproductlist("white tee",""))