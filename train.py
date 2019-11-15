import pandas as pd
from torch import nn, optim
import torch.nn.functional as F
import torch.utils.data as data
import torch
import numpy as np
import io

from sklearn.model_selection import train_test_split

dataset = pd.read_csv('result_set-a.csv')
dataset=dataset.sample(frac=1)
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp = imp.fit(dataset)
dataset=imp.transform(dataset)
x=dataset[:,0:41]
y=dataset[:,41]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

from xgboost import XGBClassifier

classifier = XGBClassifier();
classifier.fit(x_train,y_train)

from sklearn.externals import joblib 
  
# Save the model as a pickle in a file 
joblib.dump(classifier, 'model.pkl') 

y_pred = classifier.predict(x_test)

errors = abs(y_pred - y_test)
sum=np.sum(errors)
print("Accuracy=",(1-sum/(errors.shape))*100)
