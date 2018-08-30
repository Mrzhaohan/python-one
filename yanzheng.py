#_/#_conding:utf8_/#_
import string
import random
keys = string.ascii_letters
yz=keys[random.randint(0,26)]+keys[random.randint(26,42)]\
+keys[random.randint(0,26)]+str(random.randint(0,10))
print(yz)
