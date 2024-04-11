from bs4 import BeautifulSoup
import urllib.request as urllib1
from urllib.parse import urlparse


class URLScraper:

    @classmethod
    def get_url_plaintext(cls, url: str):
        '''
        Get the HTML of a website, given a http://websitename.com format
        :param url: URL of website, in http://websitename.com format
        :return: plaintext HTML of website URL
        '''
        dec = urllib1.urlopen(url).read()
        text = dec.decode('utf-8')
        return text

    @classmethod
    def find_links_url(cls, url: str):
        '''
        Gets all the links of refrence of a website url
        :param url: URL of website, in http://websitename.com format
        :return: List of links from the website.
        '''
        link_list = []
        html = cls.get_url_plaintext(url)
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            text = link.get('href')
            if bool(urlparse(text).netloc):  # is this link an absolute link?
                link_list.append(text)
            else:
                if text[0] != '#' and text != '/':  # filters for redirects in page and empty links
                    link_list.append(url + text)
                else:
                    continue

        return link_list


print(URLScraper.find_links_url("http://python.org"))
