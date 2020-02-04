#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# CoverageProcessing is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# CoverageProcessing is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# Author : Fabien Rétif - fabien.retif@zoho.com
#
from __future__ import division, print_function, absolute_import
from spatialetl.exception import CoverageError

class VariableNameError(CoverageError):

    def __init__(self,module,msg,code):
        CoverageError.__init__(self,module,msg)
        self.code_error = code
        self.message_error = msg

    def __str__(self):
        return "["+self.module + "] "+self.message_error+ ". Code error: "+str(self.code_error)



