def nhapn():
    while True:
        try:
            n =int(input(""))
            if n>0:
                return n
            else:
                print("abc")
        except ValueError:
            print("loi du lieu")
def tamgiac(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f"*",end="")
        print()
def perf(n):
    tong = 0
    for i in range (1,n):
        if n%i == 0:
            tong += i
    if tong ==n:
        return True
    return False