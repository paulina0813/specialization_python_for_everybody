import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count: "))
position = int(input("Enter a position: "))


for i in range(1,count+1,1):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    iteration = 0
    for tag in tags:
    #print(tag.get('href', None))
        iteration += 1
        if iteration == position:
            iteration = 0
            new_url = tag.get('href', None)
            url = new_url
            print(new_url)
            break

