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

def get_separator(
  char='*',
  length=80,
):
  separator = ''
  for i in range(length): separator += char
  return separator

def __main__():
  [args, parser] = cli()
  print(args)
  cut_off = 61
  if args.verbose: cut_off = 0

  try:
    found_movies = netflix_data.search(args)
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
