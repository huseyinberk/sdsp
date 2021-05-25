from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import numpy as np


import joblib

class HomeView(View):
    template = 'home.html'

    def get(self, request):
        df = joblib.load('static/selected_df.pkl')
        selected_cols = df.columns
        disease = joblib.load('static/disease.pkl').unique()[:3]
        dict = []
        numerics = df.select_dtypes('number').columns

        for sel in selected_cols:
            if sel not in numerics:
                values = df[sel].unique()
                dict.append([sel, values])
            else:
                dict.append([sel])

        context = {'sel': dict,
                   'dis': disease,
                   'predict': False}
        return render(request, self.template, context)

    def post(self, request):
        df = joblib.load('static/selected_df.pkl')
        model = joblib.load('static/model.pkl')
        disease = joblib.load('static/disease.pkl').unique()

        selected_cols = df.columns

        lst = []
        for sel in selected_cols:
            lst.append(request.POST.get(sel))

        varlst = []
        numerics = df.select_dtypes('number').columns
        for sel, var in zip(selected_cols, lst):

            if sel not in numerics:
                vars = sorted(df[sel].unique())
                index = vars.index(var)
                varlst.append(index)
            else:
                varlst.append(var)

        nplist = np.array(varlst).reshape(1, -1)

        result = model.predict_proba(nplist).tolist()[0]

        resultVars = []
        for disease, result in zip(disease, result):
            resultVars.append([disease, round(result*100, 0)])
        resultVars = sorted(resultVars, key=lambda l: l[1], reverse=True)[:3]


        dict = []
        numerics = df.select_dtypes('number').columns

        for sel in selected_cols:
            if sel not in numerics:
                values = df[sel].unique()
                dict.append([sel, values])
            else:
                dict.append([sel])

        context = {'sel': dict,
                   'dis': resultVars,
                   'predict': True}

        return render(request, self.template, context)


