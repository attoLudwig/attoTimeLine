from fedex.config import FedexConfig
from fedex.services.track_service import FedexTrackRequest
from fedex.tools.conversion import sobject_to_dict
#from ClassicUPS import UPSConnection
from datetime import datetime
import requests
import json
import xmltodict
import config


def get_carrier(TrackingID):
            if TrackingID[:2] == '1Z':
                        return "UPS"

            if TrackingID[:1] == '7':
                        return 'FedEx'

            if TrackingID[:2] == 'GD':
                        return 'TNT'


def fedex_track(TrackingID, auth):

    # key = auth[0]
    # account_number = auth[1]
    # meter_no = auth[2]
    # password = auth[3]
    #
    # CONFIG_OBJ = FedexConfig(key=key,
    #                      password=password,
    #                      account_number=account_number,
    #                      meter_number=meter_no)
    #
    # track = FedexTrackRequest(CONFIG_OBJ)
    #
    # track.SelectionDetails.PackageIdentifier.Type = 'TRACKING_NUMBER_OR_DOORTAG'
    # track.SelectionDetails.PackageIdentifier.Value = TrackingID
    # track.send_request()
    #
    # response_dict = sobject_to_dict(track.response)
    #
    # return response_dict

    return "Fedex not done yet.", datetime.now()

"""
    Fedex track written by hand!
"""
# def fedex_track(TrackingID, auth):
#
#             key = auth[0]
#             account_number = auth[1]
#             meter_no = auth[2]
#             password = auth[3]
#
#             url = 'https://wsbeta.fedex.com:443/web-services/track'
#
#             headers = {'content-type': 'text/xml'}
#
#             body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
#                       xmlns:v14="http://fedex.com/ws/track/v14">
#                         <soapenv:Header/>
#                         <soapenv:Body>
#                             <v14:TrackRequest>
#                                 <v14:WebAuthenticationDetail>
#                                     <v14:UserCredential>
#                                         <v14:Key>{}</v14:Key>
#                                         <v14:Password>{}</v14:Password>
#                                     </v14:UserCredential>
#                                 </v14:WebAuthenticationDetail>
#                                 <v14:ClientDetail>
#                                     <v14:AccountNumber>{}</v14:AccountNumber>
#                                     <v14:MeterNumber>{}</v14:MeterNumber>
#                                 </v14:ClientDetail>
#                                 <v14:TransactionDetail>
#                                     <v14:CustomerTransactionId>Track By Number_v14</v14:CustomerTransactionId>
#                                     <v14:Localization>
#                                         <v14:LanguageCode>EN</v14:LanguageCode>
#                                         <v14:LocaleCode>US</v14:LocaleCode>
#                                     </v14:Localization>
#                                 </v14:TransactionDetail>
#                                 <v14:Version>
#                                     <v14:ServiceId>trck</v14:ServiceId>
#                                     <v14:Major>14</v14:Major>
#                                     <v14:Intermediate>0</v14:Intermediate>
#                                     <v14:Minor>0</v14:Minor>
#                                 </v14:Version>
#                                 <v14:SelectionDetails>
#                                     <v14:CarrierCode>FDXE</v14:CarrierCode>
#                                     <v14:PackageIdentifier>
#                                         <v14:Type>TRACKING_NUMBER_OR_DOORTAG</v14:Type>
#                                         <v14:Value>{}</v14:Value>
#                                     </v14:PackageIdentifier>
#                                     <v14:ShipmentAccountNumber/>
#                                     <v14:SecureSpodAccount/>
#                                         <v14:Destination>
#                                             <v14:GeographicCoordinates>rates evertitque aequora</v14:GeographicCoordinates>
#                                         </v14:Destination>
#                                     </v14:SelectionDetails>
#                                 </v14:TrackRequest>
#                             </soapenv:Body>
#                         </soapenv:Envelope>""".format(key, password, account_number, meter_no, TrackingID)
#
#
#             """
#                 	with parent credentials
#             """
#             # body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
#             #           xmlns:v14="http://fedex.com/ws/track/v14">
#             #             <soapenv:Header/>
#             #             <soapenv:Body>
#             #                 <v14:TrackRequest>
#             #                     <v14:WebAuthenticationDetail>
#             #                         <v14:ParentCredential>
#             #                             <v14:Key>{}</v14:Key>
#             #                             <v14:Password>{}</v14:Password>
#             #                         </v14:ParentCredential>
#             #                         <v14:UserCredential>
#             #                             <v14:Key>{}</v14:Key>
#             #                             <v14:Password>{}</v14:Password>
#             #                         </v14:UserCredential>
#             #                     </v14:WebAuthenticationDetail>
#             #                     <v14:ClientDetail>
#             #                         <v14:AccountNumber>{}</v14:AccountNumber>
#             #                         <v14:MeterNumber>{}</v14:MeterNumber>
#             #                     </v14:ClientDetail>
#             #                     <v14:TransactionDetail>
#             #                         <v14:CustomerTransactionId>Track By Number_v14</v14:CustomerTransactionId>
#             #                         <v14:Localization>
#             #                             <v14:LanguageCode>EN</v14:LanguageCode>
#             #                             <v14:LocaleCode>US</v14:LocaleCode>
#             #                         </v14:Localization>
#             #                     </v14:TransactionDetail>
#             #                     <v14:Version>
#             #                         <v14:ServiceId>trck</v14:ServiceId>
#             #                         <v14:Major>14</v14:Major>
#             #                         <v14:Intermediate>0</v14:Intermediate>
#             #                         <v14:Minor>0</v14:Minor>
#             #                     </v14:Version>
#             #                     <v14:SelectionDetails>
#             #                         <v14:CarrierCode>FDXE</v14:CarrierCode>
#             #                         <v14:PackageIdentifier>
#             #                             <v14:Type>TRACKING_NUMBER_OR_DOORTAG</v14:Type>
#             #                             <v14:Value>{}</v14:Value>
#             #                         </v14:PackageIdentifier>
#             #                         <v14:ShipmentAccountNumber/>
#             #                         <v14:SecureSpodAccount/>
#             #                             <v14:Destination>
#             #                                 <v14:GeographicCoordinates>rates evertitque aequora</v14:GeographicCoordinates>
#             #                             </v14:Destination>
#             #                         </v14:SelectionDetails>
#             #                     </v14:TrackRequest>
#             #                 </soapenv:Body>
#             #             </soapenv:Envelope>""".format(key, password, key, password, account_number, meter_no, TrackingID)
#
#             r = requests.post(url, data=body, headers=headers)
#
#             #return_dict = xmltodict.parse(r.content, process_namespaces=True)
#
#             return r.content
#
#
#
#             #return 'Fedex Tracking not done yet!', datetime.now()


def ups_track(TrackingID, auth):

    url = 'https://onlinetools.ups.com/rest/Track'

    json_request = {
            "UPSSecurity": {
                "UsernameToken": {
                    "Username": auth[5],
                    "Password": auth[6]
                    },
                "ServiceAccessToken": {
                    "AccessLicenseNumber": auth[4]
                    }
                },
                "TrackRequest": {
                    "Request": {
                        "RequestOption": "1",
                        "TransactionReference": {
                            "CustomerContext": "Tracking"
                            }
                        },
                    "InquiryNumber":  TrackingID
                    }
            }

    r = requests.post(url, json=json_request)

    json_return = r.json()

    # check if requests was successful
    if json_return["TrackResponse"]["Response"]["ResponseStatus"]["Code"] == '1':

        date_string = json_return["TrackResponse"]["Shipment"]["Package"][0]["Activity"][0]["Date"]
        last_date = datetime.strptime(date_string, '%Y%m%d')

        step_type = json_return["TrackResponse"]["Shipment"]["Package"][0]["Activity"][0]["Status"]["Type"]

        # set return value for delivered
        if step_type == 'D':
            signed = json_return["TrackResponse"]["Shipment"]["Package"][0]["Activity"][0]["ActivityLocation"]["SignedForByName"]
            return_string = "Delivered. Signed for by: " + signed

        # set return value for in transit
        elif step_type == 'I':
            last_city = json_return["TrackResponse"]["Shipment"]["Package"][0]["Activity"][0]["ActivityLocation"]["Address"]["City"]
            return_string = "In transit. Last Location: " + last_city

        # set return value for manifest
        elif step_type == 'M':
            return_string = "Manifest."

        elif step_type == 'X':
            desc = json_return["TrackResponse"]["Shipment"]["Package"][0]["Activity"][0]["Status"]["Description"]
            return_string = "Exception. Description: "

        elif step_type == 'P':
            return_string = "Pickup."

        return return_string, last_date

    else:

        return 'JSON Error!', datetime.now()
