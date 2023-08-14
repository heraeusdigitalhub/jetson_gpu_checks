#!/usr/bin/env python3

"""
Check gpu temperature with jtop informations on nvidia jetson devices
"""

__author__ = "Chrisitan Piazzi"
__company__ = "Heraeus Consulting and IT Solutions"
__version__ = "0.1.0"
__license__ = "Apache 2.0"

import argparse
import sys
import jtop

icinga_codes = {'OK': 0, 
    	    	'WARNING': 1, 
                'CRITICAL': 2,
	    	'UNKNOWN': 3}

def icinga_return(code, response, perfdata=None):
    if perfdata is not None:
        print(code + ": " + response + " | " + perfdata)
    else:
        print(code + ": " + response)
    sys.exit(icinga_codes[code])


def get_stats():
    with jtop.jtop() as jetson:
        return jetson._stats

def get_gpu_temp(stats):
    return stats['temperature']['GPU']

def check_condition(warning=40, critical=50):
    """ Put some logic here
        Return check status code and message.
    """
    stats = get_stats()
    temp = get_gpu_temp(stats=stats)
    
    if temp < warning:
        return dict(code = "OK", message = "GPU temperature is OK",perfdata = str(temp))
    elif temp >= warning and temp < critical:
        return dict(code = "WARNING", message = "GPU temperature is WARNING",perfdata = str(temp))
    elif temp >= critical:
        return dict(code = "CRITICAL", message = "GPU temperature is CRITICAL",perfdata = str(temp))
    
def parse_args():
    parser = argparse.ArgumentParser(
        description='Script usage'
    )

    parser.add_argument(
        '-w', '--warning',
        metavar='warning_threshold',
        required=False,
        help='Define warning threshold'
    )

    parser.add_argument(
        '-c', '--critical',
        metavar='critical_threshold',
        required=False,
        help='Define critical threshold'
    )

    # Optional verbosity (for debug) -> Not implemented yet, maybe not needed
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        dest="debug_level",
        default=0,
        help="Verbosity. Enable debug mode in your script.")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    return parser.parse_args()

def main():
    try:
        args = parse_args()
    except:
        icinga_return('UNKNOWN', "Wrong usage")

    result = check_condition()
    icinga_return(result['code'],result['message'],result['perfdata'])


if __name__ == "__main__":
    main()

