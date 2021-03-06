#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/5/18 23:57
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

* 本模块提供了对Maya Api数组的封装让其可以顺利的融入Python循环机制中
    >>> import CPMel.api as api
    >>> api.OpenMaya.MFloatArray(10, 0)
    <class 'CPMel.api.__OpenMaya_array__.MFloatArray'>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    >>> arr = api.OpenMaya.MFloatArray(10, 0)
    >>> [i for i in arr]
    [<CPMel.api.__OpenMaya_it__.MItDag; proxy of <Swig Object of type 'MItDag *' at 0x0000000016A16E10> >,...]

* 不仅如此还提供了迭代器的封装
    >>> from CPMel.api.OpenMaya import MItDag
    >>> itdg = MItDag()
    >>> [i for i in itdg] # 注意迭代器循环的 “i”是迭代器本身


"""
# 初始化MayaApi
import maya.OpenMaya
import maya.OpenMayaAnim
import maya.OpenMayaUI
import maya.OpenMayaFX
import maya.OpenMayaRender
import maya.OpenMayaMPx

del maya
from . import __OpenMaya__
from . import __OpenMaya__
from . import __OpenMayaAnim__
from . import __OpenMayaRender__
from . import __OpenMayaFX__
from . import __OpenMayaUI__
from . import __OpenMayaMPx__
from . import __OpenMaya_it__
from . import __OpenMayaAnim_it__
from . import __OpenMaya_array__
from . import __OpenMayaAnim_array__
from . import OpenMaya
from . import OpenMayaAnim
from . import OpenMayaFX
from . import OpenMayaRender
from . import OpenMayaUI
from . import OpenMayaMPx

