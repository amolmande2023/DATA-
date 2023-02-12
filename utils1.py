import pickle
import json
import config
import numpy as np

class JobPlacement():
    def __init__(self, gender, ssc_percentage, ssc_board, hsc_percentage, hsc_board, hsc_subject, degree_percentage, undergrad_degree, work_experience, emp_test_percentage, specialisation, mba_percent):
        self.gender = gender
        self.ssc_percentage = ssc_percentage
        self.ssc_board = ssc_board
        self.hsc_percentage = hsc_percentage 
        self.hsc_board = hsc_board
        self.hsc_subject = hsc_subject
        self.degree_percentage = degree_percentage
        self.undergrad_degree = undergrad_degree
        self.work_experience = work_experience
        self.emp_test_percentage= emp_test_percentage
        self.specialisation = specialisation
        self.mba_percent = mba_percent
        return

    def __load_models(self):
        with open(r"artifacts/log_reg_model.pkl" ,'rb') as f:
            self.model= pickle.load(f)
            print('self.model >>',self.model)

        with open(r"artifacts/project_data1.json",'r') as f:
            self.project_data1 = json.load(f)
            print("Project Data is ",self.project_data1)
    
    def get_pridected_price(self):
        self.__load_models()
        test_array = np.zeros((1,self.model.n_features_in_))
        test_array[0][0] = self.project_data1['Gender'][self.gender]
        test_array[0][1] = self.ssc_percentage
        test_array[0][2] = self.project_data1['Ssc_board'][self.ssc_board]
        test_array[0][3] = self.hsc_percentage
        test_array[0][4] = self.project_data1['Hsc_board'][self.hsc_board]
        test_array[0][5] = self.degree_percentage
        test_array[0][6] = self.project_data1['Work_experience'][self.work_experience]
        test_array[0][7] = self.emp_test_percentage
        test_array[0][8] = self.project_data1['Specialisation'][self.specialisation]
        test_array[0][9] = self.mba_percent
        
        hsc_subject = 'hsc_subject_' + self.hsc_subject
        index = self.project_data1["Columns Name"].index(hsc_subject)
        undergrad_degree = 'undergrad_degree_' + self.undergrad_degree
        index = self.project_data1["Columns Name"].index(undergrad_degree)

        test_array[0][index] = 1

        print("test array is :",test_array)

        #test_array = self.model.transform(test_array)

        predicted_charges = self.model.predict(test_array)[0]
        print("Predicted Charges is :",predicted_charges)

        return predicted_charges