
def get_features(choice):
    if choice == 1:
        return ['ALT','Platelets','AST','Glucose','Urine']
    elif choice == 2:
        return ['Platelets','PaO2','Glucose','NISysABP','HR']
    elif choice == 3:
        return ['ALT','Platelets','Glucose',"Urine",'AST']
    elif choice == 4:
        return ['Platelets','Glucose','AST','PaO2','ALT']
    else:
        return ['INVALID INPUT OF ICU TYPE']


# In[ ]:




