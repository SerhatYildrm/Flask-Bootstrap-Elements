


#-*- coding: utf-8 -*-

#Author: Serhat YILDIRIM
#Date: 17.01.2020 16:50

from element import Element
from markupsafe import Markup


class Badges(Element):    def render(self):
        self.html = "<span class='{0}' ".format(self._class)
        self.addOthersProperty()
        self.html += "> {0}</span>".format(self.value)

        return Markup(self.html)
        







