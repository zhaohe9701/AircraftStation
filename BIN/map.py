import os
import folium
from branca.element import IFrame
from folium import MacroElement
from jinja2 import Template

from PySide6.QtCore import QUrl
from folium.plugins import MousePosition

from net.mapJsHandler import MapJsHandler
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineCore import QWebEngineSettings


# 定义JavaScript代码


class FsMap:
    def __init__(self):
        self.map = folium.Map(location=[30.1833, -239.7595],
                              tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
                              zoom_start=13, attr='default')

        self.map.add_child(folium.LatLngPopup())  # 显示鼠标点击点经纬度
        self.map.add_child(MousePosition(prefix='经纬度:',
                                         position='topright'))

    def saveMapHtml(self):
        # pass
        self.map.save("../net/save_map.html")


if __name__ == "__main__":
    m = FsMap()
    m.saveMapHtml()


class MapWidget:
    def __init__(self):
        self.channel = QWebChannel()
        self.handler = MapJsHandler()

    def setUpMap(self, view):
        self.channel.registerObject('py', self.handler)
        view.page().setWebChannel(self.channel)
        view.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        view.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        url = os.path.abspath(os.path.dirname(os.getcwd())) + '\\net\\map.html'
        url = url.replace("\\", "/")
        print(url)
        view.load(QUrl(url))
