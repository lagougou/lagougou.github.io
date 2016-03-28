#encoding=utf-8
"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中：
"""
import json,xlwt
f=open('students.txt','r')
data=json.loads(f.read().decode('utf-8'))
xls=xlwt.Workbook()
sheet=xls.add_sheet('studet')
for i in range(len(data.keys())):
    row=i
    col=0
    sheet.write(row,col,data.keys()[i])
    for j in (data[data.keys()[i]]):
        col+=1
        sheet.write(row,col,j)

xls.save('student.xls')
