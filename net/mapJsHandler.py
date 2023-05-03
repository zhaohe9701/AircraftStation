from PySide6.QtCore import QObject, Slot


class MapJsHandler(QObject):

    def __init__(self):
        super().__init__(None)
        self.lat = 0.0
        self.lng = 0.0

    @Slot(float, float)
    def sendLatLng(self, lat, lng):
        self.lat = lat
        self.lng = lng
