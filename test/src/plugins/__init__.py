#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/12/30 21:18
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from config import *

if DEBUG:
    from . import mesh_mirror_inspection

    reload(mesh_mirror_inspection)
from . import mesh_mirror_inspection

plugins = [
    mesh_mirror_inspection,
]
