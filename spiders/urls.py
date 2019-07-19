import json

# urls
urls = []
# get json values
with open('D:\\image\\scraper\\forsale.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    urls.append(distro['url'])
