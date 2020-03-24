import random

thing=["fish", "boy", "tortoise", "balloon", "horse","girl"]
things=["combs", "sweets", "bananas", "trees", "hats", "maps"]
names=["Derek", "Flopsy", "Trevor", "Mike","Wendy", "Michelle"]
actions=["bought a", "bought some", "went to", "likes"]
places=["Gloucester", "Cheltenham", "Reigate"]

cont = ""
while (cont == ""):
    outputString = "A " + thing[random.randint(0,len(thing)-1)] + " called " + names[random.randint(0,len(names)-1)]

    action = actions[random.randint(0,len(actions)-1)]
    if(action == "went to"):
        outputString = outputString + " " + action + " " + places[random.randint(0,len(places)-1)]
    elif(action == "bought a"):
        outputString = outputString + " " + action + " " + thing[random.randint(0,len(thing)-1)]
    elif(action == "bought some"):
        outputString = outputString + " " + action + " " + things[random.randint(0,len(things)-1)]
    elif(action == "likes"):
        outputString = outputString + " " + action + " " + names[random.randint(0,len(names)-1)]
        
    print(outputString)
    cont=raw_input("")
    

