import argparse
import re
import sys


class ParseWgetUrls(object):
    def __init__(self, args):
        self.inFile, self.outFile = self._getFiles(args)
        self.acceptableLineRegex = re.compile("^http://localhost:8000/.*/$")

    def run(self):
        with open(self.inFile, "r") as infile:
            with open(self.outFile, "w") as outfile:
                for line in infile:
                    writeLine = self._isLineWritable(line)
                    if writeLine:
                        outfile.write(line)

    def _getFiles(self, args):
        parser = argparse.ArgumentParser(description="input and output files")
        parser.add_argument("infile")
        parser.add_argument("outfile")
        args = parser.parse_args()
        return args.infile, args.outfile

    def _isLineWritable(self, line):
        result = self.acceptableLineRegex.match(line)
        if result:
            return True
        return False


if __name__ == "__main__":
    parser = ParseWgetUrls(sys.argv)
    parser.run()
