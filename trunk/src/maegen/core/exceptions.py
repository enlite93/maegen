# -*- encoding: UTF-8 -*-

#    Maegen is a genealogical application for N900. Use it on the go
#    to store genealogical data including individuals and relational
#    informations. Maegen can be used to browse collected data on the
#    device but the main goal is its capabilitie to export the dtabase
#    in a GEDCOM file which can be imported into any desktop genealocial
#    application.
#
#    Copyright (C) 2011  Thierry Bressure
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
'''
Created on Oct 29, 2011

@author: maemo
'''

from ..common import version 

version.getInstance().submitRevision("$Revision$")

class MaegenException(Exception):
    """
    Base class for all application exception
    """
    def __init_(self, message=None, cause=None):
        self.meseage = message
        self.cause = cause
        
    def __str__(self):
        if cause:
            return  repr(self.message) + "caused by \n" + repr(self.cause)
        else:
            return repr(self.message)
        

class MaegenIntegrityExceptiopn(MaegenException):
    """
    A database intéegrity error was detected
    """
    pass