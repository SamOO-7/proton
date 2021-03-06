#!/usr/bin/env python3

#            ---------------------------------------------------
#                             Proton Framework              
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import core.implant

class EnumPrintersJob(core.job.Job):
    def done(self):
        self.display()

    def display(self):
        self.shell.print_plain("Printer Connections:")
        self.shell.print_plain(self.data)
        self.results = self.data

class EnumPrintersImplant(core.implant.Implant):
    
    NAME = "Enumerate Printer Connections"
    DESCRIPTION = "Enumerates all Printer Connections."
    AUTHORS = ["Entynetproject"]
    STATE = "implant/gather/enum_printers"

    def load(self):
        pass    
    
    def job(self):
        return EnumPrintersJob

    def run(self):
        payloads = {}
        payloads["js"] = "data/implant/gather/enum_printers.js"
        self.dispatch(payloads, self.job)

    
