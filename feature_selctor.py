import sklearn_relief as relief
import numpy as np
import pandas as pd
df = pd.read_csv("seta_icu4.csv")
from sklearn.impute import SimpleImputer
imp=SimpleImputer(missing_values=np.nan,strategy='mean')
imp=imp.fit(df)
df=imp.transform(df)
X = df[:,0:41]
Y = df[:,41]

# Load some data and put it in a numpy.array matrix
my_input_matrix = X

# Load the label vector
my_label_vector = Y

r = relief.Relief(
    n_features=5 # Choose the best 5 features
) # Will run by default on all processors concurrently

my_transformed_matrix = r.fit_transform(
    my_input_matrix,
    my_label_vector
)