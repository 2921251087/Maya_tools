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
"""
from . import __OpenMayaAnim__ as omaim
from .__ALL import its, MItForIt


# MItKeyframe

class MItKeyframe(omaim.MItKeyframe):
    def __iter__(self):
        return MItForIt(self)


__all__ = ["MItKeyframe"]
