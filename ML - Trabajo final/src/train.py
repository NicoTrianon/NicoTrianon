import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import joblib

## Modelo ##
from sklearn.tree import DecisionTreeClassifier, plot_tree

## Métricas ##
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV

data = pd.read_csv("C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//data//processed//data_df_num.csv")

data_df = pd.DataFrame(data)

X = data_df.drop(columns="Adaptivity Level")
y = data_df["Adaptivity Level"]
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1234)

tree = DecisionTreeClassifier()

dicc_hiperparametros_tree = {"max_depth":[4, 6, 8, None],
                        "splitter":["best", "random"],
                        "criterion":["gini", "entropy", "log_loss"],
                        "max_features":["auto", "sqrt", "log2", None], 
                        }

Ajuste_tree = GridSearchCV(estimator = tree,
            param_grid = dicc_hiperparametros_tree)

Ajuste_tree.fit(x_train,y_train)

with open("C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//model/my_model.pkl","wb") as f:
    joblib.dump(Ajuste_tree, f)