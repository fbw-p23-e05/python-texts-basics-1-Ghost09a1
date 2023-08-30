text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

search_word = "capital"
if search_word in text:
    index = text.index(search_word)
    print(search_word + ":", index)
