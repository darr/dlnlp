#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : cut.py
# Create date : 2019-08-05 13:38
# Modified date : 2019-08-05 13:45
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from .viterbi import vtb
import os

class CUT:
    def __init__(self):
        self.current_path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
        trans_path = self.current_path + '/model/hmm_cut_trans.model'
        emit_path = self.current_path + '/model/hmm_cut_emit.model'
        start_path = self.current_path + '/model/hmm_cut_start.model'
        self.prob_trans = self.load_model(trans_path)
        self.prob_emit = self.load_model(emit_path)
        self.prob_start = self.load_model(start_path)

    def load_model(self, model_path):
        f = open(model_path, 'r')
        a = f.read()
        word_dict = eval(a)
        f.close()
        return word_dict

    def label2word(self, labels, sent):
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
        '''分词主控函数'''
        labels = vtb(sent, ('B', 'M', 'E', 'S'), self.prob_start, self.prob_trans, self.prob_emit)
        return self.label2word(labels, sent)
