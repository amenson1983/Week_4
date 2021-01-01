my_file = open("Monthly_sales.csv",'r')

arr = []
for line in my_file.readline():
    string_get = line.split("\n")
    string_get = line.rstrip("")

    value = string_get.rstrip("\n")
    arr.append(value)
my_file.close()
print(arr)