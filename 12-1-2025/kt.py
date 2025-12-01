import func
try:
    cd = int(input("chieu dai la :"))
    cr = int(input("chieu rong la :"))
except ValueError:print("Loi nhap sai kieu du lieu")
else:
    tuple = func.hcn(cd,cr)
    print (f"Dien tich hinh chu nhat la {tuple[0]} va Chu vi hinh chu nhat la {tuple[1]}")