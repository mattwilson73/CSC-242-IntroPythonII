from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

url = 'http://zoko.cdm.depaul.edu/csc242/helloworld.html'
listurl = 'http://zoko.cdm.depaul.edu/csc242/lists.html'

def testParser(url):
    content = urlopen(url).read().decode()
    parser = LinkParser()
    parser.feed(content)

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'ol':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])
