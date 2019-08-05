#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : postag.py
# Create date : 2019-08-05 15:05
# Modified date : 2019-08-05 15:07
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

class POSTAG:
    def __init__(self):
        self.model_path = '/'.join(os.path.abspath(__file__).split('/')[:-2]) + '/model/crf_pos_model.pkl'
        self.model = joblib.load(self.model_path)

    def postag(self, word_list):
        sent_reps = feature_extract(word_list)
        return self.model.predict(sent_reps)[0]
