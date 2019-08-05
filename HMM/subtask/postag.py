#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : postag.py
# Create date : 2019-08-05 13:37
# Modified date : 2019-08-05 13:45
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from .viterbi import vtb
import os

class POSTAG:
    def __init__(self):
        self.current_path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
        trans_path = self.current_path + '/model/hmm_pos_trans.model'
        emit_path = self.current_path + '/model/hmm_pos_emit.model'
        start_path = self.current_path + '/model/hmm_pos_start.model'
        self.prob_trans = self.load_model(trans_path)
        self.prob_emit = self.load_model(emit_path)
        self.prob_start = self.load_model(start_path)

    def load_model(self, model_path):
        f = open(model_path, 'r')
        a = f.read()
        word_dict = eval(a)
        f.close()
        return word_dict

    def postag(self, word_list):
        '''分词主控函数'''
        state_list = ['n', 'nt', 'nd', 'nl', 'nh', 'nhf', 'ns', 'nhs',
                      'nn', 'ni', 'nz', 'v', 'vd', 'vl', 'vu',
                      'a', 'f', 'm', 'mq', 'q', 'd', 'r',
                      'p', 'c', 'u', 'e', 'o', 'i', 'j',
                      'h', 'k', 'g', 'x', 'w', 'ws', 'wu']  # 状态序列

        pos_list = vtb(word_list, state_list, self.prob_start, self.prob_trans, self.prob_emit)
        return pos_list
