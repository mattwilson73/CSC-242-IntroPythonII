
    
from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import Request,urlopen

def testStatParser(url):
    req = Request(url)
    req.add_header('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4056.0 Safari/537.36 Edg/82.0.432.3')
    content = urlopen(req).read().decode()

    parser = StatParser()
    parser.feed(content)
    return parser.getTagCounts()
    

class StatParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        
        
    def handle_starttag(self, tag, attrs):
        pass

           
    def getTagCounts(self):
        pass


from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END
from tkinter.messagebox import showinfo


class BrowserGUI(Tk):
    'Browser GUI'
    def __init__(self,parent=None):
        'Constructor'
        pass

    def getStats(self):
        'Called to get the stats of the page entered int the edit box'
        pass

    def writeToFile(self):
        'write all the stats to a file'
        pass



    def make_widgets(self):
        'create the UI'
        pass


