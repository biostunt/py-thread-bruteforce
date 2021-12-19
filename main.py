from multiprocessing.managers import BaseManager
from arg_parser import create_parser
from utils.brute import BruteDictionaryIterable, BruteCompleteHashes
from utils.hash import create_hash, compare_hash
from multiprocessing import Process
import os
import time


def runnable(name: str, chunk: list[int, int], iterator: BruteDictionaryIterable, hashes: list[str]) -> None:
  print(f"[{name}]: Started")
  for i in range(chunk[0], chunk[1] + 1):
    current_word = iterator.generate_word(i)
    current_hash = create_hash(current_word)
    if compare_hash(current_hash, hashes):
      print(f"[{name}] Found: {current_word}; Hash: {current_hash}")
  print(f"[{name}]: finished")

def start_watching(threads_num: int, hashes: list[str]) -> None: 
  start_time = time.time()
  iterable = BruteDictionaryIterable()
  chunks = iterable.split_on_chunks(threads_num)
  if(threads_num > 1):
    threads: list[Process] = [Process(target=runnable,  args=(f"THREAD#{str(i + 1)}",chunks[i], iterable,  hashes)) for i in range(threads_num)]
    [thread.start() for thread in threads]
    [thread.join() for thread  in threads]
  else:
    runnable('THREAD#ALONE',chunks[0], BruteDictionaryIterable(), hashes)
  end_time = time.time()
  print(f"[PyThreadBruteforce] Elapsed {(end_time - start_time)} seconds")
  # print(f"[PyThreadBruteforce] Found {len(hash_manager.manager)} hashes")
    
   
def main() -> None: 
  parser = create_parser()
  args = parser.parse_args().__dict__
  threads_num = 1
  file = None
  hashes = None
  file = open('hashes.txt', 'r', encoding='utf-8')
  str = file.read()
  file.close()
  hashes = str.split('\n')
  # if args['file'] is not None:
  #   if os.path.isfile(args['file'][0]):
  #     file = open(args['file'][0], 'r', encoding='utf-8')
  #     str = file.read()
  #     file.close()
  #     hashes = str.split('\n')
  #   else:
  #     raise FileNotFoundError(f"File with path {args['file'][0]} did not found..")
  if args['hash'] is not None:
    hashes = args['hash']
  # if args['file'] is None and args['hash'] is None:
  #   raise ValueError('No file or hash provided. Run with -h to see documentation')
  if args['threads'] is None:
    print('[PyThreadBruteforce] The program will run in single thread mode')
  else:
    threads_num = int(args['threads'][0])
  print(f"[PyThreadBruteforce] Total hashes: {len(hashes)}")
  start_watching(threads_num, hashes)

if __name__ == "__main__":
  main()