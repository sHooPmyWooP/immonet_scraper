from django.shortcuts import render
from django.http import HttpResponse
from .scraper import immonet_scraper, update_items


def scraper(request):
    immonet_scraper()
    return HttpResponse("<h1>Scraping IDs</h1>")


def scraper_update(request):
    update_items()
    return HttpResponse("<h1>Updating Items</h1>")
