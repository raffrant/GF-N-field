def rrefbinary(a):
    n,m=np.shape(a)
    for i in range(n):
        if a[i,i]==1:
           pass
        else:
            j=i+1
            k=0
            while a[i,i]<1 and j<n:
                if a[j,i]==1 and k==0:
                 a[[i,j]]=a[[j,i]]
                 k+=1
                j+=1
        for j in range(i+1,n):
          if a[i,i]==1:  
           if a[j,i]==0:
               pass   
           if a[j,i]==1:
               a[j]=a[j]^a[i]
    
    for k in range(n-1,0,-1):
      for j in range(k):  
         if a[j,k]==1:
             a[j]=a[j]^a[k]
         else:
             pass      
    return a 
