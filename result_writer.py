class ResultWriter(object):
    def __init__(self, out_file):
        self.out_file = out_file
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def output_results(self):
        with open(self.out_file, "w") as out_file:
            for result in self.results:
                out_file.write(result)
