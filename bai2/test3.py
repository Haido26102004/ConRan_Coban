try:
    thang = int(input("Nhap so thang"))
except:print("loi nhap lieu")
else:
    if thang in (1,3,5,7,9,11):
        print (f"Thang {thang} co 31 ngay")
    elif thang in (4,6,10,12):
        print (f"Thang {thang} co 30 ngay")
# Tinh nam nhuan
    elif thang == 2:
        nam = int(input("nhap nam"))
        if nam%4 ==0 and nam%100 != 0:
            print (f"Thang {thang} co 29 ngay ")
        else:
            print (f"Thang {thang} co 28 ngay")
    else:print("chi co 12 thang ")