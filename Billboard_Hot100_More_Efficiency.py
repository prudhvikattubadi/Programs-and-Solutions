import bs4
import requests
from operator import itemgetter

url = 'http://www.billboard.com/charts/hot-100'

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "html.parser")
len_titlename = []
artist_data = []
artist_name = []
tracklen_artistname = []
tracklen_artistname_list=[]
tracklen_artistname_sorted=[]

track_soup = soup.find_all("span", {"class":"chart-element__information__song text--truncate color--primary"})
artist_soup = soup.find_all("span", {"class":"chart-element__information__artist text--truncate color--secondary"})

for titlename, artistname in zip(track_soup,artist_soup):
    len_titlename = len(titlename.string)
    artist_data = artistname.string
    tracklen_artistname = [[len_titlename, artist_data]]
    tracklen_artistname_list.extend(tracklen_artistname)
    tracklen_artistname_sorted=sorted(tracklen_artistname_list, key=itemgetter(0))
print(tracklen_artistname_sorted)