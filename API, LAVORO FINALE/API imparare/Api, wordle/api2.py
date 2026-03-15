import requests

base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_words(words):
  url = f"{base_url}/{words}"
  response = requests.get(url)
  print(response.status_code)
  
  if response.status_code == 200:
    pass
  else: 
    print("n")




word_of_the_day = "hello"
info_word = get_words(word_of_the_day)
