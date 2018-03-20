import pandas as pd
import tracking_f as tr
from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

"""
    initialise dataframe with norm-days
    Stored in Excel file for easy editing!
"""
def initPrio():
            PrioDf = pd.read_excel('../Data/Prio.xlsx', 'Priorities',
                        userows=range(0,20),
                        usecols=range(0,10),
                        )
            return PrioDf

"""
    get status of UHD 
    To do: Check if None needs to be replaced by NaT
"""
def status_calc(df):
            if df.DateShipped != None:
                        Status = 8
            elif df.QS2 != None:
                        Status = 7
            elif df.QS1 != None:
                        Status = 6
            elif df.RepAuftr != None:
                        Status = 5
            elif df.RepAngebot != None:
                        Status = 4
            elif df.DatumAngekommen != None:
                        Status = 3
            elif df.DatumRepAngebot != None:
                        Status = 2
            else:
                        Status = 1

            return Status

""" get date of last completed step """
def calc_LastStep(df, Status):

            ShippingStatus = ''

            if Status == 1:
                        LastStep = df.DatumBeginn
            elif Status == 2:
                        LastStep = df.DatumRetAngebot
            elif Status == 3:
                        LastStep = df.DatumAngekommen
            elif Status == 4:
                        LastStep = df.RepAngebot
            elif Status == 5:
                        LastStep = df.RepAuftr
            elif Status == 6:
                        LastStep = df.QS1
            elif Status == 7:
                        LastStep = df.QS2
            elif Status == 8:
                        """ Status = 8 -> shipped.
                            find tracking status
                        """
                        if get_carrier(df.TrackingID[i]) == 'UPS':
                                    ShippingStatus, LastStep = tr.ups_track(df.TrackingID[i])
                        if get_carrier(df.TrackingID[i]) == 'FedEx':
                                    ShippingStatus, LastStep = tr.fedex_track(df.TrackingID[i])

            return LastStep, ShippingStatus

"""
    This function only calculates a day difference between time passed in each step and the norm-time for each step
    -> Priority function needs to be discussed!
"""
def calc_waiting(PrioDf, Priority, Status, LastStep):

            now = datetime.now()

            """ find the row in the Priority dataframe that matches our priority-type """
            Row = PrioDf.query(Priority)

            """ match  norm-days per step with the current step """
            for i in range(1,9):
                        if Status == i:
                                    NormDays = Row.loc[i]

            dt = NormDays - days_between(LastStep, now)

            """
                I added an overdue-flagm because I thought it might help with sorting.
                What we did before is calculate a percentage of "time-passed", so overdue orders had some not very intuitive high %-number.
                Now we can directly see how many days are left in the step, or how many days we are overdue.
            """
            if dt < 0:
                        overdue = True
            else:
                        overdue = False

            return abs(dt), overdue
