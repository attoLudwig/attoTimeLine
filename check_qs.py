import pandas as pd

def QS_POS(SN, df_QS):

    try:
        QS1 = df_QS[(df_QS['s/n'] == SN) & (df_QS["1 OK?"] == "Ja")].Datum.tail(1).iloc[0]
    except:
        QS1 = pd.NaT

    try:
        QS2 = df_QS[(df_QS['s/n'] == SN) & (df_QS["2 OK?"] == "Ja")].Datum.tail(1).iloc[0]
    except:
        QS2 = pd.NaT

    return QS1, QS2


def QS_SEN(SN, df_QS):

    # check if IDS
    QS1, QS2 = pd.NaT, pd.NaT

    if SN[0] != "I":
        return QS1, QS2

    else:

        SN_arr = SN.split('0')
        SN = SN_arr[-1]

        """ DISCUSS!! QS1 as latest none-passed test? """
        try:
            QS1 = df_QS[(df_QS['Nr.'] == SN) & (df_QS["Bestanden"] == "Nein")].Datum.tail(1).iloc[0]
        except:
            QS1 = pd.NaT

        try:
            QS2 = df_QS[(df_QS['Nr.'] == SN) & (df_QS["Bestanden"] == "Ja")].Datum.tail(1).iloc[0]
        except:
            QS2 = pd.NaT

        return QS1, QS2
