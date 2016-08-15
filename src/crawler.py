import urllib
import time
# import re
from HTMLParser import HTMLParser
urls = ['http://www.thepremiereresidential.com/properties/san-diego/la-jolla-international-gardens/availability/']
link = urllib.urlopen(urls[0])
update = link.read()


# create a subclass and override the handler methods
class InitialParser(HTMLParser):
    root_links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    if value not in self.root_links:
                        print 'adding', value
                        self.root_links.append(value)
                    else:
                        print 'ignoring', value

# instantiate the parser and fed it some HTML
parser = InitialParser()
parser.feed(update)
#print parser.root_links

time.sleep(3)

link = urllib.urlopen(urls[0])
update = link.read()
parser.feed(update)

#print parser.root_links