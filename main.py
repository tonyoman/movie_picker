import requests
from bs4 import BeautifulSoup
import random


url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"


def main():
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    movie_containers = soup.select('td.titleColumn')
    href_movie_tags = soup.select("td.titleColumn a")
    rating_tags = soup.select("td.posterColumn span[name=ir]")

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-4]
        return year

    years = [get_year(tag) for tag in movie_containers]
    actors_list = [tag['title'] for tag in href_movie_tags]
    titles = [tag.text for tag in href_movie_tags]
    ratings = [float(tag['data-value']) for tag in rating_tags]

    number_of_movies = len(titles)
    while(True):
        index = random.randrange(0, number_of_movies)
        print(
            f"{titles[index]} {years[index]}, rating: {ratings[index]:.1f}, starring: {actors_list[index]}")

        user_input = input("Do you want another movie (y/[n])? ")
        if user_input != 'y':
            break


if __name__ == "__main__":
    main()


#

# actors = href_first_movie['title']
# title = href_first_movie.text
# print(title)
