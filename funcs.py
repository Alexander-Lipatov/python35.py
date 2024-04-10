import contextlib

with contextlib.suppress(ImportError):
  from pyscript import window
  input = window.prompt
  print = window.alert


def upper_for_word(event):
    str = input('Input text: ')
    words = input('Input words: ')

    words = words.split()
    for word in words:
         str = str.replace(word, word.upper())
    print(str)