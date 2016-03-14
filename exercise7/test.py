#encodin:utf-8
# stence=raw_input('Stence:')
# screen_width=80
# text_width=len(stence)
# box_width=text_width+6
# left_margin=(screen_width-box_width)//2
# print
# print ' '*left_margin+ '+' + '-'*(text_width+2) + '+'
# print ' '*left_margin+'| '+' '*text_width    +' |'
# print ' '*left_margin+'| '+    stence       +' |'
# print ' '*left_margin+'| '+' '*text_width    +' |'
# print ' '*left_margin+ '+' + '-'*(text_width+2) + '+'
# print
"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""
class Bird(object):
    def __init__(self):
        self.hungry=True

    def eat(self):
        if self.hungry:
            print 'Aaaa'
            self.hungry=False
        else:
            print 'no thanks'

class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        super(SongBird,self).__init__()       #调用父类的eat方法
        self.sound='quak'
    def sing(self):
        print self.sound

sb=SongBird()
sb.sing()
sb.eat()
sb.eat()