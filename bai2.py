def nhapDS():
    """Nhap danh sach mat hang tu ban phim """
    ds = []
    n = int(input("Nhap so luong mat hang: "))
    for i in range(n):
        print(f"\nNhap thong tin mat hang thu {i + 1}")
        ma = input("Ma hang: ")
        ten = input("Ten mat hang: ")
        so_luong = int(input("So luong: "))
        gia = int(input("Gia tien: "))
        tong = so_luong * gia
        ds.append({
            "ma": ma,
            "ten": ten,
            "so_luong": so_luong,
            "gia": gia,
            "tong_tien": tong
        })
    return ds

def hienThiDanhSach(ds):
    """Hien thi danh sach mat hang voi bang dinh dang"""
    print("\n{:<10} | {:<20} | {:<8} | {:<10} | {:<12}".format("Ma hang", "Ten hang", "So luong", "Gia", "Tong tien"))
    print("-" * 70)
    for mh in ds:
        print("{:<10} | {:<20} | {:<8} | {:<10} | {:<12}".format(
            mh["ma"], mh["ten"], mh["so_luong"], mh["gia"], mh["tong_tien"]
        ))

def timTongTienNhoNhat(ds):
    """Tim gia tri tong tien nho nhat"""
    return min(mh["tong_tien"] for mh in ds)

def hien_thi_mat_hang_tong_tien_min(ds):
    """Hien thi mat hang co tong tien nho nhat"""
    min_tien = timTongTienNhoNhat(ds)
    print(f"Mat hang co tong tien nho nhat ({min_tien:,} VND):")
    for mh in ds:
        if mh["tong_tien"] == min_tien:
            print("{:<10} | {:<20} | {:<8} | {:<10} | {:<12}".format(
            mh["ma"], mh["ten"], mh["so_luong"], mh["gia"], mh["tong_tien"]
        ))
            
def dem_mat_hang_theo_dieu_kien(ds):
    """Dem mat hang co so luong > 5 va tong tien < 1,000,000 """
    count = sum(1 for mh in ds if mh["so_luong"] > 5 and 
                mh["tong_tien"] < 1_000_000)
    print(f"\nSo luong mat hang co SL > 5 va tong tien < 1,000,000 VND: {count}")


#Main

def main():
    danh_sach = nhapDS()
    hienThiDanhSach(danh_sach)
    hien_thi_mat_hang_tong_tien_min(danh_sach)
    dem_mat_hang_theo_dieu_kien(danh_sach)

if __name__ == "__main__":
    main()