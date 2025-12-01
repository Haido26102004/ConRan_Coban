import func
while True:
    try:
        a = int(input("a la :"))
        b = int(input("b la :"))
    except ValueError:
        print("Loi nhap sai kieu du lieu")
    else:
        print(f"UCBC cua {a} va {b} la {func.ucbc(a,b)}")