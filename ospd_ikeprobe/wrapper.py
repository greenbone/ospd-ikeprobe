# -*- coding: utf-8 -*-
# Description:
# Core of the OSP ikeprobe Server
#
# Authors:
# Christian Fischer <info@schutzwerk.com>
#
# Copyright:
# Copyright (C) 2015 Greenbone Networks GmbH
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.

from ospd.ospd import OSPDaemon
from ospd.misc import main as daemon_main
from ospd_ikeprobe import __version__

import subprocess
import os

OSPD_ikeprobe_DESC = """
This scanner runs the tool 'ikeprobe' on the local host where the scanner is installed.

ikeprobe tries to identify IPSEC VPN endpoints which are sending
Pre-Shared Keys within the Aggressive mode.
"""

OSPD_ikeprobe_PARAMS = \
    {'exe_path':
     {'type': 'string',
      'name': 'Exe path',
      'default': "c:\Program Files\ikeprobe\ikeprobe.exe",
      'mandatory': 0,
      'description': 'Path to the ikeprobe.exe',},

     'use_wine':
     {'type': 'boolean',
      'name': 'Use WINE',
      'default': '0',
      'mandatory': 0,
      'description': 'Whether to use WINE on linux systems to run ikeprobe.exe (experimental). Set the Exe path to e.g. /opt/ikeprobe/ikeprobe.exe.',},}

class OSPDikeprobe(OSPDaemon):

    """ Class for ospd-ikeprobe daemon. """

    def __init__(self, certfile, keyfile, cafile):
        """ Initializes the ospd-ikeprobe daemon's internal data. """
        super(OSPDikeprobe, self).__init__(certfile=certfile, keyfile=keyfile,
                                            cafile=cafile)
        self.server_version = __version__
        self.scanner_info['name'] = 'ikeprobe'
        self.scanner_info['version'] = 'depends on the version of the installed scanner'
        self.scanner_info['description'] = OSPD_ikeprobe_DESC
        for name, param in OSPD_ikeprobe_PARAMS.items():
            self.add_scanner_param(name, param)

    def check(self):
        # If we hard-code the path to the scanner, we could check it there
        return True

    def exec_scan(self, scan_id, target):
        """ Starts the ikeprobe scanner for scan_id scan. """

        options = self.get_scan_options(scan_id)
        exe_path = options.get('exe_path')
        use_wine = options.get('use_wine')

        if use_wine == 1:
            p = subprocess.Popen(['wine', exe_path, target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=dict(os.environ, WINEDEBUG="-all"))
            result = str(p.communicate())
        else:
            p = subprocess.Popen([exe_path, target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = str(p.communicate())

        if 'System not vulnerable' in result:
            self.add_scan_alarm(scan_id, host=target, name='IPSEC VPN not vulnerable',
              qod=95, value=result, port='500/udp')
            return 0
        elif 'System is vulnerable' in result:
            self.add_scan_alarm(scan_id, host=target, name='IPSEC VPN vulnerable',
              qod=95, value=result, port='500/udp', severity='5.0')
            return 0
        else:
            self.add_scan_error(scan_id, host=target,
              value='A problem occurred trying to execute "ikeprobe": %s' % result)
            return 2


def main():
    """ OSP ikeprobe main function. """
    daemon_main('OSPD - ikeprobe wrapper', OSPDikeprobe)
