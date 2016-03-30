#encoding=utf-8
import xlrd,json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

workbook=xlrd.open_workbook("student.xls",'utf-8')
table=workbook.sheet_by_name(u"studet")

stu_info={}
info=[]

rows=table.nrows


for i in range(rows):
    stu = table.row_values(i)
    list = []
    for x in range(len(stu)-1):
        list.append(stu[x+1])
    stu_info[stu[0]] = list


s=json.dumps(stu_info,indent=4,ensure_ascii=False)
i=s.find(',')

f=open('student.xml','w')
f.write('<?xmlversion="1.0" encoding="UTF-8"?>\n'+
        '<root>\n'+
        '<students>\n'+
        '<!--\n'+
        '    学生信息表\n'+
        '    "id" : [名字, 数学, 语文, 英文]\n'+
        '-->\n'+
        s+
        '\n</students>\n</root>')

