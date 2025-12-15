
def vonglap(s):
    lap =""
    for i in range(len(s)-1,-1,-1):
        lap += s[i]
    return lap
for i in range(4):
    for j in range (i,4):
        print(j,end=" ")
    print()