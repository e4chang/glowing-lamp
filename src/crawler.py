#import urllib
import time
import re
from html.parser import HTMLParser
import urllib.request
update = ''
with urllib.request.urlopen('http://www.thepremiereresidential.com/properties/san-diego/la-jolla-international-gardens/availability/') as response:
   update = str(response.read())

# create a subclass and override the handler methods
class InitialParser(HTMLParser):
    root_links = []
    listing_section = False
    pattern = re.compile('^(\\\\n|\\\\t| )')
    def handle_starttag(self, tag, attrs):
        if tag == 'article':
            for (key, value) in attrs:
                if key == 'class':
                    self.listing_section = True

    def handle_endtag(self, tag):
        if tag == 'article':
            self.listing_section = False

    def handle_data(self, data): 
        if self.listing_section and not self.pattern.match(data):
            print(data)

# instantiate the parser and fed it some HTML
parser = InitialParser()
parser.feed(update)

time.sleep(3)

