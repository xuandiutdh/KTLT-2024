print("Nguyễn Xuân Dịu")
print("235752021610078")
def read_and_reverse_file(filename):
    try:
        
        with open(filename, 'r') as file:
            
            content = file.readlines()
        
        
        reversed_content = content[::-1]
        
        
        for line in reversed_content:
            print(line.strip())  

    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    filename = input("Nhập tên file (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    read_and_reverse_file(filename)

if __name__ == "__main__":
    main()
