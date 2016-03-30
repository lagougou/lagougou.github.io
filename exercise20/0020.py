#encoding=utf-8
import xlrd,sys

reload(sys)
sys.setdefaultencoding('utf-8')

second=0
minite=0
hour=0

worksheep=xlrd.open_workbook('C:\\Users\\X250\\Desktop\\13918163358.xls','utf-8')
sheet=worksheep.sheet_by_index(0)
rows=sheet.nrows
for i in range(rows):
    if i>=6:
         hour=hour+int(sheet.cell_value(i,4)[:2])
         minite+=int(sheet.cell_value(i,4)[3:5])
         second+=int(sheet.cell_value(i,4)[6:])
 
minite+=(second%3600)/60
hour+=second/3600+minite/60
second=(second%3600)%60

print '%2d:%2d:%2d' %(hour,minite,second)