alphabet = "abcdefghijklmnopqrstuvwxyz"
def vigenere_decode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0

  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  decoded_message = ""

  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index + offset_index) % 26]
      decoded_message += new_character
    else:
      decoded_message += message[i]
    
  return decoded_message

vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"
print(vigenere_decode(vigenere_message, vigenere_keyword))


def vigenere_encode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0

  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  encoded_message = ""

  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index - offset_index) % 26]
      encoded_message += new_character
    else:
      encoded_message += message[i]
    
  return encoded_message

vigenere_message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword_for_v = "besties"

print(vigenere_encode(vigenere_message_for_v, keyword_for_v))
print(vigenere_decode(vigenere_encode(vigenere_message_for_v, keyword_for_v), keyword_for_v))