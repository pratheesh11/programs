#pratheesh 

def printMaxSubSquare(N): 
    G = len(N) 
    C = len(n[0])
  
    R = [[0 for k in range(C)] for l in range(G)] 
 
  
    
    for i in range(1, G): 
        for j in range(1, C): 
            if (N[i][j] == 1): 
                R[i][j] = min(R[i][j-1], R[i-1][j], 
                            R[i-1][j-1]) + 1
            else: 
                R[i][j] = 0
      
   
    max_of_s = R[0][0] 
    max_i = 0
    max_j = 0
    for i in range(G): 
        for j in range(C): 
            if (max_of_s < R[i][j]): 
                max_of_s = R[i][j] 
                max_i = i 
                max_j = j 
  
    print("Maximum size sub-matrix is: ") 
    for i in range(max_i, max_i - max_of_s, -1): 
        for j in range(max_j, max_j - max_of_s, -1): 
            print (N[i][j], end = " ") 
print("") 
