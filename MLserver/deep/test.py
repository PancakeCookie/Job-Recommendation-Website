import pandas as pd
import numpy as np
from catboost import CatBoostClassifier

def jobRec(q_list):
    cat_clf = CatBoostClassifier()
    cat_clf.load_model("C:\\Users\\H\\ssac\\PycharmProjects\\MLserver\\deep\\test.obj")
    pred = cat_clf.predict_proba(q_list)
    job_li = []
    for i in zip(pred, cat_clf.classes_):
        job_li.append(i)
    job_li.sort(key= lambda x : x[0], reverse=True)
    # print(job_li[0][1], job_li[1][1], job_li[2][1])
    
    return (job_li[0][1], job_li[1][1], job_li[2][1])

q_list=[2,2,2,2,2]
jobRec(q_list)