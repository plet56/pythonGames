import sys 
import time
import curses

def restart_line():
	sys.stdout.write('\r')
	sys.stdout.flush()
	
	
def main(win):
	win.nodelay(True)
	key=""
	trackLength=30
	distance=0
	win.clear()
	for i in range(distance, trackLength-1):
		win.addstr(" ")
	win.addstr("|#")

	while 1:
		try:
			key = win.getkey()
			win.clear()
			distance = distance + 1
			for i in range(0, distance):
				win.addstr("=")
			win.addstr("oo>")
			for i in range(distance, trackLength-1):
				win.addstr(" ")
			win.addstr("|#")
#			win.addstr(str(distance) + "/"+str(trackLength))
			if (distance >= trackLength):
				win.addstr("finished")
				break
		except Exception as e:
			pass
	win.clear()
	time.sleep(1)

print("On your marks...")
time.sleep(1)
print("Get set...")
time.sleep(1)
print("Go!!")
time.sleep(1)
startT = time.clock()
curses.wrapper(main)
print("your time: " + str(time.clock()-startT) + " seconds")
