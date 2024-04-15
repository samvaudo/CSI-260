from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse, urlsplit, urlunsplit
import requests


class URLScraper:

    @classmethod
    def get_base_url(cls, url: str):
        return str(urlsplit(url)[1])

    @classmethod
    def get_url_plaintext(cls, url: str):
        '''
        Get the HTML of a website, given a www.websitename.com format
        :param url: URL of website, in www.websitename.com format
        :return: plaintext HTML of website URL
        '''
        urlnew = 'https://' + cls.get_base_url(url)
        print(urlnew)
        text1 = requests.get(url).text
        return text1

    @classmethod
    def find_links_url(cls, url: str):
        '''
        Gets all the links from a URL that is not a relative link
        :param url: URL of website, in www.websitename.com format
        :return: List of links from the website.
        '''
        link_list = []
        html = cls.get_url_plaintext(url)
        soup = BeautifulSoup(html, 'html.parser')
        for text in soup.find_all('a'):
            link = text.get('href')
            if link is not None:  # sometimes the URL scrapers return none, as they cant find an href
                if (cls.get_base_url(url) not in link) and ('http' in link):  # is this link an absolute link?
                    link_list.append(link)
                else:
                    # link_list.append(url + text)
                    continue
            else:
                continue

        return link_list

    @classmethod
    def find_image_links_url(cls, url: str):
        '''
        Gets all sources of images from a URL that is not a relative link
        :param url: URL of website, in www.websitename.com format
        :return: List of image links
        '''
        image_list = []
        html2 = cls.get_url_plaintext(url)
        soup = BeautifulSoup(html2, 'html.parser')
        for img in soup.find_all('img'):
            link = img.get('src')
            if link is not None:  # sometimes the URL scrapers return none, as they cant find a src
                if (cls.get_base_url(url) not in link) and (
                        'http' in link):  # is this image referencing an absolute link?
                    image_list.append(link)
                else:
                    # image_list.append(url + link)
                    continue
            else:
                continue

        return image_list

    @classmethod
    def find_linked_sites(cls,url: str):
        '''
        This finds all URLs that are found on a specific page.
        :param url: the URL of the site requested, in www.websitename.com format
        :return: all domains connected to the site given, as a dictionary.
        '''
        site_list = {}
        href_links = cls.find_links_url(url)
        img_links = cls.find_image_links_url(url)
        for link in href_links:
            base = cls.get_base_url(link)
            if base not in site_list:
                site_list[base] = [link]
            else:
                site_list[base].append(link)

        for img in img_links:
            base = cls.get_base_url(img)
            if base not in site_list:
                site_list[base] = ['image-related']
            else:
                continue
        return site_list


print(URLScraper.find_linked_sites('http://www.python.org'))
