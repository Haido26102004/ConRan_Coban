import func
while True:
    try:
        a = int(input("a la :"))
        b = int(input("b la :"))
        if a>0 and b>0:
            break
    except ValueError:
        print("Loi nhap sai kieu du lieu")
print(f"UCBC cua {a} va {b} la {func.ucbc(a,b)}")