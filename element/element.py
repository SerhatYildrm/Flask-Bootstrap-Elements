


from abc import abstractmethod

class Element(object):
    """
        just element object
    """


    def __init__(self,value,_class,aria_label="",aria_current="",**kwargs):
        self.value = value
        self._class = _class
        self.html = ""
        self.aria_label = aria_label
        self.aria_current = aria_current
        if kwargs:
            self.kwargs = kwargs


    @abstractmethod
    def render(self):
        pass

    def addOthersProperty(self):
        if hasattr(self,"kwargs"):
            for key,value in self.kwargs.items():
                self.html += key+"='"+value+"'"


        if self.aria_label:
            self.html +="aria-label="+self.aria_label

        if self.aria_current:
            self.html += "aria-current="+self.aria_current


    def __str__(self):
        return str(self.render())
