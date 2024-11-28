print("Nguyễn Xuân Dịu")
print("235752021610078")
def count_file_contents(filename):
    try:
        with open(filename, 'r') as file:
           
            content = file.readlines()

            
            num_lines = len(content)

            
            num_words = 0
            num_characters = 0

            for line in content:
                
                num_characters += len(line)
                
                num_words += len(line.split())

            
            print(f"Số dòng: {num_lines}")
            print(f"Số từ: {num_words}")
            print(f"Số ký tự: {num_characters}")

    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    filename = input("Nhập tên file (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    count_file_contents(filename)

if __name__ == "__main__":
    main()
