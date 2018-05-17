#from fedex.config import FedexConfig
#from fedex.services.track_service import FedexTrackRequest
#from ClassicUPS import UPSConnection
from datetime import datetime




def get_carrier(TrackingID):
            if TrackingID[:2] == '1Z':
                        return "UPS"

            if TrackingID[:1] == '7':
                        return 'FedEx'

            if TrackingID[:2] == 'GD':
                        return 'TNT'


def fedex_track(TrackingID, auth):

            '''
                        TO DO!
            '''
            '''
            key = auth[0]
            account_number = auth[1]
            meter_no = auth[2]
            password = auth[3]


            CONFIG_OBJ = FedexConfig(key=key,
                         password=password,
                         account_number=account_number,
                         meter_number=meter_no)

            track = FedexTrackRequest(CONFIG_OBJ)
            track.SelectionDetails.PackageIdentifier.Type = 'TRACKING_NUMBER_OR_DOORTAG'
            track.SelectionDetails.PackageIdentifier.Value = TrackingID
            track.send_request()

            """ edit return value! """
            return track.response
            '''
            return 'Fedex Tracking not done yet!', datetime.now()


def ups_track(TrackingID, auth):

    return 'UPS Tracking not done yet!', datetime.now()
            # license_number = auth[4]
            # user_id = auth[5]
            # password = auth[6]
            #
            # ups = UPSConnection(license_number,
            #         user_id,
            #         password,
            #         debug=True)  # Set to false when ready
            #
            # tracking = ups.tracking_info(TrackingID)
            #
            # #print tracking.shipment_activities[0]
            #
            # last_step = tracking.shipment_activities[0]['Status']['StatusType']['Code']
            #
            # date_string = tracking.shipment_activities[0]['Date']
            # last_date = datetime.strptime(date_string, '%Y%m%d')
            #
            # """
            #             Return description of last step and date of that step
            # """
            # if last_step == 'D':
            #             #signed = tracking.shipment_activities[0]['ActivityLocation']['SignedForByName']
            #             return 'Delivered.', last_date
            # elif last_step == 'M':
            #             return 'Manifest', last_date
            # elif last_step == 'X':
            #             return 'Exception', last_date
            # elif last_step == 'P':
            #             return 'Pickup', last_date
            # elif last_step == 'I':
            #             city = tracking.shipment_activities[0]['ActivityLocation']['Address']['City']
            #             return 'In transit. Last location: ' + city, last_date

