print("Nguyễn Xuân Dịu")
print("235752021610078")
def append_text_to_file(filename, text):
    try:
        
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text + '\n') 
        print(f"Nội dung đã được nối vào tệp '{filename}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi nối văn bản vào tệp: {e}")

def display_file_content(filename):
    try:
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Nội dung của tệp:")
            print(content)
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{filename}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi đọc tệp: {e}")

def main():
    filename = input("Nhập tên tệp (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    text = input("Nhập văn bản bạn muốn nối vào tệp: ")
    
    
    append_text_to_file(filename, text)
    
    
    display_file_content(filename)


if __name__ == "__main__":
    main()
