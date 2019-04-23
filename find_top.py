import requests
from bs4 import BeautifulSoup
import json


def getFromFile(nameOfFile, whatNeed):
    '''Country selection'''
    f = open(nameOfFile, 'r')
    result = "Nothing"
    for line in f:
        if (line.find(whatNeed) != -1):
            result = line.split(" ")[0].strip()
            break
    return result


def getRssChannel(name, howMuch, isFree):
    '''Create url '''
    name = getFromFile("Cods.txt", name)
    return "https://rss.itunes.apple.com/api/v1/%s/ios-apps/%s/all/%s/explicit.json" % (name.lower(), "top-free" if isFree else "top-paid", str(howMuch if howMuch <= 100 else 100))


def get_key(d, value):
    '''Get key from d '''
    for k, v in d.items():
        if v == value:
            return k


def top(url):
    '''It analyzes all the apps and makes up the top of the most popular categories of apps  '''
    categories = []
    UNIC = []
    TOP3 = {}
    if "nothing" in url:
        print("Try again. This country is not supported.")
        return
    r = requests.get(url).text
    soup = json.loads(r)
    a = soup.get('feed')
    b = a.get('results')
    # analyze every app
    for app in range(len(b)):
        c = b[app].get('genres')
        for category in range(len(c)):
            categories.append(c[category].get('name'))
    for o in range(len(categories)):
        if categories[o] not in UNIC:
            k = categories.count(categories[o])
            TOP3[categories[o]] = k
            UNIC.append(categories[o])
    print(TOP3)
    sort_list = sorted(list(TOP3.values()))
    print('The most popular is ' + get_key(TOP3, sort_list[len(sort_list)-1]))
    print('Second is ' + get_key(TOP3, sort_list[len(sort_list)-2]))
    print('Third is ' + get_key(TOP3, sort_list[len(sort_list)-3]))
    print('Fourth is ' + get_key(TOP3, sort_list[len(sort_list)-4]))
    print('Fiveth is ' + get_key(TOP3, sort_list[len(sort_list)-5]))
top(getRssChannel("Russia", 100, False))

