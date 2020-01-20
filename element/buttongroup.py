

# -*- coding: utf-8 -*-

#Author: Serhat Yıldırım
#Date: 19.01.2020 16:43



from element import Element
from markupsafe import Markup

class ButtonGroup(Element):    

    def render(self):
        self.html = """
            <div class='{0}' role='toolbar'
        """.format(self._class)
        self.addOthersProperty()
        self.html +=">{0}</div>".format(self.value)
        return Markup(self.html)



class Group(Element):
    def render(self):
        self.html = "<div class='{0}' role='group' ".format(self._class)
        self.addOthersProperty()
        self.html + = ">{0}</div>".format(self.value)
        return Markup(self.html)



