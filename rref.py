import numpy as np
import matplotlib.pyplot as plt
import time

def rowoper(a1,a2,N):
    tel=np.array(a1)+np.array(a2)
    return np.array(tel)%(2*N)

def rrefring(a,N):
    n,m=np.shape(a)
    for i in range(n):
        if a[i,i]>N-1:
           pass
        else:
            j=i+1
            k=0
            while a[i,i]<N-1 and j<n:
                if a[j,i]>N-2 and k==0:
                 a[[i,j]]=a[[j,i]]
                 k+=1
                j+=1
 
        for j in range(i+1,n):
          if a[i,i]!=0 and a[j,i]>N-2:
            a[j]=(a[j]+a[i])%N
            print(222,j)
 
    return a            

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
             a[j]=(a[j]+a[i])%N
             a[j]=(a[j]+a[i])%N
           if a[j,i]==0:
               pass
            #print(222,j)
 
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
                
                #elif a[j,i]==1 and k==0:
                
 
        for j in range(i+1,n):
          if a[i,i]==3:  
           if a[j,i]==0:
               pass   
           if a[j,i]==1:
             a[j]=(a[j]+a[i])%N
           if  a[j,i]==2  :
             a[j]=(a[j]+a[i])%N
             a[j]=(a[j]+a[i])%N
           if  a[j,i]==3:
             a[j]=(a[j]+a[i])%N
             a[j]=(a[j]+a[i])%N
             a[j]=(a[j]+a[i])%N               
           
            #print(222,j)
 
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
                
                #elif a[j,i]==1 and k==0:
                
 
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
            # a[j]=(a[j]+a[i])%N
            # a[j]=(a[j]+a[i])%N
           if  a[j,i]==3:
               for _ in range(3):  
                  a[j]=(a[j]+a[i])%N                #a[j]=(a[j]+a[i])%N
             #a[j]=(a[j]+a[i])%N
             #a[j]=(a[j]+a[i])%N
           if  a[j,i]==4:
               for _ in range(4):  
                   a[j]=(a[j]+a[i])%N 
             #a[j]=(a[j]+a[i])%N
             #a[j]=(a[j]+a[i])%N
             #a[j]=(a[j]+a[i])%N               
             #a[j]=(a[j]+a[i])%N               
           
            #print(222,j)
 
    return a            
