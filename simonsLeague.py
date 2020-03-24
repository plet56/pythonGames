import random

f = open("teams.txt", "r")
teams=[]

for x in f:
  team=x.replace('\n','').split(',')
  teams.append(team[0])	

played=[False] * len(teams)
for i in range(0, len(teams)/2):
	t1 = random.randint(0,len(teams)-1)

	while(played[t1]):
		t1 = random.randint(0,len(teams)-1)
	played[t1] = True
	
	t2 = random.randint(0,len(teams)-1)
	while(played[t2]):
		t2 = random.randint(0,len(teams)-1)
	played[t2] = True
	
	raw_input(teams[t1] + " v " + teams[t2]) 
	print("\r" + teams[t1] + " " + str(random.randint(0,5)) + "   " + str(random.randint(0,5)) + " " + teams[t2] )
	print("")

