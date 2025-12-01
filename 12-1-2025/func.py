
def hcn(cd,cr):
    S = (cd+cr)*2
    CV = cd*cr
    return S,CV

def ucln (a,b):
    if b == 0:
        return a
    while b!= 0:
        temp = b
        b =a%b
        a = temp
    return a
def bcnn(a, b):
    return (a * b)//ucln(a, b)