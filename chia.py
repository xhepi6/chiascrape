from bs4 import BeautifulSoup
import requests
import time
from win10toast import ToastNotifier

toast = ToastNotifier()

my_animes_file = open("myanimes.txt","r")
last_checked = open("lastchecked.txt", "w")
last_checked_read = open("lastchecked.txt", "r")
with open("myanimes.txt") as myanimes:
    myanimelist = myanimes.read().splitlines()


#-------------------------------------------------------------------------------
#securing chia-anime link from google-search (because it changes frequently)

'''
searchlink = "https://www.google.com/search?q=chia-anime&oq=chia-anime&aqs=chrome..69i57j69i60l2.2599j0j4&sourceid=chrome&ie=UTF-8"
url = requests.get(searchlink)
html = url.text
htmlcode = BeautifulSoup(html, 'html.parser')
print(htmlcode)
firstresult = htmlcode.find("div",{"class":"g"})
print(firstresult)
_chialink = firstresult.a['href']
chialink = _chialink[7:]
#-------------------------------------------------------------------------------
'''
chialink = 'http://www.chia-anime.com'

#prepares chia-anime link to be scraped
url = requests.get(chialink)
html = url.text
htmlcode = BeautifulSoup(html, 'html.parser')


animelist = last_checked_read.read()

#scrapes and fills a list with animes and their episodes from the first page of chia-anime's homepage
#for post in htmlcode.find_all("div",{"class":"post"}):
#    anime = []
#    title = post.center.div.getText()
#    episodenumber = post.span.getText()
#    animelist.append(title + " / " + episodenumber)

#repeatedly checks for new animes
while True:
    time.sleep(5)
    _animelist = []
    for post in htmlcode.find_all("div",{"class":"post"}):
        anime = []
        title = post.center.div.getText()
        episodenumber = post.span.getText()
        _animelist.append(title + " / " + episodenumber)
        print(_animelist)
    try:
        if animelist.index(_animelist[0]) == 0:
            #no new animes
            print("No new anime")
        #found new animes
        else:
            print("New animes")
            try:
                newanimes = _animelist.index(animelist[0])
                print(newanimes)
                toast.show_toast("New Anime" , newanimes, icon_path= None, duration = 5)
                
                while anime in newanimes:
                    while myanime in myanimelist:
                        if myanime in anime:
                            pass
            except ValueError:
                pass
    except ValueError:
        pass

'''       
with open("myanimes.txt") as myanimes:
    myanimelist = myanimes.read().splitlines() = len(_animelist)
    print(newanimes)

    counter = 0
    while counter < newanimes:
        for anime in_animelist[counter]
        counter = counter + 1
    animelist = _animelist
    last_checked.write(str(animelist))
'''
