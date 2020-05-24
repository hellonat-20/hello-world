

import requests
words = requests.get('https://api.datamuse.com/words?rel_jjb=kicking')
print(words)

words_json = words.json()
print(words_json)

for w in words_json:
	print(w['word'])
