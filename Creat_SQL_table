import os
import pandas as pd
import sys
import re
import csv

class Create_Table:
    def __init__(self):
        self.dloc = None
        self.dfile = None
        
    def get_fields(self, dloc):
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
            fields = dfile['Variable / Field Name']
            return fields
        
    def adjust_id_field(self, x):
        if x.lower() == 'studyid':
            return 'SYS_LOC_CODE'
        if x.lower() == 'study_id':
            return 'SYS_LOC_CODE'
        else:
            return x
        
    def genquery_table_dic(self, dloc):
        dfile = self.dfile
        dfile['Variable / Field Name'] = dfile['Variable / Field Name'].map(self.adjust_id_field)
        sql_name = os.path.splitext(self.dloc)[0]
        f = open("dt_" + sql_name + "_sql.txt", "w+")
        f.write("CREATE TABLE [dbo].[dt_" + sql_name + "](\n")
        f.write("	[FACILITY_ID] [int] NOT NULL,\n")
        # fields fulfill
        f_string = []
        output_list = []
        # -- facility Bio --
        if dfile['Facility Type'].unique() == 'Biological Data':
            p_keys = ['SYS_LOC_CODE', 'VISITID', 'CONC', 'ANALYTE']
            for i in range(len(dfile['Variable / Field Name'])):
                if dfile['Field Type'][i] == 'text'and dfile['Text Validation Type OR Show Slider Number'][i] != 'date_mdy':
                    if dfile['Required Field?'][i] == 'y':
                        f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[nvarchar](100)' + ' NOT NULL,'+"\n")
                    else:
                        f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[nvarchar](200)' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Field Type'][i] == 'text' and dfile['Text Validation Type OR Show Slider Number'][i] == 'date_mdy':
                    f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[date]' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Field Type'][i] == 'radio':
                    if dfile['Required Field?'][i] == 'y':
                        f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[int]' + ' NOT NULL,'+"\n")
                    else:
                        f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[int]' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Field Type'][i] == 'decimal':
                    if dfile['Required Field?'][i] == 'y':
                        f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[decimal](16, 8)' + ' NOT NULL,'+"\n")
                    else:
                        f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[decimal](16, 8)' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Field Type'][i] == 'notes':
                    f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[nvarchar](200)' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
            f_string[-1] = re.sub(',$', '', f_string[-1])
            for s in f_string:
                f.write(s)
        # -- facility Zika --
        if dfile['Facility Type'].unique() == 'Zika':
            p_keys = ['SYS_LOC_CODE']
            for i in range(len(dfile['Variable / Field Name'])):
                if dfile['Field Type'][i] == 'text'and dfile['Text Validation Type OR Show Slider Number'][i] == 'datetime_dmy':
                    f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[DATETIME]' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Field Type'][i] == 'text' and dfile['Text Validation Type OR Show Slider Number'][i] == 'date_mdy':
                    f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[date]' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Variable / Field Name'][i] == 'original_id' and dfile['Field Label'][i] == '1. Participant ID':
                    f_string.append('	[' + 'SYS_LOC_CODE' + ']' + ' ' + '[nvarchar](100)' + ' NOT NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Variable / Field Name'][i] == 'hurricane_id' and dfile['Field Label English'][i] == 'Hurricane ID':
                    f_string.append('	[' + 'SYS_LOC_CODE' + ']' + ' ' + '[nvarchar](100)' + ' NOT NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Field Type'][i] == 'radio':
                    f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[int]' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Field Type'][i] == 'text' and dfile['Text Validation Type OR Show Slider Number'][i] == 'integer':
                    f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[int]' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
                if dfile['Field Type'][i] == 'text' and dfile['Text Validation Type OR Show Slider Number'][i] == 'integer':
                    f_string.append('	[' + dfile['Variable / Field Name'][i].upper() + ']' + ' ' + '[int]' + ' NULL,'+"\n")
                    output_list.append(dfile['Variable / Field Name'][i] +' [Done]')
            f_string[-1] = re.sub(',$', '', f_string[-1])
            for s in f_string:
                f.write(s)
        
        f.write("PRIMARY KEY CLUSTERED\n")
        f.write("(\n")
        # primary key
        p_string = []
        for key in p_keys:
            p_string.append("\t[" + key + "] ASC,\n")
        p_string[-1] = re.sub(',$', '', p_string[-1])
        for s in p_string:
            f.write(s)
            
        f.write(")WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]\n")
        f.write(") ON [PRIMARY]")
        f.write("\n")
        f.write("GO\n")
        f.write("\n")
        f.write("SET ANSI_PADDING OFF\n")
        f.write("GO\n")
        
        # -- facility Zika ck--
        ck_string = []
        if dfile['Facility Type'].unique() == 'Zika':
            for i in range(len(dfile['Variable / Field Name'])):
                if dfile['Field Type'][i] == 'radio' and dfile['Field Label English'][i] is not None:
                    #ck_text = str(dfile['Field Label English'][i])
                    numbers = re.findall(r"\d+\.?\d*", str(dfile['Field Label English'][i]))
                    ck_n = ''
                    for n in numbers:
                        ck_n+=("[" + dfile['Variable / Field Name'][i] + "]=" + "(" + str(n) + ")" + " OR ")
                    ck_n = re.sub(' OR $', '', ck_n)
                    ck_string.append("ALTER TABLE [dbo].[dt_" + sql_name + "]  WITH CHECK ADD  CONSTRAINT [" + dfile['Variable / Field Name'][i] + "_CK] CHECK " + " ((" + ck_n + "))" +"\n" +"GO\n"+"\n")
                if dfile['Field Type'][i] == 'radio' and dfile['Choices, Calculations, OR Slider Labels'][i] is not None:
                    if dfile['Branching Logic (Show field only if...)'][i] is None:
                        ck_text = str(dfile['Choices, Calculations, OR Slider Labels'][i])
                        numbers = re.findall(r"\d+\.?\d*", ck_text)
                        ck_n = ''
                        label = ''.join(re.findall(r"[A-Za-z_]", str(dfile['Choices, Calculations, OR Slider Labels'][i])))
                        for n in numbers:
                            ck_n+=("[" + dfile['Variable / Field Name'][i] + "]=" + "(" + str(n) + ")" + " AND "+ label + " IS NOT NULL" + " OR ")
                        ck_n = re.sub(' OR $', '', ck_n)
                        ck_string.append("ALTER TABLE [dbo].[dt_" + sql_name + "]  WITH CHECK ADD  CONSTRAINT [" + dfile['Variable / Field Name'][i] + "_CK] CHECK " + " ((" + ck_n + "))" +"\n" +"GO\n"+"\n")
        for s in ck_string:
            f.write(s)
        return output_list, len(output_list)
