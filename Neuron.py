import random as rd
import numpy as np

def train_func(I,W,T,epoch):
    beta=1
    alfa=0.1
    for e in range(epoch):
        f=rd.randrange(len(I[0]))
        dI=[x[f] for x in I]
        print('dI: ', dI)
        print('W: ', W)
        #dW=[x[f] for x in W]
        U=np.matmul(np.transpose(W),dI)
        print('U: ', U)
        y=1/(1+np.exp(-beta*U))
        D=[x-y for x in T]
        alfaI=[[x*alfa for x in y] for y in I]
        dW=np.matmul(alfaI,np.transpose(D))
        W=W+dW
    return W
    
def activate_funct(model,sample):
    return np.matmul(np.transpose(model),sample)

I=[[4, 2, -1], [0.01, -1, 3.5], [0.01, 2, 0.01], [-1, 2.5, -2], [-1.5, 2, 1.5]]
T=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
W=np.random.random_sample(size=(len(I), len(I[0])))*0.2-0.1

model=train_func(I,W,T,1)
sample=[[2], [0.01], [00.1], [-1], [-1.5]]


print(activate_funct(model,sample))
