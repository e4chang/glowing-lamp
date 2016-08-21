import urllib2
import re

url_list = [
'http://www.thepremiereresidential.com/properties/san-diego/la-jolla-international-gardens/availability/',
'http://www.thepremiereresidential.com/properties/san-diego/la-jolla-international-gardens/availability/',
]
for site in url_list:
   html_content = urllib2.urlopen(site).read()

   matches = re.findall('There are currently no available units', html_content);

   if len(matches) == 0: 
      output_str = 'New listing available in site: %s'
      print(output_str, site)
   else:
      print('Still not available')
