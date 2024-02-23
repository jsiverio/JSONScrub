import Scrubber
import sys

def main():
    if len(sys.argv) > 1:
            scrubber = Scrubber.Scrubber(sys.argv[1])
            scrubber.scrub()
    else:
        print("Usage: PDNAScrubber.py <path to JSON file>")
        exit(1)

main()
    