import pandas as pd
from Timeline import db
import timeit
import tracking_f as tr
import priority_calc as prio
import numpy as np


start = timeit.default_timer()

"""
    Read authentification details from auth.txt
"""
with open("../Data/auth.txt") as f:
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
    clear database
    CHECK: Performance impact too large? Maybe better to update DB?
           -> More coding effort
"""
UHDs = UHD.query.all()
for u in UHDs:
            db.session.delete(u)
db.session.commit()

"""
    load excel sheet into dataframe
    Future: Run SQL query via pandas
"""
df = pd.read_excel('../Data/Timeline_v27.xlsm', 'Data',
            skiprows=range(0,2),
            usecols=range(0,23),
            dtype={'UHD':str,'RMA':str})

"""
    remove duplicates
"""
df.drop_duplicates(subset='UHD', inplace=True)

"""
    initialise Priority Dataframe from excel file
"""
PrioDF = prio.initPrio()

"""
            loop over all datasets
"""
for i in range(0,len(df.UHD)):

            """  find status  """
            Status = prio.status_calc(df.loc[i,:])

            """  find LastStep and ShippingStatus """
            LastStep, ShippingStatus = calc_LastStep(df.loc[i,:], Status)

            """ get priority type from dataframe, e.g. POS2 """
            PriorityType = df.POS[i] + str(df.Priority[i])

            """ find Waiting time and check if step is overdue """
            waiting, overdue = prio.calc_waiting(PrioDf, PriorityType, Status, LastStep)

            """ write to database from dataframe """
            data = UHD(
                        DatumBeginn=df.DatumBeginn[i],
                        UHD=df.UHD[i],
                        POSSEN=df.POS[i],
                        Titel=df.Titel[i],
                        Bearbeiter=df.Bearbeiter[i],
                        Notizen=df.Notizen[i],
                        Customer=df.Customer[i],
                        CustNo=df.CustNo[i],
                        Priority=df.Priority[i],
                        SN=df.SN[i],
                        RMA=df.RMA[i],
                        RepAngebot=df.RepAngebot[i],
                        RepAuftr=df.RepAuftr[i],
                        DatumRetAngebot=df.DatumRetAngebot[i],
                        DatumAngekommen=df.DatumAngekommen[i],
                        DatumRepAngebot=df.DatumRepAngebot[i],
                        DatumRepAuftr=df.DatumRepAuftrag[i],
                        QS1=df.QS1[i],
                        QS2=df.QS2[i],
                        DateShipped=df.DateShipped[i],
                        Wiedervorlage=df.Wiedervorlage[i],
                        TrackingID=df.TrackingID[i],
                        ShippingStatus=df.ShippingStatus[i],
                        Status=Status,
                        Waiting=waiting,
                        LastStep=LastStep,
                        Overdue=overdue
                        )

            db.session.add(data)
            db.session.commit()


stop = timeit.default_timer()

print("Runtime: ", stop-start, "s")
