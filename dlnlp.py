#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : dlnlp.py
# Create date : 2019-08-04 23:28
# Modified date : 2019-08-05 14:02
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from CRF.CRF import CRF
from HMM.HMM import HMM
import re

class DLNLP:
    def __init__(self, algorithm = 'CRF'):
        self.algorithm = algorithm
        print(self.algorithm)

    def sentsplit(self, text):
        sents = re.split(r"([。!！?？])", text.strip())
        sents.append("")
        sents = [item for item in ["".join(i) for i in zip(sents[0::2], sents[1::2])] if len(item) > 0]
        return sents

    def ner(self, text):
        if self.algorithm == 'CRF':
            return CRF().ner(text)
        elif self.algorithm == 'HMM':
            return HMM().ner(text)

    def cut(self, text):
        if self.algorithm == 'CRF':
            return CRF().cut(text)
        elif self.algorithm == 'HMM':
            return HMM().cut(text)

    def postag(self, text):
        if self.algorithm == 'CRF':
            return CRF().postag(text)
        elif self.algorithm == 'HMM':
            return HMM().postag(text)

    def dep(self, word_list, pos_list):
        return CRF().dep(word_list, pos_list)
