import argparse
import sys

from result_writer import ResultWriter
from rules_engine import RulesEngine
from url_reader import UrlReader


class CheckAccessability(object):
    def __init__(self, args):
        in_file, out_file, rules_file = self._getFiles(args)
        self.url_reader = UrlReader(in_file)
        self.result_writer = ResultWriter(out_file)
        self.rules_engine = RulesEngine(rules_file)

    def _getFiles(self, args):
        parser = argparse.ArgumentParser(description="input and output files")
        parser.add_argument("infile")
        parser.add_argument("outfile")
        parser.add_argument("rulesfile")
        args = parser.parse_args()
        return args.infile, args.outfile, args.rulesfile

    def run(self):
        for url in self.url_reader.get_url():
            match_found, matching_rule = self.rules_engine.check_url(url)
            if match_found:
                self.result_writer.add_result("{} - {}".format(url, matching_rule))

        self.result_writer.output_results()


if __name__ == "__main__":
    parser = CheckAccessability(sys.argv)
    parser.run()
