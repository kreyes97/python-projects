import json
import difflib
from difflib import SequenceMatcher
import random
import time

idk = ["\nUh I didn't quite get that, sorry!\n", "\nUhh not sure what you mean by that\n", 
"\nHm. I'm not quite sure what you mean. Try again!\n", "\nA little confused here. Try again!\n"]

no = ["\nThat word is not in the dictionary. Check again!\n", "\nI'm not quite sure what that word is. Try again!\n", 
"You sure that's a word?\n", "\nRun that word by my again, will ya?\n"]

data = json.load(open("Dictionary+data+inside/data.json"))

def foo(word):
    if word in data:
        return [f"\n{word.capitalize()} means:\n"] + data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        yesno =  input(f"\nSorry! Did you mean {difflib.get_close_matches(word, data.keys())[0]}? Y for Yes and N for no.\n").lower()
        if yesno == "y":
            return data[difflib.get_close_matches(word, data.keys())[0]]
        elif yesno == "n":
            return no[random.randint(0, 3)]
        else:
            return idk[random.randint(0, 3)]
    else:
        return idk[random.randint(0, 3)]

sayso = input("Enter word here: \n").lower()
output = foo(sayso)
if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)

valid_answers = ["y", "n"]

idk2 = ["\nI'm not quite sure I got that. Let's try that again!", "\nI didn't quite get that. Let's try that again!", 
"\nA little confused here. Let me know what you want again."]

ok = ["\nAlright! Enter a word here again: \n", "\nOkay! Onto the next round. Enter a word here again: \n", 
"\nNice! Let's keep going, then. Enter a word here: \n"]

goodbye = ["\nThat was fun! I hope to see you soon. :)", "\nHopefully I was able to help. See you next time! :)", 
"\nGlad to be of service! :)"]

while True:
    cont = input("\nWould you like to continue? Enter Y for yes and N for no.\n").lower()
    if cont == "n":
        print(goodbye[random.randint(0, 2)])
        time.sleep(1.0)
        break
    elif cont not in valid_answers:
        print(idk2[random.randint(0, 2)])
        continue
    else:
        sayso = input(ok[random.randint(0, 2)]).lower()
        output = foo(sayso)
        if isinstance(output, list):
            for item in output:
                print(item)
        else:
            print(output)