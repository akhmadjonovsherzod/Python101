#importing the whole module

import time

start = time.time()

print("Measuring the runtime")

stop = time.time()

measurement = stop - start

print(measurement)

#dont

# import time, random  #this is wrong, violates the PEP8 standard

#importing some specific methods from modules

from time import sleep

print(sleep(0.002))

#don't

# from time import * #this violates the namespaces

#importing with modul aliases

from datetime import time as d_t

print(d_t())

#absolute path

#from my_application1.service_module1 import method1

#relative path #if the module is in the same directory

#from .my_application1 import method1