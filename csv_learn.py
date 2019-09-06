# import numpy as np
# import csv

'''csv文件的写入'''
# output = '1.csv'
# with open('1.csv', 'w', newline='') as csvfile:
#     fieldnames = ['value1','value2','value3']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     a = [1, 2, 3]
#     b = [4, 5, 6]
#     writer = csv.writer(csvfile)
#     writer.writerow(a)
#     writer.writerow(b)
'''csv文件的读取'''
# output = '1.csv'
# with open(output,'r') as csvfile:
#     lines=csv.reader(csvfile) #可以先输出看一下该文件是什么样的类型
#     # 输出的只是一个文件对象，并不是我们需要打印的数字类型的，所以需要遍历这个文件，可以输出文件每一行的信息，也可以直接输出全部信息
#     print(lines)
#     content = []  # 用来存储整个文件的数据，存成一个列表，列表的每一个元素又是一个列表，表示的是文件的某一行
#     for line in lines:
#         print(line)
#         content.append(line)
#     print("该文件中保存的数据为:\n", content)

'''csv文件的追加写入数据'''
# import csv
# output = '1.csv'
# with open(output, 'a+', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     c=[7, 8, 9]
#     writer.writerow(c)











