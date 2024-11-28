print("Nguyễn Xuân Dịu")
print("23572021610078")
keys = ["name", "age", "city"]
values = [["Mây", "Dịu", "Happy"], [17, 19, 27], ["Hà Tĩnh", "Canada", "Japan"]]


dictionary = {}


for i in range(len(keys)):
    dictionary[keys[i]] = values[i]


print("Từ điển kết quả:")
print(dictionary)
