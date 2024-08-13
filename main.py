def main():
  with open('./books/frankenstein.txt') as f:
    file_contents = f.read()
    generate_report(file_contents)

def count_words(text):
  text_list = text.split() 
  word_count = 0
  for word in text_list:
    word_count += 1

  return word_count

def count_characters(text):
  lowered_text = text.lower()
  char_dict = {}
  for char in lowered_text:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1

  return char_dict 

def sort_on(dict):
    return dict["count"]

def generate_report(text):
  total_words = count_words(text)
  char_dict = count_characters(text)
  char_list = []
  
  for char in char_dict:
    if char.isalpha(): 
      char_list.append({
        'name': char,
        'count': char_dict[char] 
      })

  char_list.sort(reverse=True, key=sort_on)

  print('--- Begin report of books/frankenstein.txt ---')
  print(f'${total_words} words found in the document') 
  for char in char_list:
    print(f'The {char["name"]} character was found {char["count"]} times')
  
  print('--- End report ---')

main()