# coding=utf-8

"""
    Paths to important files
"""
def auth_file():
    auth = 'U:\Ludwig_Boess\Python\Timeline\Data\qauth.txt'
    return auth

def prio_excel_path():
    Prio_Data = 'U:\Ludwig_Boess\Python\Timeline\Data\Prio.xlsx'
    return Prio_Data

def QS_POS_path():
    QS_POS = "U:\Ludwig_Boess\L003 QS-Auswertung KW aktuell.xlsx"
    return QS_POS

def QS_SEN_path():
    QS_POS = "U:\Ludwig_Boess\IDS-QS_Ludwig.xlsx"
    return QS_POS


def employees():

    empl = ['Sipos', 'Rück', 'Dienstmaier', 'Enayat', 'Burra']

    return empl

def status_touples():

    touples = [(0, 'Filter löschen'),
               (1, 'Aufgenommen'),
               (2, 'Retoure angeboten'),
               (3, 'Angekommen'),
               (4, 'Reparatur angeboten'),
               (5, 'Reparatur Angenommen'),
               (6, 'QS 1 abgeschlossen'),
               (7, 'QS 2 abgeschlossen'),
               (8, 'Versendet')
               ]

    return touples

def select_columns():
    columns = ['Titel', 'UHD', 'DatumBeginn', 'Customer', 'RMA', 'LastStep', 'Overdue', 'Bearbeiter']
    return columns

def sql_str_return():
    sql_str = "SELECT \
                uhdca.d_startdate AS [DatumBeginn], \
	            uhdca.s_callno AS [UHD], \
 	            uhdca.s_custname1 AS [Customer], \
	            uhdca.n_priority AS [Priority], \
	            cust.s_custno AS [CustNo], \
	            uhdca.s_optional1 AS [SN], \
	            por.d_pordate AS [DatumRetAngebot], \
	            del.d_delivdate AS [DatumAngekommen], \
	            uhdca.s_optional2 AS [RMA], \
	            offer.d_offerdate AS [DatumRepAngebot], \
	            uhdca.s_optional5 AS [RepAngebot], \
	            ord.d_orderdate AS [DatumRepAuftrag], \
	            ordpos.s_orderno AS [RepAuftr], \
	            del2.d_delivdate AS [DateShipped], \
	            del.s_atttrackingnr AS [TrackingID],\
	            uhdca.d_reminderdate AS [Wiedervorlage], \
	            uhdcat2.s_description AS [POS], \
	            uhdca.s_description AS [Titel], \
	            emp.s_name1 AS [Bearbeiter], \
	            uhdca.ls_question AS [Notizen] \
           FROM sao.UHDCALL uhdca \
                FULL OUTER JOIN sao.ORDPOSCOMBI ordpos ON uhdca.N_ORDERPOS2 = ordpos.i_ordposcombi \
                FULL OUTER JOIN sao.POR_P por ON uhdca.s_optional2 = por.s_porno \
                FULL OUTER JOIN sao.UHDCATEGORY1 uhdcat1 ON uhdca.i_uhdcategory1 = uhdcat1.i_uhdcategory1 \
                FULL OUTER JOIN sao.UHDCATEGORY2 uhdcat2 ON uhdca.i_uhdcategory2 = uhdcat2.i_uhdcategory2 \
                LEFT JOIN sao.POR2RET_P porret ON por.i_por_p = porret.i_por_p \
                FULL OUTER JOIN sao.ORDERS_P ord ON ordpos.s_orderno = ord.s_orderno \
                FULL OUTER JOIN sao.OFFER_P offer ON uhdca.s_optional5 = offer.s_offerno \
                FULL OUTER JOIN sao.EMPLOYEE_M emp ON emp.i_employee_m = uhdca.i_employee_m \
                LEFT JOIN sao.DELIVERY_P del ON del.i_delivery_p = porret.i_delivery_p \
                LEFT JOIN sao.ord2deliv_p orddel ON orddel.i_orders_p = ord.i_orders_p \
                LEFT JOIN sao.DELIVERY_P AS del2 ON del2.i_delivery_p = orddel.i_delivery_p \
                FULL OUTER JOIN sao.CUSTOMER_M cust ON uhdca.i_customer_m = cust.i_customer_m \
            WHERE uhdca.n_level2state = 1 \
                AND uhdcat1.s_description = 'Support' \
                AND uhdca.d_enddate IS NULL \
                AND uhdca.dt_deleted IS NULL \
                AND porret.dt_deleted IS NULL"

    return sql_str

#
# def accounts():
#
#     accounts = {}
