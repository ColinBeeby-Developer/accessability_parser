import argparse
import sys

from result_writer import ResultWriter
from url_reader import UrlReader


class CheckAccessability(object):
    def __init__(self, args):
        in_file, out_file = self._getFiles(args)
        self.url_reader = UrlReader(in_file)
        self.result_writer = ResultWriter(out_file)
        # need to do something here to read in the rule

    def _getFiles(self, args):
        parser = argparse.ArgumentParser(description="input and output files")
        parser.add_argument("infile")
        parser.add_argument("outfile")
        args = parser.parse_args()
        return args.infile, args.outfile

    def run(self):
        for url in self.url_reader.get_url():
            print(url)


if __name__ == "__main__":
    parser = CheckAccessability(sys.argv)
    parser.run()
