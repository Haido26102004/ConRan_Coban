import ham
chuoi = str(input("Nhap chuoi vao: "))
ho = "Do"
ten ="Hai"
print("Do dai",len(chuoi))
s1 = chuoi[9:10]
s2 =chuoi[0]
s3 = chuoi[17:18]
print(f"ky tu giua la {s1}")
print(f"ky tu dau tien la {s2}")
print(f"ky tu cuoi la {s3}")
# cau3
nuadau = chuoi [:3]
nuasau = chuoi [15:18]
print(nuadau)
print(nuasau)
# cau 4
print(chuoi.upper())
print(chuoi.lower())
# cau 5
print(f"{ho} {ten}")
c = ho +" " + ten
print(c)
# cau 6
print(chuoi.startswith("Python"))
# cau 7
chuoi1 = "23/7/2025"
print(chuoi1.replace("/","-"))
# cau 8
chuoi2 = "     Xoa khoang trong      "
print(chuoi2.strip())
# cau 9
chuoidau ="hello"
chuoisau = (chuoidau)
print(f"{ham.vonglap(chuoisau)}")