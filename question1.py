import requests
from bs4 import BeautifulSoup
def get_filmography(actor_name):
    search_name=actor_name.replace(" ","+")
    search_url=f"https://www.imdb.com/find?q={search_name}&s=nm"
    search_response=requests.get(search_url, verify= True)
    search_soup=BeautifulSoup(search_response.text,'html.parser')
    try:

         actor_page_link = search_soup.find("td", class_="result_text").find("a")["href"]
    except TypeError:
         print("Actor not found.")
         return []
    actor_url = "https://www.imdb.com" + actor_page_link
    try:
       actor_response = requests.get(actor_url)
       actor_soup = BeautifulSoup(actor_response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching actor's IMDb page: {e}")
        return []

    filmography = []
    for film in actor_soup.find_all("div", class_="filmo-row"):
       for year in film.find_all("span", class_="year_column"):
           year_text = year.text.strip()
           film_title = film.a.text.strip()
           filmography.append((year_text, film_title))
    filmography.sort(key=lambda x: x[0], reverse=True)
    return filmography
    actor_name = input("Enter the name of the actor: ")
    filmography = get_filmography("leonardo Dicaprio")

    if filmography:
        print(f"Filmography for {actor_name}:")
        for year, film_title in filmography:
            print(f"{year}: {film_title}")
    else:
          print(f"No filmography found for {actor_name}.")