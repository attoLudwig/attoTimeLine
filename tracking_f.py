from fedex.config import FedexConfig
from fedex.services.track_service import FedexTrackRequest
from ClassicUPS import UPSConnection

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


def ups_track(TrackingID, auth):

            license_number = auth[0]
            user_id = auth[1]
            password = auth[2]

            ups = UPSConnection(license_number,
                    user_id,
                    password,
                    debug=True)  # Set to false when ready

            tracking = ups.tracking_info(TrackingID)

            last_step = tracking.shipment_activities[0]['Status']['StatusType']['Code']

            """
                        Return description of last step and date of that step
            """
            if last_step == 'D':
                        signed = tracking.shipment_activities[0]['ActivityLocation']['SignedForByName']
                        return 'Delivered. Signed by: ' + signed, tracking.shipment_activities[0]['Date']
            elif last_step == 'M':
                        return 'Manifest', tracking.shipment_activities[0]['Date']
            elif last_step == 'X':
                        return 'Exception', tracking.shipment_activities[0]['Date']
            elif last_step == 'P':
                        return 'Pickup', tracking.shipment_activities[0]['Date']
            elif last_step == 'I':
                        city = tracking.shipment_activities[0]['ActivityLocation']['Address']['City']
                        return 'In transit. Last location: ' + city, tracking.shipment_activities[0]['Date']


'''
            Testing
'''
"""
#TrackingID = '1Z29340V6670553000'

TrackingID = '735594506654'

shipper = get_carrier(TrackingID)

shipper

test = fedex_track(TrackingID)

test
test['ActivityLocation']['SignedForByName']
"""
