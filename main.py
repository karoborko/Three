import PQ_list as l
import PQ_listwithnodes as lwn
import time as t
import random as rd
import matplotlib.pyplot as pl

# ***
# PRIORITY QUEUE HANDLING EFFICIENCY TEST:
# ***

# on the list:
PQ_l = l.PriorityQueue_List()
PQ_list_times = []
n_list = []

for i in range(10, 17):
    n = 2 ** i
    n_list.append(n)
    time_start = t.time()
    for j in range(n):
        PQkey = rd.randint(1, 150000)
        PQ_l.enqueue(PQkey)
    for j in range(n):
        PQ_l.dequeue_max()
    time_end = t.time()
    t_i = time_end - time_start
    PQ_list_times.append(t_i)

pl.figure(figsize=(8, 8))
pl.loglog(n_list, PQ_list_times, basex=2, basey=2, color='k')  # czarny


PQ_lwn = lwn.UnorderedList()
PQ_lwn_times = []
n_lwn = []

for i in range(10, 17):
    n = 2 ** i
    n_lwn.append(n)
    time_start = t.time()
    for j in range(n):
        PQkey = rd.randint(1, 150000)
        PQ_lwn.add(PQkey)
    for j in range(n):
        PQ_lwn.get_max()
    time_end = t.time()
    t_i = time_end - time_start
    PQ_lwn_times.append(t_i)

pl.loglog(n_lwn, PQ_lwn_times, basex=2, basey=2, color='g')  # zielony
pl.show()

# conclusion:
try:
    file = open("conclusion.txt", 'a')
except IOError:
    print("Error! File cannot be open!")
else:
    file.write(
        "The graph shows the creation and handling time for all elements (Y-axis) for a different number of data (X-axis) \n growing exponentially. The black curve shows the runtime for the priority queue \n on a regular list, the red curve shows the MAX pile, and the green curve shows the linkage list.")
finally:
    file.close()