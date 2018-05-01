class TaxiTrip(object):

    def __init__(self, tripID, taxiID, tripStartTImestamp, pickupCommunityArea, lattitude, longitude):
        self.tripID = tripID
        self.taxiID = taxiID
        self.tripStartTimestamp = tripStartTImestamp
        self.pickupCommunityArea = pickupCommunityArea
        super.__init__(lattitude, longitude)


class CrimeRecord(Coordinate):
    def __init__(self, id, date, communityArea, lattitude, longitude):
        self.id = id
        self.date = date
        self.communityArea = communityArea
        super.__init__(lattitude, longitude)


class Coordinate(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


    @property
    def point(self):
        return {'x' : self.latitude,
                'y' : self.longitude}

