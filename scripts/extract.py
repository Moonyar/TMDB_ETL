import requests
from config.config import TMDB_API_KEY

# function to get movie data
def extract_movie_data():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# Testing the fucntion
if __name__ == "__main__":
    movies = extract_movie_data()
    print(movies[:5]) # print the first 5 movies to verify