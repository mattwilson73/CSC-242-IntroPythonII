# Completed by myself
#Matt Wilson
import os

def Indexer(root):
    'recursively crawl through a directory structure comibining all the text contents into one string with path'
    ss = ''
    for item in os.listdir(root):
        n = os.path.join(root, item)
        if os.path.isdir(n):
            ss += Indexer(n)
        
        else:
            
            f = open(n,'r')
            s = f.read()
            f.close()
            
            newtxt = 'Path : ' + n + '\n' +s + '\n'
            ss += newtxt
    return ss




def findAllDirectoriesWithFiles(root):
    'return a list of all directories that contain files'
    lst = []
    for item in os.listdir(root):

        n = os.path.join(root,item)
        if os.path.isdir(n):
            lst += (findAllDirectoriesWithFiles(n))
            
        else:
            if root not in lst:
                
                lst.append(root)
    return lst
    


def fileContentsLength(root):
    'recursivly crawl a directory structure and get the total character count of all the file in the folder '

    localcount = 0
    
    for item in os.listdir(root):
        
        n = os.path.join(root,item)
        
        if os.path.isdir(n):
            localcount += fileContentsLength(n)
            
        else:
            f=open(n,'r')
            s=f.read()
            localcount += len(s) 
            f.close()
    return localcount




from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

def testLParser(url):
    content = urlopen(url).read().decode()
    parser = ListParser()
    parser.feed(content)
    return parser.getListItems()

class ListParser(HTMLParser):
    '''
    returns links found in HTML from url
    '''
    def __init__(self):
        HTMLParser.__init__(self)
        self.foundlist = False
        self.listitems = []
        
        
    def handle_starttag(self, tag, attrs):
        if tag == 'ol' or tag == 'li' or tag == 'ul':
            self.foundlist = True

    def handle_endtag(self, tag):
        if tag == 'ol' or tag == 'li' or tag == 'ul':
            self.foundlist = False
            
    def handle_data(self, data):
        if self.foundlist == True:
            self.listitems.append(data.strip())
        
    def getListItems(self):
        return self.listitems

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

#'https://www.gamespot.com/news/'

def testGamespotNewsParser(url):
    content = urlopen(url).read().decode()
    parser = GamespotNewParser()
    parser.feed(content)
    return parser.getNews()

class GamespotNewParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.news=[]
        self.sectionAllowed=False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'h3':
            for attr in attrs:
                if attr[0] == 'class':
                    if attr[1] == 'media-title':
                        self.sectionAllowed = True
                    else:
                        self.sectionAllowed = False

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.sectionAllowed = False
            
    def handle_data(self, data):
        data = data.strip()
        if self.sectionAllowed == True and data != '':
            self.news.append(data)
        
    def getNews(self):
        return self.news


#txt=Indexer('Test')
#print(txt)
#print(findAllDirectoriesWithFiles('Test'))
#print(fileContentsLength('Test'))
#print(testLParser('http://zoko.cdm.depaul.edu/csc242/lists.html'))
print(testGamespotNewsParser('https://www.gamespot.com/news/'))

