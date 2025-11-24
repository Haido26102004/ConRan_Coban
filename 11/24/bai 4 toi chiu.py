# i=1
# dem=0
# while(i<=10):
#     try:
#         n=int(input(f"nhap so thu {i} "))
#         i += 1
#         if(so<0):
# #             dem += 1
#     except ValueError:
#         print("Loi roi cu")
# print(f"Co {dem} so am ")
min =  1000
max = -1000
i = 1
while(i<= n):
    try:
        x = int(input(f"nhap so thu {i} "))
        i += 1
        if x <min:
            min = x
        if x > max:
            max = x
    except ValueError:
        print ("Loi kieu du lieu")
print("So nho nhat la {min}")
print ("So lon nhat {max}")