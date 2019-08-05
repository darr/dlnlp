#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-04 23:28
# Modified date : 2019-08-05 14:01
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import dlnlp

def run_model(text, model_name):
    nlp = dlnlp.DLNLP(model_name)
    words = nlp.cut(text)
    print('words', words)
    postags = nlp.postag(words)
    print('postags', postags)
    ners = nlp.ner(text)
    print('ners', ners)
    deps = nlp.dep(words, postags)
    print('deps',deps)

def test():
    text = '土耳其称明年将对叙利亚库尔德武装发起新一轮军事行动'
    run_model(text, "CRF")
    run_model(text, "HMM")

test()

'''
CRF
words ['土耳其', '称明', '年', '将', '对', '叙利', '亚库尔德', '武装', '发起', '新', '一', '轮', '军事', '行动']
postags ['ns', 'm', 'nt', 'd', 'p', 'n', 'n', 'n', 'v', 'a', 'm', 'n', 'n', 'n']
ners {'ORG': [], 'TIM': ['明年'], 'LOC': ['土耳其', '叙利亚库尔德'], 'PER': []}
['ns', 'm', 'nt', 'd', 'p', 'n', 'n', 'n', 'v', 'a', 'm', 'n', 'n', 'n'] ['土耳其', '称明', '年', '将', '对', '叙利', '亚库尔德', '武装', '发起', '新', '一', '轮', '军事', '行动']
'''
