import matplotlib.pyplot as plt

from Lesson_w04.__main1__ import get_list_from_file

sales_monthly = open("Monthly_sales.csv",'w')
sales_monthly.write('653421\n')
sales_monthly.write('738693\n')
sales_monthly.write('762122\n')
sales_monthly.write('396765\n')
sales_monthly.write('508288\n')
sales_monthly.write('595680\n')
sales_monthly.write('629934\n')
sales_monthly.write('671846\n')
sales_monthly.write('809779\n')
sales_monthly.write('783773\n')
sales_monthly.write('878155\n')
sales_monthly.write(input("Please point December`s final sales:")+'\n')


sales_monthly.close()
#in_file = open(r"Monthly_sales.csv",'r')
#line1 = in_file.readline()
#line2 = in_file.readline()
#line3 = in_file.readline()
#line4 = in_file.readline()
#line5 = in_file.readline()
#line6 = in_file.readline()
#line7 = in_file.readline()
#line8 = in_file.readline()
#line9 = in_file.readline()
#line10 = in_file.readline()
#line11 = in_file.readline()
#line12 = in_file.readline()
list1 = get_list_from_file("Monthly_sales.csv")
#line1 = int(line1.rstrip('\n'))
#line2 = int(line2.rstrip('\n'))
#line3 = int(line3.rstrip('\n'))
#line4 = int(line4.rstrip('\n'))
#line5 = int(line5.rstrip('\n'))
#line6 = int(line6.rstrip('\n'))
#line7 = int(line7.rstrip('\n'))
#line8 = int(line8.rstrip('\n'))
#line9 = int(line9.rstrip('\n'))
#line10 = int(line10.rstrip('\n'))
#line11 = int(line11.rstrip('\n'))
#line12 = int(line12.rstrip('\n'))
#list1 = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12]
#in_file.close()

x_coord = list(range(1,13,1))
y_coord = list1
plt.xlabel("Месяц")
plt.ylabel("Продажи в евро")
plt.grid(False)
plt.title("Продажи в евро по месяцам")

plt.xticks(x_coord,
           ["Январь",'Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'])
plt.plot(x_coord,y_coord,marker="s")
plt.show()

