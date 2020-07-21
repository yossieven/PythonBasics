import json
import difflib
from time import sleep

from ScreenCapture.capturerunner import ScreenCaptureRunner

data = json.load(open("data.json"))


def translate(word):
    return data.get(word)


def check_similarities(original, similar):
    if len(similar) > 0:
        print("Did you mean " + similar[0] + "? (Y/N)")
        decision = input()
        if decision.upper() == "N":
            original = input("Word doesn't exist. Enter word (to end type \\end): ")
        elif decision.upper() == "Y":
            original = similar[0]
        else:
            return original
    else:
        print("Word doesn't exist.")
        original = input("Enter word (to end type \\end): ")

    return original


def translate_word(word):
    if word is None:
        word = input("Enter word (to end type \\end): ")

    while True:
        translation = None;
        translation_cap = None;

        if word == "\\end":
            break;
        if word.strip() == "":
            word = input("enter a word (to end type \\end): ")
            continue

        if word.lower().strip() in data:
            translation = translate(word.lower().strip())
        elif word.lower().strip().title() in data:
            translation = translate(word.lower().strip().title())
        elif word.lower().strip().upper() in data:
            translation = translate(word.lower().strip().upper())

        if translation is None:
            similar = difflib.get_close_matches(word, data.keys())
            word = check_similarities(word, similar)
            continue;
        else:
            if translation is not None:
                [print(item) for item in translation]
            word = input("Enter word: ")
            continue


ScreenCaptureRunner.run('another test', filename='output.mp4', window='adobe')
sleep(10)
ScreenCaptureRunner.shutdown('another test')
translate_word(None)
