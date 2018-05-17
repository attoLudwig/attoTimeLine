import pandas as pd
import tracking_f as tr
import config
from datetime import datetime
import numpy as np

def days_between(d1, d2):
    #d1 = datetime.strptime(d1, "%Y-%m-%d")
    #d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

"""
    initialise dataframe with norm-days
    Stored in Excel file for easy editing!
"""
def initPrio():
            Prio_Data = config.prio_excel_path()
            PrioDf = pd.read_excel(Prio_Data, 'Priorities',
                        userows=range(0,20),
                        usecols=range(0,10),
                        )
            return PrioDf

"""
    get status of UHD
    To do: Check if None needs to be replaced by NaT
"""
def status_calc(df):
            #print pd.isnull(df.DateShipped)

            if not pd.isnull(df.DateShipped):
                        Status = 8
            elif not pd.isnull(df.QS2):
                        Status = 7
            elif not pd.isnull(df.QS1):
                        Status = 6
            elif not pd.isnull(df.DatumRepAuftrag):
                        Status = 5
            elif not pd.isnull(df.DatumRepAngebot):
                        Status = 4
            elif not pd.isnull(df.DatumAngekommen):
                        Status = 3
            elif not pd.isnull(df.DatumRetAngebot):
                        Status = 2
            else:
                        Status = 1

            return Status

""" get date of last completed step """
def calc_LastStep(df, Status, auth):

            ShippingStatus = ''

            if Status == 1:
                        LastStep = df.DatumBeginn
            elif Status == 2:
                        LastStep = df.DatumRetAngebot
            elif Status == 3:
                        LastStep = df.DatumAngekommen
            elif Status == 4:
                        LastStep = df.DatumRepAngebot
            elif Status == 5:
                        LastStep = df.DatumRepAuftrag
            elif Status == 6:
                        LastStep = df.QS1
            elif Status == 7:
                        LastStep = df.QS2
            elif Status == 8:
                        """ Status = 8 -> shipped.
                            find tracking status
                        """
                        #print "TrackingID: ", pd.isnull(df.TrackingID)
                        if not pd.isnull(df.TrackingID):
                                    if tr.get_carrier(df.TrackingID) == 'UPS':
                                                ShippingStatus, LastStep = tr.ups_track(df.TrackingID, auth)
                                    if tr.get_carrier(df.TrackingID) == 'FedEx':
                                                ShippingStatus, LastStep = tr.fedex_track(df.TrackingID, auth)

                        else:
                                    LastStep = df.DateShipped
                                    ShippingStatus = "Not available - No Tracking ID!"
                        #LastStep, ShippingStatus = ""

            return LastStep, ShippingStatus

"""
    This function only calculates a day difference between time passed in each step and the norm-time for each step
    -> Priority function needs to be discussed!
"""
def calc_waiting(PrioDf, Priority, Status, LastStep):

            #print "Status: ", Status
            now = datetime.now()

            #print now

            """ find the row in the Priority dataframe that matches our priority-type """
            Row = PrioDf.loc[PrioDf['Type - Prio'] == Priority]
            print("Priority: ", Priority)

            """ match  norm-days per step with the current step """
            NormDays = Row.iloc[0, Status]

            #print "NormDays: ", NormDays

            dt = NormDays - days_between(LastStep, now)
            #print "dt: ", dt

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
