import pandas as pd
import numpy as np
import io
from sklearn.externals import joblib
from xgboost import XGBClassifier


def feat (dict):
  arr1=[64.248,0.561,88.919,2.76,74.153,8.223,68.488,39.827,59.043,90.392,12.02,35.026,24.189,28.629,21.923,1.184,108.588,21.848,1.788,179.384,3.759,136.92,10.362,7.37,34.572,92.288,39.874,0.44,57.941,1,78.181,94.828,2.915,98.295,120.289,143.787,1.691,1.702,156.38,5.584,0.814,0.139]
  list = ["Age","Gender","Height","ICUType","Weight","GCS","HR","NIDiasABP","NIMAP","NISysABP","RespRate","Temp","Urine","HCT","BUN","Creatinine","Glucose","HCO3","Mg","Platelets","K","Na","WBC","pH","PaCO2","PaO2","DiasABP","FiO2","MAP","MechVent","SysABP","SaO2","Albumin","ALP","ALT","AST","Bilirubin","Lactate","Cholestrol","Troponinl","TropininT"]
  arr= np.empty(41,dtype='float')
  for i in range(41):
    feature=list[i]
    if feature in dict:
      arr[i]=(dict[feature])
    else:
      arr[i]=arr1[i]
  return arr

def test (dict):
  x=feat(dict)
    
  classifier = joblib.load('model.pkl')  
  x=np.array(x).reshape((1,-1))
  y_pred = classifier.predict_proba(x)
  return y_pred
