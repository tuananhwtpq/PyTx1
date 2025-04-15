# Nhập vào từ bàn phím một mảng a gồm n số nguyên

def NhapDS():

    n = int(input("Nhập số lượng phần tử trong mảng a: "))
    a = []
    for i in range(n):
        num = int(input("Nhập phần tử thứ {} : ".format(i+1)))
        a.append(num)

def SapXepTangDS():
    # Sắp a tăng dần và in ra màn hình
    a.sort()
    print("Mảng a sau khi sắp xếp tăng dần: ", a)

    index = -1
    for i, x in enumerate(a):
        if x % 2 == 0:
            index = i
        break

    print("Giá trị lớn nhất trong mảng a: ", max(a))
    print("Giá trị nhỏ nhất trong mảng a: ", min(a))
    print("Vị trí của phần tử chẵn đầu tiên trong mảng a: ", index if index != -1 else "Không có")
    print("Mảng a có chứa số 3: ", "Có" if 3 in a else "Không")


def ChenPtuVaoDS():
#Chen phan tu vao ds

    k = int(input("Nhập vị trí cần chèn: "))
    value = int(input("Nhập giá trị cần chèn: "))
    a.insert(k, value)
    a = [x for x in a if x % 2 != 0]

    print("Mảng a sau khi chèn và xóa các phần tử chẵn: ", a)

    #Tao ds b, nhan doi b, ghep voi a de tao moi danh sach

    m = int(input("Nhập số lượng phần tử trong mảng b: "))
    b = []
    for i in range(m):
        num = int(input("Nhập phần tử thứ {} : ".format(i+1)))
        b.append(num)

    b = b * 2
    b.reverse()
    c = a + b

    print("Mảng c sau khi ghép a và b: ", c)

#============Tuple=========

# Khởi tạo tuple

def KhoiTaoTuple():
    c = (3, 8, 5, 12, 7, 6, 14, 9, 2, 11)

    # In tuple và số phần tử
    print("Tuple c:", c)
    print("Số phần tử trong c:", len(c))

    # Đếm số phần tử chẵn
    so_chan = sum(1 for x in c if x % 2 == 0)
    print("Số phần tử chẵn trong c:", so_chan)

    # Nhập x và kiểm tra xem x có trong c không
    x = int(input("Nhập một số nguyên x: "))
    if x in c:
        print(f"{x} có xuất hiện trong tuple.")
    else:
        print(f"{x} không có trong tuple.")


#==============SET=================

 #Thêm một phần tử: add()
 #Thêm nhiều phần tử: update()
# Xóa một phần tử đang tồn tại: remove()
 #Xóa một phần tử nếu tồn tại: discard()
 #Xóa tất cả: clear()
 #Lấy ra một phần tử ngẫu nhiên: pop()

 # Các phép kiểm tra trên set
 # Kiểm tra xem hai tập hợp có rời nhau: isdisjoint()
# Kiểm tra xem một tập có là tập con của tập khác: issubset()
# Kiểm tra xem một tập có là tập mẹ của tập khác: issuperset()

# Khởi tạo một set với các giá trị hỗn hợp kiểu số và xâu ký tự

def USE_SET():  


    s = {1, "hai", 3.0, "bốn"}

    # Bổ sung một phần tử vào set
    s.add("năm")
    print("Sau khi thêm một phần tử: ", s)

    # Bổ sung hai phần tử vào set
    s.update([6, "bảy"])
    print("Sau khi thêm hai phần tử: ", s)

    # Xóa một phần tử trong set
    s.remove("hai")
    print("Sau khi xóa một phần tử: ", s)

    # Lấy ra một giá trị trong set
    value = s.pop()
    print("Lấy ra một giá trị ngẫu nhiên trong set: ", value)

    # Xóa toàn bộ set
    s.clear()
    print("Sau khi xóa toàn bộ set: ", s)


def Union_SET():
    # Khởi tạo hai set a và b
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    # In ra hợp, giao, hiệu của hai tập hợp
    print("Hợp của hai tập hợp: ", a.union(b))
    print("Giao của hai tập hợp: ", a.intersection(b))
    print("Hiệu của hai tập hợp: ", a.difference(b))

    # Kiểm tra xem tập a có là tập con của b không
    print("Tập a có là tập con của b không? ", a.issubset(b))

    # Kiểm tra xem tập a có chứa tập b không
    print("Tập a có chứa tập b không? ", a.issuperset(b))

    # Kiểm tra xem một giá trị nhập từ bàn phím có nằm trong set a hay set b không.
    value = int(input("Nhập một giá trị: "))
    print("Giá trị có nằm trong tập a không? ", value in a)
    print("Giá trị có nằm trong tập b không? ", value in b)

#==========Dictionary=========

def TaoDictTuChuoi():
    # keys for the dictionary
    alphabets = {'a', 'b', 'c'}

    # value for the dictionary
    number = 1

    # creates a dictionary with keys and values
    dictionary = dict.fromkeys(alphabets, number)

    print(dictionary)

# Output: {'a': 1, 'c': 1, 'b': 1}

    # set of vowels
    keys = {'a', 'e', 'i', 'o', 'u' }

    # list of number
    value = [1]

    vowels = dict.fromkeys(keys, value)
    print(vowels)

    # updates the list value
    value.append(2)

    print(vowels)

# Tra ve key hoac value

def TraVe():
    employee = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

    # extracts the keys of the dictionary
    dictionaryKeys = employee.keys()

    print(dictionaryKeys) # dict_keys(['name', 'age', 'salary'])

    marks = {'Physics':67, 'Maths':87}

    print(marks.values())

    # Output: dict_values([67, 87])

    marks = {'Physics':67, 'Maths':87}

    print(marks.items())


    marks = {'Physics':67, 'Maths':87, 'Aerobics':90,
    '': ''}
    #Kiem tra moi key deu True
    print(all(marks))
    #Ktra xem co key nao False
    print(any(marks))
    #Lay so phan tu
    print(len(marks))
    #Sap xep cac phan tu
    print(sorted(marks))

def BaiTapDict():

    students = {
    "2020601001": "Nguyễn Văn A",
    "2020601002": "Trần Thị B",
    "2020601003": "Lê Văn C",
    }

    print("Tất cả sinh viên:", students)
    # Kiểm tra xem sinh viên có mã “2020601001” có trong từ điển hay không
    sid = "2020601001"
    if sid in students:
        print(f"Sinh viên có mã {sid} là {students[sid]}")
    else:
        print(f"Không tìm thấy sinh viên có mã {sid}")
    # Sao chép các sinh viên có mã là số chẵn sang một từ điển mới
    students_even_id = {id: name for id, name in students.items() if int(id) % 2 == 0}
    print("Sinh viên có mã số chẵn:", students_even_id)


    # Tạo một từ điển chứa nội dung
    config = {
    "Date": "28-03-24",
    "Time": "09:24:05",
    "Server": "FIT-HaUI",
    "Name": "Root",
    "Pass": "*****"
    }

    # Bổ sung tham số: Status: Active
    config["Status"] = "Active"

    # Xóa thông tin về thời gian (Time)
    del config["Time"]

    # Sửa lại thông tin về Name = “Sa”
    config["Name"] = "Sa"

    # In từ điển ra màn hình
    print("Từ điển sau khi cập nhật:", config)

    # Kiểm tra xem trong từ điển có chứa thông tin về “Server” hay chưa
    if "Server" in config:
        print("Từ điển chứa thông tin về 'Server'")
    else:
        print("Từ điển không chứa thông tin về 'Server'")


#========Xau====

def KiemTraPhuHop():
# Tạo một ngăn xếp để theo dõi các dấu ngoặc
    stack = []
    # Duyệt qua từng ký tự trong biểu thức
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.remove(char)
        if not stack:
            return False
    stack.pop()
    # Nếu tất cả các dấu ngoặc đều đã được loại bỏ, biểu thức là hợp lệ
    return not stack

