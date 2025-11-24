i=1
dem=0
while(i<=10):
    try:
        so=int(input(f"nhap so thu {i} "))
        i += 1
        if(so<0):
            dem += 1
    except ValueError:
        print("Loi roi cu")
print(f"Co {dem} so am ")