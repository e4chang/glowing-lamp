import urllib2
import re

html_content = urllib2.urlopen('http://www.thepremiereresidential.com/properties/san-diego/la-jolla-international-gardens/availability/').read()

matches = re.findall('There are currently no available units', html_content);

if len(matches) == 0: 
   print 'Somethings there!'
else:
   print 'Still not available'