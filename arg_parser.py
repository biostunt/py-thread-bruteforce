from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
  parser = ArgumentParser(prog='PyThreadBruteforce',description='Decrypts hashed passwds')

  parser.add_argument('-f', '--file', 
    nargs=1,  
    metavar='<file_path>', 
    help='file if no hash provided'
  )

  parser.add_argument('--hash', 
    nargs='*',  
    metavar='<hash>',
    help='hash if no file provided' 
  )

  parser.add_argument('-t', '--threads',
    nargs=1,  
    metavar='<threads_count>', 
    help='Num of threads'
  )
  return parser