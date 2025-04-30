import requests

def zalora_search(query, enable_relevance_classifier, full_facet_category, image_format, image_quality, image_resize, shop, sort, sort_dir):
    
    url = "https://api.zalora.sg/v1/dynproducts/datajet/list"

    param = {
        "enableRelevanceClassifier": enable_relevance_classifier,
        "fullFacetCategory": full_facet_category,
        "image_format": image_format,
        "image_quality": image_quality,
        "image_resize": image_resize,
        "query": query,
        "shop": shop,
        "sort": sort,
        "dir": sort_dir
    }
    
    header = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    
    response = requests.get(url, params=param, headers=header)
    
    return response.json()



    
