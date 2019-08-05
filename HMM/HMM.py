#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : HMM.py
# Create date : 2019-08-05 13:36
# Modified date : 2019-08-05 13:51
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from .subtask.cut import CUT
from .subtask.ner import NER
from .subtask.postag import POSTAG

class HMM:
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
