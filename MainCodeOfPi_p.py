#created by Mahgol Gholampour
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import measurements
import random


#li & lf are lengths that we want to find Pi in them.
li = 70
lf = 146
stepl = 25

#defining random colors for distinguishing lines
number_of_colors = 0
for l in range(li , lf ,stepl):
    number_of_colors = number_of_colors+1

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]

#To have a smoother diagram , N has to be large.
N = 500
parts = 200
Pis=[]
P_axis=[]

#P is a variable that accepts probabalities in a limited interval.It helps us to look at changes more accurately.
P = np.linspace(0.52, 0.65, num=parts)
for m, p in enumerate(P):
    P_axis.append(p)

for l in range(li , lf ,stepl):

    Pi = np.zeros(parts)
#Random lattice has to be defined N times.
    for n in range(N):
        randomLattice = np.random.random(size=(l, l))
        for m, p in enumerate(P):
            flag = False
            lattice = randomLattice < p

#Any site in each random lattice has a label.The lable depends on the neighbors of the home.For example, label 1 is related to first connected sites and connection here means to be the nearest neighbors.
            labels, num = measurements.label(lattice)
            list1 = np.array(labels[0])
            list2 = np.array(labels[l - 1])
   
            #we want to understand whether we have spanning cluster in this p(p_) or not .If we have spanning cluster, then Pi is 1 .
            for i in list1:
                if flag == False:
                    for j in list2:
                        if (i == j) and i > 0 and (flag == False):
                            Pi[m] = Pi[m] + 1
                            flag = True



    z = Pi / N
    Pis.append(z)


i=0
for Pi in Pis:
    plt.xlabel('p')
    plt.ylabel('Pi')
    plt.grid(True)
    plt.plot(P, Pi, color[i])
    i=i+1

plt.savefig('pi.png')
plt.show()
