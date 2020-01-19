


from abc import abstractmethod

class Element(object):
    """
        just element object
    """
    @abstractmethod
    def render(self):
        pass

    def addOthersProperty(self):
        if hasattr(self,"kwargs"):
            for key,value in self.kwargs.items():
                self.html += key+"='"+value+"'"



