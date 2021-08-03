import argparse
import netflix_data

def cli():
  parser = argparse.ArgumentParser(description='Netflix Movie Searcher')
  parser.add_argument('-t',
                      '--title',
                      help='Search movies by title',
                      required=False
                      )
  parser.add_argument('-y',
                      '--year',
                      help='Search movies by year',
                      required=False
                      )
  parser.add_argument('-d',
                      '--director',
                      help='Search movies by director',
                      required=False
                      )
  parser.add_argument('-c',
                      '--cast',
                      help='Search movies by cast',
                      required=False
                      )
  parser.add_argument('-dur',
                      '--duartion',
                      help='Search movies by duration',
                      required=False
                      )
  parser.add_argument('-desc',
                      '--description',
                      help='Search movies by description',
                      required=False
                      )
  parser.add_argument('-v',
                      '--verbose',
                      action="store_true",
                      help="Print the formula",
                      required=False
                      )
  args = parser.parse_args()
  return [args, parser]

def redefine_search_key(key):
  key = "release_year" if key == "year" else key
  return key

def search(args):
  movies = netflix_data.get_movies()
  filter_flag = False
  for search_key in vars(args):
    search_value = vars(args)[search_key]
    search_key = redefine_search_key(search_key)

    if not search_value: continue
    if search_key == "verbose": continue

    filter_flag = True

    movies = netflix_data.search_by_key(
      movies=movies,
      key=search_key,
      value=search_value,
      strict=False
    )

  if not filter_flag:
    raise Exception("ERROR: No search criteria specified")

  return movies

def get_separator(
  char='*',
  length=80,
):
  separator = ''
  for i in range(length): separator += char
  return separator

def __main__():
  [args, parser] = cli()

  cut_off = 61
  if args.verbose: cut_off = 0

  try:
    found_movies = search(args)
    for movie in found_movies:
      netflix_data.print_movie(
        movie=movie,
        cut_off=cut_off,
        show_id=False,
        type=False,
        country=False,
        date_added=False,
        rating=False,
        listed_in=False,
      )
      print(get_separator())
  except Exception as error:
    print(error)
    print(parser.print_help())

__main__()
