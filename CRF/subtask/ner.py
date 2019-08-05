#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : ner.py
# Create date : 2019-08-05 15:04
# Modified date : 2019-08-05 15:08
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

class NER:
    def __init__(self):
        self.model_path = '/'.join(os.path.abspath(__file__).split('/')[:-2]) + '/model/crf_ner_model.pkl'
        self.model = joblib.load(self.model_path)

    def label2word(self, labels, sent):
        '''将序列标记转换为标记结果'''
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
        sent_reps = feature_extract(sent)
        labels = self.model.predict(sent_reps)[0]
        return self.label2word(labels, sent)
