import math
import random


# set p and # q

p = 97
q = 71
phi = (p-1) * (q-1)

list_of_possible_e = []

for e in range(2, phi) :
    if math.gcd( e, phi) == 1:
        # print(e)
        list_of_possible_e.append(e)

choice = random.randint(0,len(list_of_possible_e))
print(choice, len(list_of_possible_e))
e = list_of_possible_e[choice]
print('selected {0}'.format(e))

for d in range( 2, phi):
    if ( (e*d) % phi ) == 1 :
        print('found e {0}, d {1} for phi {2}'.format(e,d, phi))
