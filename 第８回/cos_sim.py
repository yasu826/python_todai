import numpy as np
import math

def cos_sim(X,Y):
    x=np.array(X)
    y=np.array(Y)
    xi2=0
    yi2=0
    xiyi=0
    for n in range(len(x)):
        xi2+=x[n]**2
        yi2+=y[n]**2
        xiyi+=x[n]*y[n]      
    return xiyi/(math.sqrt(xi2*yi2))