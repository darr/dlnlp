#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : ner.py
# Create date : 2019-08-05 13:37
# Modified date : 2019-08-05 13:46
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from .viterbi import vtb
import os

class NER:
    def __init__(self):
        self.current_path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
        trans_path = self.current_path + '/model/hmm_ner_trans.model'
        emit_path = self.current_path + '/model/hmm_ner_emit.model'
        start_path = self.current_path + '/model/hmm_ner_start.model'
        self.prob_trans = self.load_model(trans_path)
        self.prob_emit = self.load_model(emit_path)
        self.prob_start = self.load_model(start_path)

    def load_model(self, model_path):
        f = open(model_path, 'r')
        a = f.read()
        word_dict = eval(a)
        f.close()
        return word_dict

    #将序列标记转换为标记结果
    def label2word(self, labels, sent):
        per = []
        loc = []
        org = []
        tim = []
        tim_tmp = []
        loc_tmp = []
        per_tmp = []
        org_tmp = []
        ner_dict = {}
        for index in range(len(labels)):
            label = labels[index]
            word = sent[index]
            pair = [word, label]

            if label == 'ns-B':
                if loc_tmp and 'ns-E' in loc_tmp:
                    loc.append(loc_tmp)
                loc_tmp = []
                loc_tmp.extend(pair)

            elif label == 'ns-M':
                loc_tmp.extend(pair)
            elif label == 'ns-E':
                loc_tmp.extend(pair)
                if 'ns-B' in loc_tmp:
                    loc.append(loc_tmp)
                loc_tmp = []

            if label == 'nh-B':
                if per_tmp and 'nh-E' in per_tmp:
                    per.append(per_tmp)
                per_tmp = []
                per_tmp.extend(pair)
            elif label == 'nh-M':
                per_tmp.extend(pair)
            elif label == 'nh-E':
                per_tmp.extend(pair)
                if 'nh-B' in per_tmp:
                    per.append(per_tmp)
                per_tmp = []

            if label == 'ni-B':
                if org_tmp and 'ni-E' in org_tmp:
                    org.append(org_tmp)
                org_tmp = []
                org_tmp.extend(pair)
            elif label == 'ni-M':
                org_tmp.extend(pair)
            elif label == 'ni-E':
                org_tmp.extend(pair)
                if 'ni-B' in org_tmp:
                    org.append(org_tmp)
                org_tmp = []

            if label == 'nt-B':
                if tim_tmp and 'nt-E' in tim_tmp:
                    tim.append(tim_tmp)
                tim_tmp = []
                tim_tmp.extend(pair)
            elif label == 'nt-M':
                tim_tmp.extend(pair)
            elif label == 'nt-E':
                tim_tmp.extend(pair)
                if 'nt-B' in tim_tmp:
                    tim.append(tim_tmp)
                tim_tmp = []

        LOC = [''.join([loc_ for loc_ in [sub_item for sub_item in item if item.index(sub_item) % 2 == 0]]) for item in loc
               if item]
        PER = [''.join([per_ for per_ in [sub_item for sub_item in item if item.index(sub_item) % 2 == 0]]) for item in per
               if item]
        ORG = [''.join([org_ for org_ in [sub_item for sub_item in item if item.index(sub_item) % 2 == 0]]) for item in org
               if item]
        TIM = [''.join([org_ for org_ in [sub_item for sub_item in item if item.index(sub_item) % 2 == 0]]) for item in tim
               if item]

        ner_dict['LOC'] = list(set(LOC))
        ner_dict['ORG'] = list(set(ORG))
        ner_dict['PER'] = list(set(PER))
        ner_dict['TIM'] = list(set(TIM))
        return ner_dict


    def ner(self, sent):
        '''分词主控函数'''
        state_list = ['nh-B','nh-M','nh-E',
                     'ns-B','ns-M','ns-E',
                     'ni-B','ni-M','ni-E',
                     'O'] #状态序列
        ner_list = vtb(sent, state_list, self.prob_start, self.prob_trans, self.prob_emit)
        return self.label2word(ner_list, sent)
