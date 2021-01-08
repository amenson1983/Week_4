
def get_sales_month():
    sales_file_monthly = open('Monthly_sales.csv', 'w')
    month_quantity = int(input('Put number of months to put the data'))
    for i in range(1, month_quantity + 1):
        int_input = int(input('Input sales for month #' + str(i) + ':'))
        sales_file_monthly.write(str(int_input) + '\n')
    sales_file_monthly.close()
    print('We are ready with data input')


if __name__ == '__main__':
    arr = []
    my_file = open('Monthly_sales.csv', 'r')
    fig = my_file.readline()
    while fig != '':
        fig = int(fig.rstrip('\n'))
        arr.append(fig)
        fig = my_file.readline()

    my_file.close()
    print(arr)
sum = 0
for i in range(1,len(arr)):
    sum+=arr[i]
print(sum)


