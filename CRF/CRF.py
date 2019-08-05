#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : CRF.py
# Create date : 2019-08-05 13:30
# Modified date : 2019-08-05 13:53
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from .subtask.cut import CUT
from .subtask.ner import NER
from .subtask.postag import POSTAG
from .subtask.dep import DEP

class CRF:
    def __init__(self):
        pass

    def postag(self, word_list):
        postager = POSTAG()
        return postager.postag(word_list)

    def ner(self, sent):
        nerer = NER()
        return nerer.ner(sent)

    def cut(self, sent):
        cuter = CUT()
        return cuter.cut(sent)

    def dep(self, word_list, pos_list):
        deper = DEP()
        return deper.dep(word_list, pos_list)
