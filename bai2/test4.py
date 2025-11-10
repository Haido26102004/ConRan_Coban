try:
    nam = int(input("Nhap nam"))
except:print("loi nhap lieu")
else:
  ducan = nam%10
  duchi =nam%12
  can =''
  chi=''
  match ducan:
     case 0:can="Canh"
     case 1:can ="Am"
     case 2:can ="Nham"
     case 3:can="Quy"
     case 4:can ="Giap"
     case 5:can ="At"
     case 6:can ="Binh"
     case 7:can ="Dinh"
     case 8:can ="Mau"
     case 9:can ="Ky"
  match duchi:
     case 0:chi="Ty"
     case 1:chi ="Suu"
     case 2:chi ="Dan"
     case 3:chi="Mao"
     case 4:chi ="Thin"
     case 5:chi ="Ty"
     case 6:chi ="Ngo"
     case 7:chi ="Mui"
     case 8:chi ="Than"
     case 9:chi ="Dau"
     case 9:chi ="Tuat"
     case 9:chi ="Hoi"
print (can,chi)