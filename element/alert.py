


#-*- coding: utf-8 -*-

#Author: Serhat YILDIRIM
#Date: 17.01.2020 16:50

from element import Element
from markupsafe import Markup


class Alert(Element):
    def render(self):
        self.html = "<div class='{0}' role='alert' ".format(self._class)
        self.addOthersProperty()
        self.html += "> {0}</div>".format(self.value)

        return Markup(self.html)
        







