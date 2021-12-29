import requests


class MovieSuggestions():
    url = 'https://tastedive.com/api/similar'
    d = {'type': 'movies'}
    lst = []

    def __init__(self, name):
        self.name = name

    def similar_movies(self, limit=5):
        self.d['q'] = self.name
        self.d['limit'] = limit
        movies_raw = requests.get(self.url, self.d)
        movies_json = movies_raw.json()
        print("Similar Movies like : {}".format(self.name))
        print()
        for movie in movies_json['Similar']['Results']:
            self.lst.append(movie['Name'])
        return self.lst

    @staticmethod
    def display_names(mov_lst):
        for mo in mov_lst:
            print("Movie - {}".format(mo))


mov = MovieSuggestions(input("Enter the name of the movie : "))
sim_mov = mov.similar_movies()
if len(sim_mov) < 1:
    print("Sorry we couldn't find any similar movie to {}".format(mov.name))
    print("Maybe the name was not spelled correctly or its not available with us.")
else:
    mov.display_names(sim_mov)
    print()
    ip = input("Do you want more suggestions ? (Y/N) : ")
    if ip.lower() == 'y':
        mov.similar_movies(10)
        mov.display_names(sim_mov)







