# Author: Samuel Vaudo
# Class: CSI-260-01
# Certification of Authenticity:
# I certify that this is entirely my own work, except where I have given fully documented
# references to the work of others. I understand the definition and consequences of
# plagiarism and acknowledge that the assessor of this assignment may, for the purpose of
# assessing this assignment reproduce this assignment and provide a copy to another member
# of academic staff and / or communicate a copy of this assignment to a plagiarism checking
# service(which may then retain a copy of this assignment on its database for the purpose
# of future plagiarism checking).
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import requests


class URLScraper:

    @classmethod
    def get_base_url(cls, url: str):
        '''
        Gets the base URL of a given URL, converting www.webname.com --> webname.com
        :param url: URL to be converted to just the base URL
        :return: the base URL
        '''
        return str(urlsplit(url)[1])

    @classmethod
    def get_url_plaintext(cls, url: str):
        '''
        Get the HTML of a website, given a websitename.com format
        :param url: URL of website, in websitename.com format
        :return: plaintext HTML of website URL
        '''
        urlnew = 'https://' + cls.get_base_url(url)  # adds https:// to all URLs, as well as accounting
        # for those who had it before
        text1 = requests.get(url).text
        return text1

    @classmethod
    def find_links_url(cls, url: str):
        '''
        Gets all the links from a URL that is not a relative link
        :param url: URL of website, in websitename.com format
        :return: List of links from the website.
        '''
        link_list = []
        html = cls.get_url_plaintext(url)
        soup = BeautifulSoup(html, 'html.parser')
        for text in soup.find_all('a'):
            link = text.get('href')
            if link is not None:  # sometimes the URL scrapers return none, as they cant find a href
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
        :param url: URL of website, in websitename.com format
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
    def find_linked_sites(cls, url: str):
        '''
        This finds all URLs that are found on a specific page.
        :param url: the URL of the site requested, in websitename.com format
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

    @classmethod
    def find_next(cls, dictionary: dict, original_url: str, X: int):
        '''
        Finds all URLs to a depth X, given its inital dictionary find, as well as its URL
        :param dictionary: the inital dictionary it starts with.
        :param original_url: the URL that is set as the starting point
        :param X: The number of times this function will repeat, finding only unique links along the way
        :return: dictionary of all the results found related to the URL
        '''
        if X <= 0:
            return dictionary
        new_site_list = dict(dictionary)
        for site in dictionary.keys():
            for link in dictionary[site]:
                try:
                    temp_site_list = cls.find_linked_sites(link)
                except requests.exceptions.MissingSchema:
                    continue
                for key in temp_site_list.keys():
                    if key == cls.get_base_url(original_url):
                        continue
                    if key in dictionary.keys():
                        set1 = set(new_site_list[key])
                        set2 = set(temp_site_list[key])
                        unique_adds = set2 - set1
                        new_site_list[key] = list(set1) + list(unique_adds)
                    else:
                        new_site_list[key] = temp_site_list[key]
        final_list = cls.find_next(new_site_list, original_url, X - 1)
        return final_list

    @classmethod
    def find_X(cls, url: str, X: str):
        '''
        combines previous function to find all URLs with depth X
        :param url: The URL to be searched
        :param X: The number of times find_next will be run, must be > 0, else return None
        :return: The full dictionary of all unique related links
        '''
        if X <= 0:
            return None
        else:
            inital_dict = cls.find_linked_sites(url)
            final_dict = cls.find_next(inital_dict, url, X)
            return final_dict

