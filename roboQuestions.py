import random

def yes_or_no(question):
    while "only answer yes or no":
        reply = str(raw_input(question+' (y/n): ')).lower().strip()
        if (len(reply) > 0):
			if reply[0] == 'y':
				return True
			if reply[0] == 'n':
				return False

f = open("whatdaniellikes.txt", "r")
things=[]
ILikes=[]

nquestion=0
nyes=0

for x in f:
  likery=x.replace('\n','').split(',')
  things.append(likery[0])
  ILikes.append(likery[1])


outString="\nVery interesting. \n"

for i in range(0, random.randint(3,5)):

	thingIdx = random.randint(0,len(things)-1) 
	question = "Do you like " + things[thingIdx] + "?"
	nquestion = nquestion + 1

	if(yes_or_no(question)):
		outString = outString + "You like " + things[thingIdx]

		if(ILikes[thingIdx] == "yes"):
			nyes = nyes + 1
			outString = outString + " and I like " + things[thingIdx] + "\n"
		else:
			outString = outString + " but I don't like " + things[thingIdx] + "\n"

	else:
		outString = outString + "You don't like " + things[thingIdx]
		if(ILikes[thingIdx] == "yes"):
			outString = outString + " but I do like " + things[thingIdx] + "\n"
		else:
			nyes = nyes + 1
			outString = outString + " and I don't like " + things[thingIdx] + "\n"
        

print(outString)
print("We are " + str(nyes) + "/" + str(nquestion) + " the same")
