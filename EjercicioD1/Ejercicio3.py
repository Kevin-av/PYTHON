def counter(txt):
    word = txt.split()
    number = len(word)
    return number

txt = "Prueba de texto"
endWord = counter(txt)
print({endWord})