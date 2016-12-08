import requests
import re
import pprint

page = "https://pythonspot.com"
respond = requests.get(page)
#respond.content - parse web page like html page with all the shit with scripts of javascript
#respond.text - parse info from page like text as we see it
#print(respond.ok) # - get code of respond from web page (код возврата хорошего 200)

if not respond.ok:
    raise AssertionError("Page not found!!!")

text = respond.text

#-------- method with compiling of template --------
template = re.compile("<li>.*?</li>")
result = template.findall(text, re.IGNORECASE | re.MULTILINE)    #re.IGNORECASE | re.MULRILINE - in previous versions
pprint.pprint(result)



