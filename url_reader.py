class UrlReader(object):
    def __init__(self, in_file):
        self.in_file = in_file

    def get_url(self):
        with open(self.in_file, "r") as in_file:
            for line in in_file:
                print("Processing {}".format(line))
                yield line.rstrip("\n")
