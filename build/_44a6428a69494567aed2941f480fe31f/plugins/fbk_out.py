
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/12/30 23:14\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
from _44a6428a69494567aed2941f480fe31f.CPMel_Form import build, item
from _44a6428a69494567aed2941f480fe31f.CPMel.cmds import *
ui = ((item.Is, u'Test1'),)

def FBKOut(self, is_ok):
    print is_ok

def init():
    print u'INIT FBKOUT'

def doit():
    build(u'TestApp', form=ui, func=FBKOut)

def name():
    return u'FBK\u5bfc\u51fa\u5de5\u5177'
