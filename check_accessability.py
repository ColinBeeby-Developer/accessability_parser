import argparse
import sys

from url_reader import UrlReader


class CheckAccessability(object):
    def __init__(self, args):
        self.in_file, self.out_file = self._getFiles(args)
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
            # beautiful soup stuff here

if __name__ == "__main__":
    parser = CheckAccessability(sys.argv)
    parser.run()
