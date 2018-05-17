import pandas as pd
from sqlalchemy import create_engine
import timeit
import tracking_f as tr
import priority_calc as prio
import manipulate_df as m_df
import check_qs as c_qs
import config
import numpy as np


start = timeit.default_timer()

"""
    Read authentification details from auth.txt
"""
Auth_File = config.auth_file()
with open(Auth_File) as f:
    auth = f.readlines()

auth = [x.strip() for x in auth]
auth = [x.split('#', 1)[0] for x in auth]
auth = list(filter(None, auth))

"""
    FedEx credentials

    auth[0] = key
    auth[1] = account_number
    auth[2] = meter_no
    auth[3] = password


    UPS credentials

    auth[4] = license_number
    auth[5] = user_id
    auth[6] = password

"""

"""
    Run SQL query via pandas
"""
sql_string = config.sql_str_return()
engine = create_engine('mssql+pyodbc://@python')
con = engine.connect()
df = pd.read_sql(sql_string, con)


# Data_File = '/Users/Ludwig/Documents/Arbeit/Python/Data/Timeline_v27.xlsm'
#
# df = pd.read_excel(Data_File, 'Data',
#             skiprows=range(0,2),
#             usecols=range(0,23),
#             dtype={'UHD':str,'RMA':str})


# '''
#     Drop ShippingStatus to fix Type error
# '''
# df.drop(['ShippingStatus'], axis=1)

"""
    remove duplicates
"""
df.drop_duplicates(subset='UHD', inplace=True)


"""
    Check QS
"""
QS_POS = config.QS_POS_path()
df_QS_POS = pd.read_excel(QS_POS, "Quelle")

QS_SEN = config.QS_SEN_path()
df_QS_SEN = pd.read_excel(QS_SEN, "Vortest")


'''
    Add Columns
'''
df = m_df.add_columns(df)

"""
    initialise Priority Dataframe from excel file
"""
PrioDF = prio.initPrio()

"""
            loop over all datasets
"""
for i in range(0,len(df.UHD)):

            print("\n --- Row: ", i, " ---")

            if df.POS.iloc[i] == "POS":
                #print("POS")
                df.QS1.iloc[i], df.QS2.iloc[i] = c_qs.QS_POS(df.SN.iloc[i], df_QS_POS)
            elif df.POS.iloc[i] == "SEN" and df.SN.iloc[i] != None:
                #print("SEN")
                df.QS1.iloc[i], df.QS2.iloc[i] = c_qs.QS_SEN(df.SN.iloc[i], df_QS_SEN)
            else:
                print("MIC")
                #df.QS1.iloc[i], df.QS2.iloc[i] = pd.NaT, pd.NaT


            """  find status  """
            #print("Status")
            df.Status.iloc[i] = int(prio.status_calc(df.iloc[i]))

            """  find LastStep and ShippingStatus """
            #print("LastStep")
            df.LastStep.iloc[i], df.ShippingStatus.iloc[i] = prio.calc_LastStep(df.iloc[i], df.Status.iloc[i], auth)

            """ get priority type from dataframe, e.g. POS2 """
            #print("Prio")
            if int(df.Priority.iloc[i]) != 6 and int(df.Priority.iloc[i]) != '':
                df.PriorityType.iloc[i] = df.POS.iloc[i] + str(int(df.Priority.iloc[i]))
            else:
                df.PriorityType.iloc[i] = df.POS.iloc[i] + str(int(0))
            #print "POS/SEN: ", df.POS[i], " --- Priority: ", df.Priority[i]


            if not df.POS.iloc[i] == " ":
                #print("Waiting")
                """ find Waiting time and check if step is overdue """
                df.Waiting.iloc[i], df.Overdue.iloc[i] = prio.calc_waiting(PrioDF, df.PriorityType.iloc[i], df.Status.iloc[i], df.LastStep.iloc[i])

stop = timeit.default_timer()

print("Runtime: ", stop-start, "s")

#df = m_df.change_time(df)

start = timeit.default_timer()

df.to_csv('Database.csv', encoding='utf-8', date_format='%d.%m.%Y')

stop = timeit.default_timer()

print("Time to write csv: ", stop-start, "s")
