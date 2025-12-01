import ham
print ("nhap n: ",end="")
n = ham.nhapn()
ham.tamgiac(n)
print("Nhap so de kiem tra")
So = ham.nhapn()
if ham.perf(So):
    print(f"So {So} la so hoan hao")
else:
    print(f"So {So} khong phai so hoan hao")
