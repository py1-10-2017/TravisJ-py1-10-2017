import requests
response = requests.get(
    'http://api.wunderground.com/api/fcbc0b24b72db0ea/conditions/q/WA/Seattle.json')
print response
