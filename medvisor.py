from tkinter import *
import pickle
from tkinter import ttk
import test
import get_features

class MyApp:

    def __init__(self, window):
        self.window = window
        self.window.geometry('600x500')
        self.window.title("Medvisor")
        Button(self.window, text = "Add Patient", command = self.add_patient).grid(row = 0, column = 0, sticky = 'news')
        Button(self.window, text = "Existing patient", command = self.existing_patient).grid(row = 0, column = 1, sticky = 'news')
        
        self.body = Frame(self.window)
        self.body.grid(row = 1, columnspan = 3)
        self.window.rowconfigure(0, weight = 1)
        self.window.rowconfigure(1, weight = 12)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

        
        try:
            with open('patient_data.pkl', 'rb') as f:
                self.patient_data = pickle.load(f)
        except:
            self.patient_data = {}

    
    def fetch(self, entries):
        recordID = int(entries[0][1].get())
        if recordID in self.patient_data:
            for widget in self.body.winfo_children():
                widget.destroy()
            Label(self.body, text = "Patient with given record ID already exists ").grid(row = 0, sticky = 'news', pady = 5)
            Button(self.body, text = "Try Again", command=self.add_patient).grid(row = 1, pady = 5)
            return

        self.patient_data[recordID] = {}

        for i in range(1, len(entries)):
            field = entries[i][0]
            try:
                value = float(entries[i][1].get())
            except:
                value = -1

            self.patient_data[recordID][field] = value

        with open('patient_data.pkl', 'wb') as f:
            pickle.dump(self.patient_data, f)

        for widget in self.body.winfo_children():
            widget.destroy()

        Label(self.body, text = "Patient details recorded successfully! ", font = ('Courier', 20)).grid(row = 0, sticky = 'news', pady = 5)
        Button(self.body, text = "Add more", command=self.add_patient).grid(row = 1, pady = 5)
        Label(self.body, text = "Most important parameters: ", font = ('Courier', 20)).grid(row = 2, sticky = 'news', pady = 5)
        features = get_features.get_features(self.patient_data[recordID]['ICUType'])
        #features = ['Albumin', 'Temp', 'Urine', 'HCT', 'NiMAP']
        for i in range(len(features)):
            Label(self.body, text = features[i], font = ('Courier', 30)).grid(row = i+3, sticky = 'news', pady = 5)
        
            
    def enter_more(self, recordID, entry, cb):
        p = cb.get()
        try:
            v = float(entry.get())
        except:
            v = -1
        if p in self.patient_data[recordID]:
            if self.patient_data[recordID][p] > v:
                self.patient_data[recordID][p] = v
        else:
            self.patient_data[recordID][p] = v

        cb.set('')
        entry.delete(0, END)

    def submit(self, recordID, entry, cb):
        self.enter_more(recordID, entry, cb)

        with open('patient_data.pkl', 'wb') as f:
            pickle.dump(self.patient_data, f)

        for widget in self.body.winfo_children():
            widget.destroy()
         
        prob = test.test(self.patient_data[recordID])[0][0] * 100   
        Label(self.body, text = "Probability of Survival:", font = ('Courier', 20)).grid(row = 0) 
        Label(self.body, text = str(prob) + "%", font = ('Courier', 40)).grid(row = 1)

    def validate_ID(self, entry):

        recordID = int(entry.get())
        for widget in self.body.winfo_children():
            widget.destroy()

        if recordID not in self.patient_data:
            
            Label(self.body, text = "Patient with given record ID doesn't exist ", font = ('Courier', 20)).grid(row = 0, sticky = 'news', pady = 5)
            Button(self.body, text = "Try Again", command=self.existing_patient).grid(row = 1, pady = 5)
            return

        else:

            fields = ["Weight","GCS","HR","NIDiasABP","NIMAP","NISysABP","RespRate","Temp","Urine","HCT","BUN","Creatinine","Glucose","HCO3","Mg","Platelets","K","Na","WBC","pH","PaCO2","PaO2","DiasABP","FiO2","MAP","MechVent","SysABP","SaO2","Albumin","ALP","ALT","AST","Bilirubin","Lactate","Cholestrol","Troponinl","TropininT"]
            cb = ttk.Combobox(self.body, values = fields)

            Label(self.body, text = "Enter parameter name: ").grid(row = 0, column = 0, sticky = 'news', pady = 5)
            cb.grid(row = 0, column = 1)
            Label(self.body, text = "Enter parameter value ").grid(row = 1, column = 0, sticky = 'news', pady = 5)
            ent = Entry(self.body)
            ent.grid(row = 1, column = 1, pady = 5)
            Button(self.body, text = "Enter more", command = (lambda: self.enter_more(recordID, ent, cb))).grid(row = 2, column = 0)
            Button(self.body, text = "Submit", command = (lambda: self.submit(recordID, ent, cb))).grid(row = 2, column = 1)
                
        

    def add_patient(self):

        for widget in self.body.winfo_children():
            widget.destroy()

        fields = ['RecordID', 'Age', 'Gender', 'Height', 'ICUType', 'Weight']
        entries = []
        for i in range(len(fields)):
            Label(self.body, text = "Enter " + fields[i] + ": ").grid(row = i, column = 0, sticky = 'news', pady = 5)
            ent = Entry(self.body)
            ent.grid(row = i, column = 1, pady = 5)
            entries.append((fields[i], ent))

        Button(self.body, text = "Submit", command=(lambda e=entries: self.fetch(e))).grid(row = 7, columnspan = 2, pady = 5)  

    def existing_patient(self):

        for widget in self.body.winfo_children():
            widget.destroy()

        Label(self.body, text = "Enter RecordID: ").grid(row = 0, column = 0, sticky = 'news', pady = 5)
        ent = Entry(self.body)
        ent.grid(row = 0, column = 1, pady = 5)
        Button(self.body, text = "Submit", command=(lambda: self.validate_ID(ent))).grid(row = 1, columnspan = 2, pady = 5)
    
window = Tk()
gui = MyApp(window)
window.mainloop()
