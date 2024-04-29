This is an extention to BeatuifulSoup, adding additional code using its own functions

To run:
The main outward function is URLScraper.find_X(), inputting a URL and an X value.
The url should be inputted in a www.webname.suffix, and the X value should be an integer.
Avoid X values above 3 or 4, since the find_X() function is recursive, and more than 3 recursions can cause python
to overload.
The function returns a dictionary with {hostname: [sites]} format

External Installs:
Install bs4 via PIP or the Python Packages tab
requests and urlib may be installed already, but update them via PIP or the Python Packages tabs to their
most recent version

For simplier test runs:
Run find_linked_sites, which only does an X=1 search

Presentation:
https://docs.google.com/presentation/d/1-wTn6mGHTbf1GZD3bApjkGBHGsuRdSQYuWxBwQegWGA/edit?usp=sharing