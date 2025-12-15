def tinhtrungbinh(diem):
    tong = 0
    for value in diem:
        tong += value
        trungbinh = tong/(len(diem))
    return trungbinh
def toida(diem):
    max =diem[0]
    for value in diem:
        if value > max:
            max = value
    return max
def demdiem(diem):
    lon = 0
    nho = 0
    for value in diem:
        if value >= 8:
            lon += 1
        else:
            nho += 1
    return lon, nho
