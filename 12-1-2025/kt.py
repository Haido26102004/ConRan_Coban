import func
while True:
    try:
        a = int(input("a la :"))
        b = int(input("b la :"))
        if a>0 and b>0:
            break
    except ValueError:
        print("Loi nhap sai kieu du lieu")
print(f"UCLN cua {a} va {b} la {func.ucln(a,b)}")
print(f"BCNN cua {a} va {b} la {func.bcnn(a,b)}")