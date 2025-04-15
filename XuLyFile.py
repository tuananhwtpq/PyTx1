# r Mở file ở chế độ đọc (mặc định)
# w Mở file ở chế độ ghi
# x Mở file ở chế độ độc quyền, trả ra lỗi nếu file đã tồn tại
# a Mở file ở chế độ bổ sung (vào cuối file)
# t Mở file ở chế độ văn bản (mặc định)
# b Mở file ở chế độ nhị phân
# + Mở file ở cả chế độ đọc và ghi

# vd: f = open("test.txt")
#vd: f = open("test.txt", mode='r', encoding='utf-8')

def GhiFile():
    # open the file2.txt in write mode
    file2 = open('file2.txt', 'w', encoding='utf-8')

    # write contents to the file2.txt file
    file2.write('Tôi thích lập trình.\n')
    file2.write('Python là ngôn ngữ yêu thích của tôi\n')

#Nhap mang A va ghi vao file:

def NhapGhiMangA():
    n = int(input('Nhập n: '))

    f = open('B4.1a.txt', 'w')
    f.write(f'{n}\n')
    for i in range(n):
    f.write(input(f'Nhập a[{i}]: '))
    f.write(' ')
    f.close()

#Nhap ghi ma tran

def NhapMaTran():
    n = int(input('Nhập n: '))
    m = int(input('Nhập m: '))

    f = open('B4.1b.txt', 'w')
    f.write(f'{n} {m}\n')
    for i in range(n):
        for j in range(m):
            f.write(input(f'Nhập b[{i}][{j}]: '))
            f.write(' ')
    f.write('\n')
    f.close()

#Mo dong file voi with open

def MoDongWithOpen():
    with open("file1.txt", "r") as file1:
        read_content = file1.read()
        print(read_content)

#Tao ma tran va luu tru file. Doc dl tu tep len cac bien 

def TaoMaTran():
    n = int(input('Nhập n: '))
    m = int(input('Nhập m: '))

    with open('B4.2.txt', 'w') as f:
        f.write(f'{n} {m}\n')
        for i in range(n):
            for j in range(m):
                f.write(input(f'Nhập b[{i}][{j}]: '))
                f.write(' ')
            f.write('\n')

    with open('B4.2.txt', 'r') as f:
        n, m = (int(x) for x in f.readline().split())
        b = []
        for line in f.readlines():
            list_str = line.split()
            b.append([float(num) for num in list_str])
    print(n, m)
    print(b)

#Doc du lieu va luu vao bien tuong ung

def DocDLVaLuuBien():
    from pprint import pprint

    with open('Iris.txt', 'r') as f:
        n, m = (int(x) for x in f.readline().split())
        b = []
        for line in f.readlines():
            list_str = line.split()
            b.append([float(num) for num in list_str])
    print(n, m)
    pprint(b)

#Tao thu muc

def TaoThuMuc():
    import os
    import shutil

    # Tạo một thư mục trong ổ đĩa với tên bất kỳ
    folder_name = "my_folder"
    os.makedirs(folder_name, exist_ok=True)

    # Di chuyển file dữ liệu vào thư mục vừa tạo
    file_name = "Iris.txt"
    shutil.move(file_name, os.path.join(folder_name, file_name))

    # Hiển thị nội dung thư mục
    print("Nội dung thư mục:")
    for file in os.listdir(folder_name):
        print(file)

    # Đổi tên thư mục
    new_folder_name = "new_folder"
    os.rename(folder_name, new_folder_name)

    # Xóa file
    os.remove(os.path.join(new_folder_name, file_name))

    # Xóa thư mục
    os.rmdir(new_folder_name)

#Pandas

#Khoi tao Pandas

def KhoiTaoPandas():
    import pandas as pd

    grades = {"Semester1": 3.25,
    "Semester2": 3.28,
    "Semester3": 3.75}

    my_series = pd.Series(grades)

    print(my_series)

#Data Frame

def KhoiTaoDataFrame():
    import pandas as pd

    # create an empty DataFrame
    df = pd.DataFrame()

    print(df)

    data = {'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']}

    df = pd.DataFrame(data)

    print(df)

    #Khoi tao su dung danh sach
    data = [['John', 25, 'New York'],
    ['Alice', 30, 'London'],
    ['Bob', 35, 'Paris']]

    df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

    print(df)

#Khoi tao tu file csv

def KhoiTao():
    import pandas as pd

    # load data from a CSV file
    df = pd.read_csv('data.csv')

    print(df)

#Truy xuat du lieu

def TruyXuat():

    data = {'Name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David', 'Linda', 'Tom', 'Emily'],

    'Age': [25, 30, 35, 28, 32, 27, 40, 33, 29, 31],

    'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Toronto', 'Moscow']}

    df = pd.DataFrame(data)

    # display the first three rows
    print('First Three Rows:')
    print(df.head(3))
    print()

    # display the first five rows
    print('First Five Rows:')
    print(df.head())

    # display the last three rows
    print('Last Three Rows:')
    print(df.tail(3))
    print()

    # display the last five rows
    print('Last Five Rows:')
    print(df.tail())

#Bai tap dataframe

def BaiTap():
    # define a dictionary containing student data

    data = {'Name': ['John', 'Emma', 'Michael', 'Sophia'],
    'Height': [5.5, 6.0, 5.8, 5.3],
    'Qualification': ['BSc', 'BBA', 'MBA', 'BSc']}

    # convert the dictionary into a DataFrame
    df = pd.DataFrame(data)

    #Them cot moi
    # declare a new list
    address = ['New York', 'London', 'Sydney', 'Toronto']

    # assign the list as a column
    df['Address'] = address

    print(df)

    #Them hang moi
    print("Original DataFrame:")
    print(df)

    df.loc[len(df.index)] = ['Amy', 5.2, 'BIT']

    print("Modified DataFrame:")
    print(df)

def XoaHang_XoaCOT():
    #Xoa hang

        # delete row with index 4
    df.drop(4, axis=0, inplace=True)

    # delete row with index 5
    df.drop(index=5, inplace=True)

    # delete rows with index 1 and 3
    df.drop([1, 3], axis=0, inplace=True)

    #Xoa cot
    # delete age column
    df.drop('Age', axis=1, inplace=True)

    # delete marital status column
    df.drop(columns='Marital Status', inplace=True)

    # delete height and profession columns
    df.drop(['Height', 'Profession'], axis=1, inplace=True)

#Loc du lieu
def LocDL():
    # create a DataFrame
    data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
    }
    df = pd.DataFrame(data)

    # access the Name column
    print(df['Name'])

    # access multiple columns
    print(df[['Name','City']])

    #Su dung .loc

        # access a single row
    print("Single row:")
    print(df.loc[2])

    # access rows 0, 3 and 4
    print("List of Rows:")
    print(df.loc[[0, 3, 4]])

    # access a list of columns
    print("List of Columns:")
    print(df.loc[:,['Name', 'Age']])

    # access second row of 'Name' column
    print("Specific Value:")
    print(df.loc[1, 'Name'])

    #Su dung .iloc

        # access single row
    print("Single Row:")
    print(df.iloc[2])

    # access rows 0, 3 and 4
    print("List of Rows:")
    print(df.iloc[[0, 3, 4]])

    # access columns 0 and 2
    print("List of Columns:")
    print(df.iloc[:,[0,2]])

    # access a specific value
    print("Specific Value:")
    print(df.iloc[1, 0])

#BT su dung .loc va .iloc

def Loc_iLoc():
    import pandas as pd
    # Tạo DataFrame mẫu
    data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [22, 25, 30],
    'Language': ['Python', 'Java', 'C++']
    }

    df = pd.DataFrame(data)

        # 1. lấy thông tin của người có tên là 'Alice'.
    print(df.loc[df['Name'] == 'Alice'])

    # 2. lấy thông tin ở dòng thứ 3.
    print(df.iloc[2])

    # 3. lấy thông tin NNLT của sinh viên có tuổi từ 20 đến 25.
    print(df.loc[(df['Age'] >= 20) & (df['Age'] <= 25), 'Language'])

    # 4. lấy thông tin của 2 người đầu tiên.
    print(df.iloc[:2])

    # 5. sửa NNLT của người có tên là 'Bob' thành 'R'.
    df.loc[df['Name'] == 'Bob', 'Language'] = 8
    print(df)