def sort_words(s):
    words = s.split("-")
    words.sort()
    sorted_string = "-".join(words)
    print(sorted_string)

sort_words("green-red-yellow-black-white") # black-green-red-white-yellow
