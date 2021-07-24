#https://www.merakilearn.org/course/76/exercise/1930
def scrape_top_list():
    import json
    import requests
    from bs4 import BeautifulSoup
    url = BeautifulSoup(requests.get("https://www.imdb.com/india/top-rated-indian-movies/").content,"html.parser").find('tbody', class_="lister-list")
    title = url.find_all('td',class_='titleColumn')
    rating = url.find_all('td',class_='ratingColumn imdbRating')
    k = [i.strong.text for i in rating]
    movies = []
    ind = 1
    for i in title:
        b = {}
        b["Name"] = i.a.text
        b["year"] = i.span.text.replace('(',"").replace(")","")
        b["postion"] = ind
        b["Rating"] = k[ind-1]
        b["url"] = "https://www.imdb.com" + i.a["href"]
        ind += 1
        movies.append(b)
    vk = open("v.json","w")
    json.dump(movies,vk,indent=4)
    return movies
