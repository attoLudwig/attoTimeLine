from datetime import datetime
from Timeline import db

class UHD(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    """ Customer Success Info """
    DatumBeginn = db.Column(db.DateTime, index=True)
    UHD = db.Column(db.String(120), index=True, unique=True)
    POSSEN = db.Column(db.String(120))
    Titel = db.Column(db.String(128))
    Bearbeiter = db.Column(db.String(120))
    Notizen = db.Column(db.String(128))

    """ Customer Info """
    Customer = db.Column(db.String(128))
    CustNo = db.Column(db.Integer)
    Priority = db.Column(db.Integer)

    """ Product Info """
    SN = db.Column(db.String(128))
    RMA = db.Column(db.String(120))
    RepAngebot = db.Column(db.String(120))
    RepAuftr = db.Column(db.String(120))

    """ Event dates """
    DatumRetAngebot = db.Column(db.DateTime)
    DatumAngekommen = db.Column(db.DateTime)
    DatumRepAngebot = db.Column(db.DateTime)
    DatumRepAuftr = db.Column(db.DateTime)
    QS1 = db.Column(db.DateTime)
    QS2 = db.Column(db.DateTime)
    DateShipped = db.Column(db.DateTime)
    Wiedervorlage = db.Column(db.DateTime)

    """ Tracking """
    TrackingID = db.Column(db.String(120))
    ShippingStatus = db.Column(db.String(128))

    """ Status """
    Status = db.Column(db.Integer)
    PriorityCalc = db.Column(db.Float64)
    Waiting = db.Column(db.Float64)
    LastStep = db.Column(db.DateTime)
    Overdue = db.Column(db.Boolean)

    """
        Add stuff for scatterplot like in Excel?
    """

    def __repr__(self):
        return '<UHD {}>'.format(self.UHD)
