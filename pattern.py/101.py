# 1
# 01
# 101 
# 01010

#  logic   i=1 then j=1 so j loop run only ones strats from zero i=1 ,j=0 1+0=1 

# i=2 j runs 2  times starts from 0,1  i=1 i=j 1+0=1,i=2 2+1=3 0,1
rows=5
for i in range(1,rows+1):
    for j in range(i):
        print((i+j)%2,end=" ")
    print()