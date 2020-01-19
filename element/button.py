

# -*- coding: utf-8 -*-

#Author: Serhat Yıldırım
#Date: 19.01.2020 16:43



from element import Element
from markupsafe import Markup

class Button(Element):
    def __init__(self,value,_type="button",_class="btn btn-primary",active=True,**kwargs):
        """
            :params value Button value
            :params _type Button type (button,reset,submit)
            :params _class add class (you can button style)
            :active True or false
            :**kwargs you can add onclick event or other property on button
        """
        
        self.value = value
        self._type = _type
        self._class = _class

        if kwargs:
            self.kwargs = kwargs


    

    def render(self):
        self.html = "<button type='{0}' class='{1}' ".format(self._type,self._class)
        #if hasattr(self,"kwargs"):
        #    for key,value in self.kwargs.items():
        #        htmlButton += key+"='"+value+"'"

        self.addOthersProperty()
        self.html +=">{0}</button>".format(self.value)
        return Markup(self.html)

