#sentence = []
#while True:
#    word = input("enter a word. when done enter \"done\": ")
#    if (word == "\done"):
#        break;
#    if len(word.split(" ")) > 1:
#        print("please enter only a single word.")
#        continue
#    sentence.append(word)


def only_numbers(some_list):
    return [element for element in some_list if isinstance(element, int)]

def foo(numbers):
    return[i for i in numbers if i > 0]

#new_sentence = [word.capitalize() for word in sentence]
#print(" ".join(new_sentence))

#print(only_numbers(["yossi", "number", 11, 43, 76, "100", 101, 54]))
def upperCase(*args):
    myList = [element.upper() for element in args]
    myList.sort()
    return myList


print(upperCase("yossi", "bottle", "aaa"))





