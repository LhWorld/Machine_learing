import requests
url = "http://www.cnblogs.com/LHWorldBlog/"
html = requests.get(url)
print(html.text)