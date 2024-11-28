print("Nguyễn Xuân Dịu")
print("235752021610078")
def read_whole_file(filename):
    try:
       
        with open(filename, 'r', encoding='utf-8') as file:
            
            content = file.read()
            print("Nội dung của tệp:")
            print(content)
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{filename}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    filename = input("Nhập tên tệp (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    read_whole_file(filename)

if __name__ == "__main__":
    main()
