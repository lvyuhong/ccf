import numpy as np
import pandas as pd

def loadData(path):
    train = pd.read_csv(path+'first_round_training_data.csv')
    test = pd.read_csv(path+'first_round_testing_data.csv')
    #submit = pd.read_csv(path+'submit_example.csv')
    return train,test
    