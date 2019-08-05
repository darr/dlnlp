#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : cut.py
# Create date : 2019-08-05 14:59
# Modified date : 2019-08-05 15:00
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import os
import sklearn_crfsuite
from sklearn_crfsuite import metrics
from sklearn.externals import joblib
from .feature import feature_extract

class CUT:
    def __init__(self):
        self.model_path = '/'.join(os.path.abspath(__file__).split('/')[:-2]) + '/model/crf_cut_model.pkl'
        self.model = joblib.load(self.model_path)

    def label2word(self, labels, sent):
        '''将序列标记转换为标记结果'''
        labellist = []
        tmp = []
        for index in range(len(labels)):
            word = sent[index]
            tag = labels[index]
            if tag == 'S':
                if tmp:
                    labellist.append(tmp)
                tmp = [word]
                labellist.append(tmp)
                tmp = []
            elif tag == 'B':
                if tmp:
                    labellist.append(tmp)
                tmp = []
                tmp.append(word)
            elif tag == 'M':
                tmp.append(word)
            elif tag == 'E':
                tmp.append(word)
                labellist.append(tmp)
                tmp = []
        return [''.join(tmp) for tmp in labellist]

    def cut(self, sent):
        '''分词主函数'''
        sent_reps = feature_extract(sent)
        labels = self.model.predict(sent_reps)[0]
        return self.label2word(labels, sent)
