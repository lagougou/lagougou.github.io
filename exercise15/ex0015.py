#encoding='utf-8'
"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中
"""
import json,xlwt,pickle
f=open('city.txt','r')
data=json.loads(f.read().decode('utf-8'))
xls=xlwt.Workbook()
sheet=xls.add_sheet('city',cell_overwrite_ok=True)

for i in range(len(data.keys())):
    col=0
    sheet.write(i,col,data.keys()[i])
    sheet.write(i,col+1,data[data.keys()[i]])
xls.save('city.xls')
