from dotenv import load_dotenv
import os

load_dotenv()
SELLERLIMIT = int(os.getenv("seller_limit"))


def productlist_limit_1lvl(api_output, attributename):
    if len(api_output[attributename]) > SELLERLIMIT:
        result = {
            "ItemList": api_output[attributename][:SELLERLIMIT],
            "IsLimit": True,
            "IsEmpty": False,
            "Message": "List has been limited. Please refine search."
        } 
    elif len(api_output[attributename]) == 0:
        result = {
            "ItemList": api_output[attributename][:SELLERLIMIT],
            "IsLimit": False,
            "IsEmpty": True, 
            "Message": "No product found. Please refine search."
        } 
    else:
        result = {
            "ItemList": api_output[attributename],
            "IsLimit": False,
            "IsEmpty": False, 
            "Message": ""
        }
    return result

def productlist_limit_2lvl(api_output, attributename_1lvl, attributename_2lvl ):
    if len(api_output[attributename_1lvl][attributename_2lvl]) > SELLERLIMIT:
        result = {
            "ItemList": api_output[attributename_1lvl][attributename_2lvl][:SELLERLIMIT],
            "IsLimit": True,
            "IsEmpty": False,
            "Message": "List has been limited. Please refine search."
        } 
    elif len(api_output[attributename_1lvl][attributename_2lvl]) == 0:
        result = {
            "ItemList": api_output[attributename_1lvl][attributename_2lvl][:SELLERLIMIT],
            "IsLimit": False,
            "IsEmpty": True, 
            "Message": "No product found. Please refine search."
        } 
    else:
        result = {
            "ItemList": api_output[attributename_1lvl][attributename_2lvl],
            "IsLimit": False,
            "IsEmpty": False, 
            "Message": ""
        }
    return result