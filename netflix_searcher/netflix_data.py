import csv

# Netflix csv file available at:
# https://github.com/andrsGutirrz/Python-Knowledge/blob/master/basics/netflix_titles.csv
CSV_FILEPATH = 'netflix.csv'

def read_csv(csv_filepath):
  rows = []
  with open(csv_filepath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      rows.append(row)
  return rows

def search_by_key(movies, key, value, strict=True):
  """Searches the movies list for a movie with the given key/value pair. The
  search is case-insensitive.

  Args:
      movies (list): A list containing dictionaries with the movies data.
      key (string): The key to search for.
      value (string): The value to search for.
      strict (bool, optional): If True, the search will only return a movie if
        the match is exact. If False, the search will return a movie if the
        match is partial. Defaults to True.

  Returns:
      list: A list of movies that match the given key/value criteria.
  """
  found_movies = []
  for movie in movies:
    if (strict and movie[key].upper() == value.upper()):
      found_movies.append(movie)
    elif (not strict and value.upper() in movie[key].upper()):
      found_movies.append(movie)
  return found_movies

def get_movies():
  return read_csv(CSV_FILEPATH)

def redefine_search_key(key):
  key = "release_year" if key == "year" else key
  return key

def search(args):
  movies = get_movies()
  filter_flag = False
  for search_key in vars(args):
    search_value = vars(args)[search_key]
    search_key = redefine_search_key(search_key)

    if not search_value: continue
    if search_key == "verbose": continue

    filter_flag = True

    movies = search_by_key(
      movies=movies,
      key=search_key,
      value=search_value,
      strict=False
    )

  if not filter_flag:
    raise Exception("ERROR: No search criteria specified")

  return movies

def print_movie(
  movie,
  cut_off=0,
  show_id=True,
  type=True,
  title=True,
  director=True,
  cast=True,
  country=True,
  date_added=True,
  release_year=True,
  rating=True,
  duration=True,
  listed_in=True,
  description=True,
):
  for key in movie:
    if not show_id and key == 'show_id': continue
    if not type and key == 'type': continue
    if not title and key == 'title': continue
    if not director and key == 'director': continue
    if not cast and key == 'cast': continue
    if not country and key == 'country': continue
    if not date_added and key == 'date_added': continue
    if not release_year and key == 'release_year': continue
    if not rating and key == 'rating': continue
    if not duration and key == 'duration': continue
    if not listed_in and key == 'listed_in': continue
    if not description and key == 'description': continue
    temp_cut_off = cut_off
    three_dots = ' '
    temp_cut_off = '' if temp_cut_off == 0 else temp_cut_off
    if temp_cut_off and len(movie[key]) > temp_cut_off:
      temp_cut_off = f'.{cut_off}'
      three_dots = '...'
    print(f"%-15s %-{temp_cut_off}s%s" % (key, movie[key], three_dots))
