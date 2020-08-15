"""
stratified k-fold cross-validation is a simple way to dividing data into a few parts and keeps the ratio of labels in each fold constant.   
We will train the model on some of these parts and test on the remaining parts. 
So stratified k-fold mean that we will divided data into k different sets which are exclusive
of each other and keeps the ratio of labels in each fold constant. 

This code assume that our dataset has a column called "target" and it is a classificiation problem.
"""

import pandas as pd 
from sklearn import model_selection


def Stratified_KFold(csv_input, csv_output)
    df = df.read_csv(csv_input)
    
    df['kfold'] = -1 
    
    df = df.sample(frac=1).reset_index(drop=True)
    
    y = df.target.values

    kf = model_selection.StratifiedKFold(n_splits=5)
    
    for f, (t_, v_) in enumerate(kf.split(X=df, y=y)):
        df.loc[v_, 'kfold'] = f
        
    df.to_csv(csv_output, index=False)

