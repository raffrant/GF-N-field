import numpy as np
import matplotlib.pyplot as plt
import time

def rrefring3(a,N):
    n,m=np.shape(a)
    for i in range(n):
        if a[i,i]==2:
           pass
        else:
            j=i+1
            k=0
            while a[i,i]<2 and j<n:
                if a[j,i]==2 and k==0:
                 a[[i,j]]=a[[j,i]]
                 k+=1
                j+=1
                
        for j in range(i+1,n):
          if a[i,i]==2:  
           if a[j,i]==1:
             a[j]=(a[j]+a[i])%N
           if  a[j,i]==2:
                for _ in range(2):  
                  a[j]=(a[j]+a[i])%N         
           if a[j,i]==0:
               pass
 
    return a   

def rrefring4(a):
    N=4
    n,m=np.shape(a)
    for i in range(n):
        if a[i,i]==3:
           pass
        else:
            j=i+1
            k=0
            while a[i,i]<3 and j<n:
                if a[j,i]==3 and k==0:
                 a[[i,j]]=a[[j,i]]
                 k+=1
                j+=1                
 
        for j in range(i+1,n):
          if a[i,i]==3:  
           if a[j,i]==0:
               pass   
           if a[j,i]==1:
             a[j]=(a[j]+a[i])%N
           if  a[j,i]==2  :
             for _ in range(2):  
                  a[j]=(a[j]+a[i])%N         
           if  a[j,i]==3:
             for _ in range(3):  
                  a[j]=(a[j]+a[i])%N         
 
    return a    


def rrefring5(a):
    N=5
    n,m=np.shape(a)
    for i in range(n):
        if a[i,i]==4:
           pass
        else:
            j=i+1
            k=0
            while a[i,i]<4 and j<n:
                if a[j,i]==4 and k==0:
                 a[[i,j]]=a[[j,i]]
                 k+=1
                j+=1                
 
        for j in range(i+1,n):
          if a[i,i]==4:  
           if a[j,i]==0:
               pass   
           if a[j,i]==1:
             for _ in range(1):  
               a[j]=(a[j]+a[i])%N 
           if  a[j,i]==2  :
             for _ in range(2):  
               a[j]=(a[j]+a[i])%N   

           if  a[j,i]==3:
               for _ in range(3):  
                  a[j]=(a[j]+a[i])%N                

           if  a[j,i]==4:
               for _ in range(4):  
                   a[j]=(a[j]+a[i])%N 
              
    return a            
