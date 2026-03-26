text = input("Enter some kind of text: ")

print(text.upper())




text1 = input("Enter some kind of text: ")

print(text1.lower())
print(len(text1))




text2 = input("Enter some kind of text: ")
print(text2.capitalize())






text3 = input("Enter some kind of text: ")

symbol = text3.find("a")






textpy = input("Enter some kind of text: ").lower()
findpy = textpy.find("python")
print(findpy)





def text_sort(txt,symbol):
    return txt.count(symbol)





def text_upper_sort(txt):
    count = 0
    for i in txt:
        if i.isupper():
            count += 1
    return count






def find_text(txt,word):
    result = txt.find(word)
    if result >= 0:
        return True
    else:
        return False
print(find_text("Monkey Jungle Lukazavri","Lukazavri"))