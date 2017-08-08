import numpy as np


def stats(lst):
    lst1 = []#STORES VALUES IN lst THAT HAS THE MEAN SUBTRACTED THEN SQUARED
    s = sum(lst)#SUM
    l = len(lst)#LENGTH
    m = s/l#MEAN
    for i in lst:
        lst1.append((i - m)**2)
    sd_s = sum(lst1)
    sd = np.sqrt(sd_s / l)
    v = sd**2
    print ("""Mean:                             {0:<}
Standard Deviation: {1:<}
Variance:           {2:<}""".format(m,sd,v)
)
    
