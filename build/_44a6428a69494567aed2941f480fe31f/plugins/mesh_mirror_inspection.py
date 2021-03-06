
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/12/30 23:14\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
from _44a6428a69494567aed2941f480fe31f.CPMel_Form import build, item
from _44a6428a69494567aed2941f480fe31f.CPMel.cmds import *
from _44a6428a69494567aed2941f480fe31f.CPMel.api.OpenMaya import MGlobal
ui = ([item.Help, u'\u591a\u8fb9\u5f62\u6a21\u578b\u9876\u70b9\u955c\u50cf\u68c0\u67e5\u5de5\u5177'], [item.Label, u'\u8bef\u5dee:'], [item.FloatSlider, 0.001, 0.1, 0.001])

def meshMirrorCheck(_, __, mistake):
    meshs = selected()
    _meshs = list()
    for i in meshs:
        ss = listRelatives(i, s=True)
        if (ss is None):
            _meshs.append(i)
        else:
            for t in ss:
                _meshs.append(t)
    meshs = [i for i in _meshs if (i.type == u'mesh')]
    sel_vtx = list()
    for i in meshs:
        MGlobal.displayInfo((u'\u68c0\u67e5: %s' % i.fullPathName()))
        refresh()
        pts = i.getPoints(space=Space.world)
        reverse_pts = tuple((Double3(((i.x * (-1)), i.y, i.z)) for i in pts))
        sel_vtx.append([i.vtx[Id] for (Id, pt) in enumerate(pts) if (min((r_pt.dis(pt) for r_pt in reverse_pts)) > mistake)])
    select([t for i in sel_vtx for t in i])

def init():
    print u'mesh mirror inspection'

def doit():
    build(form=ui, func=meshMirrorCheck, title=name(), doit_text=u'\u9009\u62e9\u6a21\u578b\u6267\u884c')

def name():
    return u'\u6a21\u578b\u955c\u50cf\u68c0\u67e5\u5de5\u5177'
