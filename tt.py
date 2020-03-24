import sys

try:
    x=int(raw_input('Input number: '))
except ValueError:
    print "Not a number"
    sys.exit(1);

for y in range(1, 13):
    print(str(y) + " times " + str(x) +" = " + str(x*y))

# i = 13
# while (3 == 3):
#         print(str(i) + " times " + str(x) +" = " + str(x*i))
#         i += 1
