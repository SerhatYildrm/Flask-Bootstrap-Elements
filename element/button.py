

# -*- coding: utf-8 -*-

#Author: Serhat Yıldırım
#Date: 19.01.2020 16:43



from element import Element
from markupsafe import Markup

class Button(Element):    

    def render(self):
        self.html = "<button type='{0}' class='{1}' ".format(self._type,self._class)
        #if hasattr(self,"kwargs"):
        #    for key,value in self.kwargs.items():
        #        htmlButton += key+"='"+value+"'"

        self.addOthersProperty()
        self.html +=">{0}</button>".format(self.value)
        return Markup(self.html)

