## Plot it ##
##A stupid program to display grades
##and take averages so I dont fuck my
##kids over too bad when I grade too harshly
#
#
# N. Wuerfel 2017 Umich goblu
#
# revised by mr manhimself 2018
# started git Feb1 2018 
# ~~~~AP~~~~

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

def plotIt(A): 
    # A is a vector of scores 

    #convert to percents
    B = [float(a)/32.0 for a in A]
    #plt.plot(A,range(len(A)))    
    plt.hist(B,8,normed=1) 

    # draw gaussian along with it
    mean = sum(B)/float(len(B))
    std = np.std(B)
    x = np.linspace(mean-3*std, mean+3*std, 100)
    plt.plot(x,mlab.normpdf(x,mean,std))
    plt.show()
    
