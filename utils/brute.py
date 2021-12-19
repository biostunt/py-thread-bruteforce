import math

DEFAULT_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
DEFAULT_MIN_WORD_LENGTH = 0
DEFAULT_MAX_WORD_LENGTH = 5


class BruteDictionaryIterable:
  def __init__(self, alphabet: str = DEFAULT_ALPHABET,min_word_length: int = DEFAULT_MIN_WORD_LENGTH, max_word_length: int = DEFAULT_MAX_WORD_LENGTH) -> None:
      self.alphabet = list(set(alphabet));
      self.alphabet.sort()
      self.total_combinations = int(math.pow(len(self.alphabet), max_word_length))
      self.current_index = math.pow(len(self.alphabet), min_word_length) 
      print(f"[BRUTE_DICTIONARY_ITERABLE] Selected alphabet -> {''.join(self.alphabet)}; Max word length -> {max_word_length}; Total combinations -> {self.total_combinations}")
 
  def get_current_char(self, index):    
    return self.alphabet[index]

  def compile_word(self, indexes: list[int]):
    if len(indexes) < 1:
      return self.get_current_char(0)
    return "".join([self.get_current_char(index) for index in indexes])

  def split_on_chunks(self, chunks_count: int) -> list[list[int]]: 
    if(chunks_count == 1):
      return [[0, self.total_combinations]]
    chunk_size = int(self.total_combinations / chunks_count)
    chunks = []
    old_right_border = 0
    while(old_right_border + chunk_size < self.total_combinations):
      new_right_border = old_right_border + chunk_size - 1
      if(new_right_border > self.total_combinations):
        new_right_border = self.total_combinations
      chunks.append([old_right_border, new_right_border - 1])   
      old_right_border = new_right_border
    chunks[len(chunks) - 1][1] = self.total_combinations
    return chunks


  def generate_word(self, index: str) -> str:
    current = index
    indexes = []
    while(current >= 1):
      indexes.append(int(current % len(self.alphabet)))
      current = int(current / len(self.alphabet))
    word = self.compile_word(indexes)
    self.current_index = self.current_index + 1
    return word
