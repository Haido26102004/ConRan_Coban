tong = 0
while True:
    try:
        n = int(input("Nhap N: "))
        if(n>0):
            break
    except ValueError:
        print("Loi ")
print("=====Cau1=====")
for i in range(1,n+1):
        if(i %2 ==0):
            print(i,end=" ")

print("\n======Cau2======")
for i in range (1,n+1):
    if(i %2 != 0):    
        tong += i
print(f"tong cua cac so le {n} la : {tong}")

print("\n======Cau3======")
for i in range(1,n+1):
    if(i%3 ==0):
        print(f"\n Cac so chia het cho 3 la {i}")
print("\n======Cau4======")
for i in range(1,10):
    pass
print("\n======Cau5======")
so =int(input("nhap so cho bang cuu chuong"))
print(f"Bang cuu chuong cua {so}")  
for i in range(1,n+1):
    kq = so * i
    print(f"\n {so} x {i} = {kq}")
print("\n======Cau6======")
for i in range (1,n+1):
    if(i%5==0):
        continue
    print(i,end =" ")
print("\n======Cau7======")
for i in range (1,n+1):
    if(i < n):    
        tong += i
print(f"tong cua cac so le {n} la : {tong}")