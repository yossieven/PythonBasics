def isQuestion(phrase):
    questionWords = ("who", "what", "how", "where", "when", "are", "is", "does", "have", "has")
    #words = input.split(" ")

    if phrase.startswith(questionWords):
        return True
    else:
        return False

def format_input(input):


        if isQuestion(input):
            input += "?"
        else:
            input += "."
        input_upper = input.capitalize()
        return input_upper




message = ""
finish = False
while(not finish):
    my_input = input("type: ")
    if my_input == "\end":
        finish = True
    else:
        message += " " + format_input(my_input)

print(message)

