import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
movies = soup.select(".titleColumn a")

print(soup)

for movie in movies[:10]:
    link = "https://www.imdb.com" + movie.get("href")
    movie_response = requests.get(link, headers=headers)
    if movie_response.ok:
        movie_soup = BeautifulSoup(movie_response.content, "html.parser")
        # Extract movie name
        try:
            movie_name = movie_soup.select_one('h1').text.strip()
        except AttributeError:
            movie_name = "N/A"
        
        # Extract movie year
        try:
            movie_year = movie_soup.select_one('.sc-8c396aa2-2.itZqyK').text.strip()
        except AttributeError:
            movie_year = "N/A"
        
        # Extract movie summary
        try:
            movie_summary = movie_soup.select_one('.sc-16ede01-2.gkNDIf').text.strip()
        except AttributeError:
            movie_summary = "N/A"
        
        print(f"Name: {movie_name}")
        print(f"Year: {movie_year}")
        print(f"Summary: {movie_summary}")
        print("--------------------")
