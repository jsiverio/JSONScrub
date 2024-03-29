"""_summary_ = "This script is used to scrub the JSON file that is generated by Cellebrite PA """

import sys
import Scrubber


def main():
    '''Driver function for the PDNAScrubber.py script. 
    This function creates a Scrubber object and calls the scrub method.'''
    if len(sys.argv) > 1:
        scrubber = Scrubber.Scrubber(sys.argv[1])
        scrubber.scrub()
    else:
        print("Usage: PDNAScrubber.py <path to JSON file>")
        sys.exit(1)

main()
