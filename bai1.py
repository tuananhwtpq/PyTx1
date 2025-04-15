
# khoi tao dict thu nhat
dict_sv = {}
n = int(input("Nhap so luong sinh vien: "))
for i in range(n):
    mssv = input("Nhap ma so sinh vien: ")
    so_tc = int(input("Nhap so tin chi da hoc: "))
    dict_sv[mssv] = so_tc

#khoi tao dict thu hai

dict_lhp = {
    "IT001": "Nhap mon lap trinh",
    "IT002": "Cau truc du lieu",
    "IT003": "Co so du lieu"
}

print("\nTu dien lop hoc phan")
for malop, tenlop in dict_lhp.items():
    print(f"{malop}: {tenlop}")

#Kiem tra sinh vien co ma 2024123456 hay khogn

mssv_can_ktra = "2024123456"
if mssv_can_ktra in dict_sv:
    print(f"\nSinh vien {mssv_can_ktra} co trong tu dien")
else:
    print(f"\nSinh vien {mssv_can_ktra} khong co trong tu dien")
    dict_sv[mssv_can_ktra] = int(input("Nhap so tin chi da hoc cho sinh vien moi: "))

#Sua tin chi cua sinh vien neu nho hon 100

if dict_sv[mssv_can_ktra] < 100:
    dict_sv[mssv_can_ktra] = 100
    print(f"Da cap nhat so tin chi sinh vien {mssv_can_ktra} thanh 100")

#Xoa sinh vien co so tin chi bang 0
dict_sv = {mssv: tc for mssv, tc in dict_sv.items() if tc != 0}

#chuyen du lieu sang 2 list

list_mssv = list(dict_sv.keys())
list_tc = list(dict_sv.values())

#in 3 phan tu dau cua list mssv
print("\n3 Phan tu dau tien cua list MSSV: ")
print(list_mssv[:3])

#in 3 phan tu cuoi cua list tc

print("\n3 phan tu cuoi cung cua list so tin chi: ")
print(list_tc[-3:])
    