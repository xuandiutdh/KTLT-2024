print("Nguyễn Xuân Dịu")
print("235752021610078")
def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            
            for i in range(n):
                line = file.readline()
                if not line:  
                    break
                print(line.strip())  
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{filename}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    filename = input("Nhập tên tệp (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    n = int(input("Nhập số dòng bạn muốn đọc: "))
    read_first_n_lines(filename, n)


if __name__ == "__main__":
    main()
