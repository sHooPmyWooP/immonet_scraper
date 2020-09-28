import requests as req
import re
import json
from bs4 import BeautifulSoup
from time import sleep
import random
import pandas as pd

from .models import Item, Item_Details


def immonet_scraper():
    link = "https://www.immonet.de/immobiliensuche/sel.do"
    max_page_result = re.findall("page=\d*", req.get(link, params=set_params(0)).text)
    max_page = [int(i.replace("page=", "")) for i in max_page_result]
    max_page.sort(reverse=True)
    max_page = max_page[0]

    for i in range(max_page):
        page = i + 1
        request = req.get(link, params=set_params(page=page)).text
        result = BeautifulSoup(request, "html.parser")

        items = result.findAll("div", {"class": "item"})
        ids = [item.a.get("data-object-id") for item in items]

        for id in ids:
            item = Item.objects.get_or_create(
                id=id
            )[0].save()

            item_detail = Item_Details.objects.get_or_create(
                id=id
            )[0].save()

        print(f"Page {page}/{max_page} scanned")
    return


def set_params(page=0):
    params = {
        "page": page,
        "pageoffset": 1,
        "listsize": 26,
        "objecttype": 1,
        "locationname": "Norderstedt",
        "city": 123249,
        "ajaxIsRadiusActive": True,
        "sortby": 19,
        "suchart": 2,
        "radius": 0,
        "pcatmtypes": "2_1",
        "pCatMTypeStoragefield": "2_1",
        "parentcat": 2,
        "marketingtype": 1,
        "fromprice": None,
        "toprice": 1000000,
        "fromarea": 75,
        "toarea": 120,
        "fromplotarea": None,
        "toplotarea": None,
        "fromrooms": 2,
        "torooms": None,
        "objectcat": -1,
        "wbs": -1,
        "fromyear=": None,
        "toyear": None
    }
    return params


def update_items():
    items = [item for item in Item_Details.objects.filter()]
    for item in items:
        update_item(item)
        sleep_time = round(random.randint(50, 200) / 100, 2)
        print(f"Item {item.id} saved, sleeping {sleep_time}")
        sleep(sleep_time)
    return


def update_item(item):
    baselink = "https://www.immonet.de/angebot/"
    item_detail = Item_Details.objects.get_or_create(id=item.id)[0]
    item_detail.link = baselink + str(item.id)
    soup = BeautifulSoup(req.get(item_detail.link).text, "html.parser")

    item_detail.description = ""
    for tag, html_id in [("p","objectDescription"), ("p","otherDescription"), ("p","locationDescription")]:
        try:
            descr = soup.find(tag, {"id" : html_id}).text
            item_detail.description += "|||"+html_id+"|||"+ descr if descr else ""
        except AttributeError:
            print("attr")
            continue

    scripts = soup.findAll("script")
    dict_found = None

    for script in scripts:
        try:
            if re.search("sdmTargetingParams", script.contents[0]):
                dict_found = script
                break
        except:
            continue

    if not dict_found:
        print("dict not found:", item.id)
        return

    with open("attr_mapping.json", "r") as f:
        attr_mapping = json.load(f)

    attrs = json.loads(re.findall(r"{.*}", dict_found.contents[0])[0])
    for k, v in attr_mapping["immonet"].items():
        setattr(item_detail, k, attrs.get(v))

    item_detail.save()

    return
