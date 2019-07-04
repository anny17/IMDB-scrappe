from bs4 import BeautifulSoup

import requests

url = "https://www.imdb.com/list/ls006299443/"

r = requests.get(url)

soup = BeautifulSoup(r.content)

group_data = soup.find_all("div",{"class" : "lister-item-content"})
data = []
for item in group_data:
  a = item.contents[1].find_all("a")[0].text
  '''count = 0
  for i in item:
    print(count,i)
    count += 1
    '''
  b = item.contents[5].find_all("span")[1].text
  zzz = item.contents[9].find_all("a")
  lll = len(zzz)
  vec = []
  for i in range(lll):
    vec.append(zzz[i].text)
  tem = []
  tem.append(a)
  tem.append(b)
  tem.append(vec)
  data.append(tem)
print(data)
