i=0; k=0; line=""

for i in range(2,10):
    line = line + (" #  %d단  #"%i)

print(line)

for i in range(1,10):
    line=""
    for k in range(2,10):
        line=line+str("%2dX %2d= %2d"%(k,i,k*i))
    print(line)