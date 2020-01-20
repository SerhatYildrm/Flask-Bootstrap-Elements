


#-*- coding: utf-8 -*-

#Author: Serhat YILDIRIM
#Date: 17.01.2020 16:50

from element import Element
from markupsafe import Markup



# File "app.py", line 21
#    bread2 =BreadcrumbLi("About",_class="breadcrumb-item active",aria-current="page")                                                               ^
#SyntaxError: keyword can't be an expression






class Breadcrumb(Element):
    def render(self):
        self.html = """
            <nav aria-label='breadcrumb' 
        """.format(self._class)
        self.addOthersProperty()
        self.html += "> {0}</nav>".format(self.value)

        return Markup(self.html)
        


class BreadcrumbOl(Element):

    def render(self):
        self.html = """
            <ol class='{0}' 
        """.format(self._class)
        self.addOthersProperty()
        self.html += "> {0} </ol>".format(self.value)

        return Markup(self.html)


class BreadcrumbLi(Element):
    def render(self):
        self.html = """
            <li class={0}
        """.format(self._class)
        self.addOthersProperty()
        self.html += ">{0} </li>".format(self.value)

        return Markup(self.html)
