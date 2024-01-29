#!/usr/bin/env python3

"""Check gpu temperature with jtop information on nvidia jetson devices."""

__author__ = "Chrisitan Piazzi"
__company__ = "Heraeus Consulting and IT Solutions"
__version__ = "0.1.0"
__license__ = "Apache 2.0"

import argparse
import sys

import jtop

icinga_codes = {"OK": 0, "WARNING": 1, "CRITICAL": 2, "UNKNOWN": 3}


def icinga_return(code, response, perfdata=None):
    """
    Print the response message and exit the program with the appropriate exit code.

    Parameters:
    code (str): The status code.
    response (str): The response message.
    perfdata (str, optional): Performance data. Defaults to None.
    """
    if perfdata is not None:
        print(code + ": " + response + " | " + perfdata)
    else:
        print(code + ": " + response)
    sys.exit(icinga_codes[code])


def get_stats():
    """
    Get the statistics from the jtop.

    Returns:
    dict: The statistics.
    """
    with jtop.jtop() as jetson:
        return jetson._stats


def get_gpu_temp(stats):
    """
    Get the GPU temperature from the statistics.

    Parameters:
    stats (dict): The statistics.

    Returns:
    int: The GPU temperature.
    """
    return stats["temperature"]["GPU"]


def check_condition(warni=40, critical=50):
    """
    Check the GPU temperature and return the status code, message, and performance data.

    Parameters:
    warni (int, optional): The warning threshold. Defaults to 40.
    critical (int, optional): The critical threshold. Defaults to 50.

    Returns:
    dict: The status code, message, and performance data.
    """
    stats = get_stats()
    temp = get_gpu_temp(stats=stats)
    print(temp)
    if temp < warni:
        return {"code": "OK", "message": "GPU temperature is OK", "perfdata": str(temp)}
    elif temp >= warni and temp < critical:
        return {"code": "WARNING", "message": "GPU temperature is WARNING", "perfdata": str(temp)}
    elif temp >= critical:
        return {"code": "CRITICAL", "message": "GPU temperature is CRITICAL", "perfdata": str(temp)}


def parse_args():
    """
    Parse the command line arguments.

    Returns:
    Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Script usage")

    parser.add_argument("-w", "--warning", metavar="warning_threshold", required=False, help="Define warning threshold")

    parser.add_argument(
        "-c", "--critical", metavar="critical_threshold", required=False, help="Define critical threshold"
    )

    # Optional verbosity (for debug)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        dest="debug_level",
        default=0,
        help="Verbosity. Enable debug mode in your script.",
    )

    # Specify output of "--version"
    parser.add_argument("--version", action="version", version=f"%(prog)s (version {__version__})")

    return parser.parse_args()


def main():
    """The main function of the script."""
    try:
        args = parse_args()
    except argparse.ArgumentError:
        icinga_return("UNKNOWN", "Wrong usage")

    result = check_condition(warni=int(args.warning), critical=int(args.critical))

    return (result["code"], result["message"], result["perfdata"])


if __name__ == "__main__":
    main()
