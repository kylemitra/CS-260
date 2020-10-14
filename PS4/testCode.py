import numpy as num

def needleman(): #Initializing all the values and setting up the matrix
   s1 = "CACGTAT"
   s2 = "CGCA"
   N = len(s1)
   M = len(s2)
   gap = -1
   mismatch = -1
   match = 1
   matrix = num.zeros((m+1,n+1))
   #building an alignment matrix
   matrix[0][0] = 0
   for i in range(1,N):
       matrix[1][0] = matrix[i-1][0] + gap
   for j in range(1,M):
       matrix[0][j] = matrix[0][j-1] + gap
   for i in range(1,N):
       for j in range(1,M):
           if(s1[i-1] == s2[j-1]):
               score1 = matrix[i-1][j-1] + match
           else:
               score1 = matrix[i-1][j-1] + mismatch
           score2 = matrix[i][j-1] + gap
           score3 = matrix[i-1][j] + gap
           matrix[i,j] = max(score1,score2,score3)
   print(matrix)

#creating directional strings
def direction(matrix,N,M):
   dstring = buildDirectionalString(matrix,N,M)
   alignment(matrix,N,M,dstring)

#building alignments using directional string
def alignment(matrix,N,M):
   seq1pos = N-1
   seq2pos = M-1
   dirpos = 0
   top = " "
   bottom = " "
   while(dirpos < len(dstring)):
       if(dstring[dirpos] == 'D'):
           top+= s1[seq1pos]
           bottom+= s2[seq2pos]
           seq1pos-= 1
           seq2pos-=1
       elif(dstring[dirpos]=='V'):
           top+= s1[seq1pos]
           bottom+= "-"
           seq1pos-=1
       else:
           top+="-"
           bottom+= s2[seq2pos]
       dirpos+=1

#fucntion to create directional string
def buildDirectionalString(matrix,N,M):
   dstring = ""
   currentrow = N
   currentcol = M
   while(currentrow!=0 or currentcol!=0):
       if(currentrow==0):
           dstring+="H"
           currentcol+=-1
       elif(currentcol==0):
           dstring+="V"
           currentrow+=-1
       elif(matrix[currentrow][currentcol-1] + "-" ==matrix[currentrow][currentcol] ):
           dstring+="H"
           currentcol+=-1
       elif(matrix[currentrow-1][currentcol] + "-" == matrix[currentrow][currentcol]):
           dstring+="V"
           currentrow+=-1
       else:
           dstring+="D"
           currentrow+=-1
           currentcol+=-1
   print(dstring)
   return dstring

if __name__ == '__main__':
    needleman()