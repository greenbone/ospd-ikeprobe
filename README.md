![Greenbone Logo](https://www.greenbone.net/wp-content/uploads/gb_logo_resilience_horizontal.png)

# ospd-ikeprobe

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/greenbone/ospd-ikeprobe/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/greenbone/ospd-ikeprobe/?branch=master)

This is an OSP server implementation to allow GVM to remotely control
an `ikeprobe` scanner, see <http://www.heise.de/download/ikeprobe-1123010.html>.

`ospd-ikeprobe` tries to identify IPSEC VPN endpoints which are sending
Pre-Shared Keys within the Aggressive mode.

Once running, you need to configure the Scanner for Greenbone Vulnerability
Manager, for example via the web interface Greenbone Security Assistant.
Then you can create scan tasks to use this scanner.

## Installation

### Requirements

Python 3 and later is supported.

Beyond the [ospd base library](https://github.com/greenbone/ospd) and the
`ikeprobe` tool, `ospd-ikeprobe` has no further dependencies.

There are no special installation aspects for this module beyond the general
installation guide for ospd-based scanners.

Please follow the general installation guide for ospd-based scanners:

  <https://github.com/greenbone/ospd/blob/master/doc/INSTALL-ospd-scanner.md>

## Usage

There are no special usage aspects for this module beyond the generic usage
guide.

Please follow the general usage guide for ospd-based scanners:

  <https://github.com/greenbone/ospd/blob/master/doc/USAGE-ospd-scanner.md>

## Support

For any question on the usage of ospd-ikeprobe please use the [Greenbone
Community Portal](https://community.greenbone.net/c/gse). If you found a
problem with the software, please [create an
issue](https://github.com/greenbone/ospd-ikeprobe/issues) on GitHub. If you are
a Greenbone customer you may alternatively or additionally forward your issue
to the Greenbone Support Portal.

## Maintainer

This project is maintained by [Greenbone Networks
GmbH](https://www.greenbone.net/).

## Contributing

Your contributions are highly appreciated. Please [create a pull
request](https://github.com/greenbone/ospd-ikeprobe/pulls) on GitHub. Bigger
changes need to be discussed with the development team via the [issues section
at GitHub](https://github.com/greenbone/ospd-ikeprobe/issues) first.

## License

Copyright (C) 2015-2018 [Greenbone Networks GmbH](https://www.greenbone.net/)

Licensed under the [GNU General Public License v2.0 or later](COPYING).
