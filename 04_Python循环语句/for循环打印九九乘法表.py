for i in range(1,10):
    j=1
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end="")
        j+=1
    i+=1
    print()
