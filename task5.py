text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

word_list = []
word = ""
for char in text:
    if char.isalnum() or char == "'":
        word += char
    else:
        if word:
            word_list.append(word)
            word = ""
if word:
    word_list.append(word)

print(word_list)
