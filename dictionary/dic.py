import json 
from difflib import get_close_matches

data=json.load(open("C:\python temelleri\Python\projects\dictionary\data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        yesno=input("Did you mean %s instead? Enter y if yes,or n if no: " % get_close_matches(w, data.keys())[0])
        if yesno=="Y" or "yes" or "Yes":
            return data[get_close_matches(w, data.keys())[0]]
        elif yesno=="N" or "no" or "No":
            return "The word doesnt matched.Please double check your input"
        else:
            return "we did not understand your input"
    else:
        return "The world does not exist.Please double check your input"
word=input("Enter your word:")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)