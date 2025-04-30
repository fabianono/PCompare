import requests
import urllib.parse

def lazada_search(query, sort):
    #sort = pricedesc or priceasc
    tag = query.replace(" ", "-")
    query_encoded = urllib.parse.quote(query)
    url = f"https://www.lazada.sg/tag/{tag}/"


    param = {
        "ajax": "true",
        "q": query_encoded,
        "sort": sort,
    }
    
    header = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    
    response = requests.get(url, params=param, headers=header)
    
    return response.text


print(lazada_search("white tee",""))