About OSPD-IKEPROBE
-------------------

This is a OSP server implementation to allow GVM to remotely control
a ikeprobe scanner, see http://www.heise.de/download/ikeprobe-1123010.html
OSPD-IKEPROBE tries to identify IPSEC VPN endpoints which are sending 
Pre-Shared Keys within the Aggressive mode.

Once running, you need to configure the Scanner for Greenbone Vulnerability
Manager, for example via the web interface Greenbone Security Assistant.
Then you can create scan tasks to use this scanner.

OSPD-IKEPROBE is licensed under GNU General Public License Version 2 or
any later version.  Please see file COPYING for details.

All parts of OSP-IKEPROBE are Copyright (C) by Greenbone Networks GmbH
(see http://www.greenbone.net).


How to start OSPD-IKEPROBE
--------------------------

There are no special usage aspects for this module
beyond the general usage guide.

Please follow the general usage guide for ospd-based scanners:

  https://github.com/greenbone/ospd/blob/master/doc/USAGE-ospd-scanner
