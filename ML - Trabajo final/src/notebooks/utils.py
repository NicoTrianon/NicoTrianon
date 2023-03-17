import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
# import utils
from sklearn.preprocessing import LabelEncoder

## Modelos ##
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier

## Métricas ##
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix, multilabel_confusion_matrix, cohen_kappa_score
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV

#--------------------------------------------------------------------------------------------------------------

# Se crea una función para determinar eventuales errores en nuestro conjunto

def missing_zero_values_table(df):
        zero_val = (df == 0.00).astype(int).sum(axis=0)
        mis_val = df.isnull().sum()
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        mz_table = pd.concat([zero_val, mis_val, mis_val_percent], axis=1)
        mz_table = mz_table.rename(
        columns = {0 : 'Zero Values', 1 : 'Missing Values', 2 : '% of Total Values'})
        mz_table['Total Zero Missing Values'] = mz_table['Zero Values'] + mz_table['Missing Values']
        mz_table['% Total Zero Missing Values'] = 100 * mz_table['Total Zero Missing Values'] / len(df)
        mz_table['Data Type'] = df.dtypes
        mz_table = mz_table[
            mz_table.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(df.shape[0]) + " Rows.\n"      
            "There are " + str(mz_table.shape[0]) +
              " columns that have missing values.")
        return mz_table

#--------------------------------------------------------------------------------------------------------------

# Se crea una función para aplicar todos los modelos de clasificación al dataframe luego de realizado el 
# Feature engineer (con todos los valores que vienen por defecto). Asimismo, la función incluye la aplicación de
# las métricas, y la visualización de cada métrica y su modelo en un dataframe final, ordenado de mayor a menor
# en función del Accuracy Score

def regression(dataframe):
    
    tree = DecisionTreeClassifier()
    neighbors = KNeighborsClassifier()
    gaussian = GaussianNB()
    multinomial = MultinomialNB()
    bernoulli = BernoulliNB()
    forrest = RandomForestClassifier()
    lr = LogisticRegression()
    super = SVC()
    xgboost = XGBClassifier()
    
       
    algos = [tree, neighbors, gaussian, multinomial, bernoulli, forrest, lr, super]
    algos_names = ["DecisionTree","KNeighbors","GaussianNB","MultinomialNB","BernoulliNB","RandomForest","LogisticRegression","SuperVectorMachine","XGBoost"]
    
    
    accuracy = []
    recall = []
    precision = []
    f1 = []
    
    result = pd.DataFrame(columns = ["Accuracy Score", "Recall Score", "Precision Score", "f1_Score"], index=algos_names)
    
    X = dataframe.drop(columns="Adaptivity Level")
    y = dataframe["Adaptivity Level"]
    x_train, x_test, y_train, y_test=train_test_split(X,y,test_size=0.3,random_state=1234)

    for algo in algos:
        algo.fit(x_train, y_train)
        pred = algo.predict(x_test)
        accuracy.append(accuracy_score(y_test, pred))
        recall.append(recall_score(y_test, pred))
        precision.append(precision_score(y_test, pred))
        f1.append(f1_score(y_test, pred))
    
    le = LabelEncoder()
    y_train_xg = le.fit_transform(y_train)
    xgboost.fit(x_train, y_train_xg)
    pred_xg = xgboost.predict(x_test)
    accuracy.append(accuracy_score(y_test, pred_xg))
    recall.append(recall_score(y_test, pred_xg, average=None))
    precision.append(precision_score(y_test, pred_xg, average=None))
    f1.append(f1_score(y_test, pred_xg, average=None))
    
    
    result["Accuracy Score"] = accuracy
    result["Recall Score"] = recall
    result["Precision Score"] = precision
    result["f1_Score"] = f1
    
    return result.sort_values("Accuracy Score", ascending=False)

#--------------------------------------------------------------------------------------------------------------

# Idem función anterior pero para clasificadores multiclase; la única métrica válida es la matriz de confusión 
# y el cohen_kappa_score

def regression_multiclass(dataframe):
    
    tree = DecisionTreeClassifier()
    neighbors = KNeighborsClassifier()
    gaussian = GaussianNB()
    multinomial = MultinomialNB()
    bernoulli = BernoulliNB()
    forrest = RandomForestClassifier()
    lr = LogisticRegression()
    super = SVC()
    xgboost = XGBClassifier()
    
       
    algos = [tree, neighbors, gaussian, multinomial, bernoulli, forrest, lr, super]
    algos_names = ["DecisionTree","KNeighbors","GaussianNB","MultinomialNB","BernoulliNB","RandomForest","LogisticRegression","SuperVectorMachine","XGBoost"]

    
    X = dataframe.drop(columns="Adaptivity Level")
    y = dataframe["Adaptivity Level"]
    x_train, x_test, y_train, y_test=train_test_split(X,y,test_size=0.3,random_state=1234)

    for algo in algos:
        algo.fit(x_train, y_train)
        pred = algo.predict(x_test)
        print(algo)
        print(multilabel_confusion_matrix(y_test, pred))
        print(f"The Cohen Kappa Score is {cohen_kappa_score(y_test, pred)}")
        print("---------------------")
    
    le = LabelEncoder()
    y_train_xg = le.fit_transform(y_train)
    xgboost.fit(x_train, y_train_xg)
    pred_xg = xgboost.predict(x_test)
    print(algo)
    print(confusion_matrix(y_test, pred_xg))
    print("---------------------")

#--------------------------------------------------------------------------------------------------------------

# Función para sacar la métrica de confussion matrix para cada modelo

def metrics_confussion(dataframe):
    for algo in algos:
        X = dataframe.drop(columns="Adaptivity Level")
        y = dataframe["Adaptivity Level"]
        x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1234)
        print(algo)
        pred=algo.fit(x_train,y_train).predict(x_test)
        print(confusion_matrix(y_test, pred))
        print("---------------------")

#--------------------------------------------------------------------------------------------------------------

# Se crea una función para graficar cada una de las columnas relacionada con la variable target

def relation_target(dataframe):
  for col in dataframe.columns:
    plt.scatter(x=dataframe[col], 
                y=dataframe["Adaptivity Level"])
    plt.ylabel("Adaptivity Level")
    plt.xlabel(f'{col}')
    plt.show()