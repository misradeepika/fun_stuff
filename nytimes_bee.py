"""Solve the NYT bee!."""

DIC_PATH = '/usr/share/dict/words'

def test_word(letters, center, word):
   if center not in word:
       return False
   if len(word) < 4:
      return False
   letters_found = []
   for l in word:
      if l not in letters:
          return False
      letters_found.append(l)
   return set(letters_found).issubset(set(letters))

def search_words(letters, center):
        english_words = {}
        with open(DIC_PATH) as english_dict:
            for line in english_dict:
                english_words[line[:-1]] = ''
        results = []
        for word in english_words:
                if test_word(letters.lower(), test_center.lower(), word.lower()):
                        results.append(word)
        return results

test_letters = 'NJIEDTO'
test_center = 'O'

print(search_words(test_letters, test_center))
