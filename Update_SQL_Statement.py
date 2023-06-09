import os
import sys
import re
import csv
from datetime import datetime
import pandas as pd
import numpy as np

class Insert_Table:
    def __init__(self, data_loc):
        """Initialize"""
        self.dloc = None
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
    
    def sql_insert(self):
        data_file = self.get_files(self.data_loc)
        sql_name = os.path.splitext(self.dloc)[0]
        f = open(sql_name + "_insert_statement.txt", "w+")
        field_name = ''
        for i in data_file.columns:
            field_name+=(i.upper() + ',')

        field_name = re.sub(',$', '', field_name)

        for i in range(len(data_file)):
            v = re.sub(']$', '', str(data_file.iloc[i].to_list()))
            f.write('INSERT INTO (' + field_name + ')' + '\n' +
                 'VALUES (' + v.replace('[', '', 1) + ')' +'\n\n')
