print("Nguyễn Xuân Dịu")
print("235752021610078")
def write_list_to_file(filename, data_list):
    try:
        
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")  
        print(f"Nội dung đã được ghi vào tệp '{filename}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra khi ghi vào tệp: {e}")

def main():
    filename = input("Nhập tên tệp (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    
 
    data_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    
    write_list_to_file(filename, data_list)

if __name__ == "__main__":
    main()
