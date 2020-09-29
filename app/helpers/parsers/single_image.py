import app.helpers.files
from bs4 import BeautifulSoup
import requests
import json
from typing import List

class SingleImageParser:

    def __init__(self):
        return


    def recognizes(self, r: Response) -> bool:
        """
        :param r: A webpage
        :returns: True if this parser recognizes the given response, else false
        """
        # If the image in the url has a recognized file extension, this is a direct link to an image
        #  (Should match artstation, i.imgur.com, i.redd.it, and other direct pages)
        return app.helpers.files.get_extension(r).lower() in [".png", ".jpg", ".jpeg", ".gif"]


    def parse(self, r: Response) -> List[str]:
        """
        :param r: A web page that has been recognized by this parser
        :returns: A list of all scrapeable urls found in the given webpage
        """
        return [r.url]
