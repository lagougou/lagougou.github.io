#encoding=utf-8
"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
"""

import json,xlwt
f=open('numbers.txt')
data=json.loads(f.read().decode('utf-8'))
xls=xlwt.Workbook()
sheet=xls.add_sheet('numbers')
for i in range(len(data)):
    for j in range(len(data)):
        sheet.write(i,j,data[i][j])
xls.save('number.xls')