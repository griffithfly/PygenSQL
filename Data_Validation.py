import os
import sys
import re
import csv
from datetime import datetime
import pandas as pd
import numpy as np

class Check_Table:
    def __init__(self, dic_loc, data_loc):
        self.dloc = None
        self.dic_loc = dic_loc
        self.dic_file = None
        self.data_loc = data_loc
        self.data_file = None
    
    def get_files(self, dloc):
        if dloc is not None:
            self.dloc = dloc
            # if the dic file is csv file
            if os.path.splitext(self.dloc)[1] == '.csv':
                try:
                    dfile = pd.read_csv(self.dloc)
                except UnicodeDecodeError:
                    dfile = pd.read_csv(self.dloc, encoding = 'latin-1')
                self.dfile = dfile
            # if the dic file is excel file
            if os.path.splitext(self.dloc)[1] == '.xlsx':
                try:
                    dfile = pd.read_excel(self.dloc)
                except UnicodeDecodeError:
                    dfile = pd.read_excel(self.dloc, encoding = 'latin-1')
                self.dfile = dfile
            return dfile
        
    def check_fields(self):
        dic_file = self.get_files(self.dic_loc)
        data_file = self.get_files(self.data_loc)
        sql_name = os.path.splitext(self.dloc)[0]
        f = open(sql_name + "_report.txt", "w+")
        f.write("User: Griffith Gao " + "\n")
        f.write("Report Time: " + datetime.now().strftime("%B %d, %Y %H:%M:%S" + "\n"))
        f.write("\n")
        f.write("Data Dictionary File: '" + str(self.dic_loc) +"'\n")
        f.write("Data Export File: '" + str(self.data_loc) +"'\n")
        f.write("\n")
        f_string = []
        # Code 1000 - check length
        if len(dic_file['Variable / Field Name']) == len(data_file.columns):
            f_string.append('Length checking passed(Code 1000): the length of fields in the Data Dictionary equals to columns in the Data exports'+ "\n")
            print('Code 1000 - Passed')
            # Code 2000 - check squence of variables
            incon_list = []
            for i in range(len(dic_file)):
                if dic_file['Variable / Field Name'][i] != data_file.columns[i]:
                    incon_list.append('Inconsistent variable: ' + '[' + data_file.columns[i] + '].' + ' The right variable should be: ' + '['+ dic_file['Variable / Field Name'][i] + ']'+ "***")
            if len(incon_list) == 0:
                f_string.append('Sequence checking passed(Code 2000): the order of fields in the Data Dictionary equals to the Data exports')
                print('Code 2000 - Passed')
            if len(incon_list) > 0:
                f_string.append('Code 2000 ERRORS: ')
                f_string.append(str(incon_list))
                print('Code 2000 Errors - Please check the report')
        for s in f_string:
            f.write(s)
        m_f = []
        # Code 1001 - Missing Variable(s)
        if len(dic_file['Variable / Field Name']) != len(data_file.columns):
            #m_f = ['Please check Data Dictionary: ' + str(dic_loc)]
            for i in range(len(dic_file['Variable / Field Name'])):
                if str(dic_file['Variable / Field Name'][i]) not in list(data_file.columns):
                    m_f.append("Code 1001 Error(s): The variable [" + str(dic_file['Variable / Field Name'][i]) + "]" + " is missing")
                    print('Code 1001 Errors - Please check the report')
        for s in m_f:
            f.write(s)
        
        f.close
                
    def field_report(self):
        dic_file = self.get_files(self.dic_loc)
        data_file = self.get_files(self.data_loc)
        sql_name = os.path.splitext(self.dloc)[0]
        f = open(sql_name + "_report.txt", "a+")
        # Code 3000 - check range for each field
        for i in range(len(dic_file)):
            if dic_file['Choices, Calculations, OR Slider Labels'][i] is not np.NaN and dic_file['Field Type'][i] == 'radio':
                f_name = str(dic_file['Variable / Field Name'][i])
                f_name_int = re.findall(r"\d+\.?\d*", str(dic_file['Choices, Calculations, OR Slider Labels'][i]))
                f_name_int = [int(x) for x in f_name_int]
                for index in range(len(data_file[f_name])):
                    if data_file[f_name][index] not in f_name_int and np.isnan(data_file[f_name][index]) == False:
                        f.write('\nCode 3000 ERRORS: ' + 'Column (' + str(f_name) + ')' + 
                              ' ID: *' + str(data_file['hurricane_id'][index]) + '*' + 
                              ' Vaule is[' + str(int(data_file[f_name][index])) + '].' + 
                              ' The Integer should be: ' + str(f_name_int))
                        print('Code 3000 Errors - Please check the report') 
        f.close
        
    def logical_report(self):
        dic_file = self.get_files(self.dic_loc)
        data_file = self.get_files(self.data_loc)
        sql_name = os.path.splitext(self.dloc)[0]
        f = open(sql_name + "_report.txt", "a+")
        # Code 5000 - check logical for each field
        for i in range(len(dic_file)):
            if dic_file['Branching Logic (Show field only if...)'][i] is not np.NaN:
                label = ''.join(re.findall(r"[A-Za-z_]", dic_file['Branching Logic (Show field only if...)'][i]))
                num = re.findall(r"\d+\.?\d*", str(dic_file['Branching Logic (Show field only if...)'][i]))
                num_int = int([int(x) for x in num][0])
                char= re.findall(r"[+-=><]\D", dic_file['Branching Logic (Show field only if...)'][i])[0]
                for uid, vaule, real_l in zip(data_file['hurricane_id'], data_file[dic_file['Variable / Field Name'][i]], data_file[label]):
                    if str(real_l) != 'nan' and str(vaule) != 'nan':
                        if char == '< ':
                                if real_l <= num_int:
                                    pass
                        if char == '>=':
                                if real_l >= num_int:
                                    pass
                        if char == '= ':
                            if real_l != num_int:
                                # uid, vaule, logical_vaule, variable_name, logical_label_name, branch_detail
                                #print(uid, vaule, real_l, dic_file['Variable / Field Name'][i], label, dic_file['Branching Logic (Show field only if...)'][i])
                                f.write('\nhurricane_id = [' + str(uid) + ']' + 
                                      ' Variable Name = [' + str(dic_file['Variable / Field Name'][i]) + ']' + ' should not have vaule.' +
                                     ' Branching Logic is: "' + str(dic_file['Branching Logic (Show field only if...)'][i]) + '"' +
                                     ' Logical Variable Name[' + str(label) + ']' +
                                     ' is = [' + str(int(real_l)) + ']')
        f.close
            
                
