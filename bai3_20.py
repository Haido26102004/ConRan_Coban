try:
    van = float(input("Nhap diem van"))
    toan = float(input("Nhap diem toan"))
    anh = float(input("Nhap diem anh"))
except ValueError:
    print("Loi gia tri ")
else:
    if(van < 0 or van > 10 or toan < 0 or toan > 10 or anh < 0 or anh > 10 ):
        print ("nhap diem sai")
    else: 
        diemtb= (van + toan + anh)/3
        if (diemtb >= 9):
            print("Xuat sac")
        elif (diemtb >=8 ):
            print ("Gioi")
        elif (diemtb >=7 ):
            print ("Kha")
        elif (diemtb >=6 ):
            print ("Trung Binh")
        else :
            print ("Yeu")
