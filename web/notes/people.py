import requests
import json

r = requests.get('http://uinames.com/api/?amount=2')

print 'Status: ', r.status_code
print 'Headers: ', r.headers
print 'Text: ', r.text
j = r.json()
