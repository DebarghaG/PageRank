"""
Parser to read the files
"""
import networkx as nx


class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.G = nx.Graph()

    def read(self):
        file1 = open(self.filename, 'r')
        count = 0
        #while True: if you have the RAM of a chad
        while count<100000:
            count += 1
            line = file1.readline()
            if not line:
                break
            e = map(int,line.split())
            self.G.add_edge(*e)

            #print("Line{}: {}".format(count, line.strip()))

        file1.close()
        print("Read : " + str(count) + " Lines")

    def PageRank(self):
        self.pr = nx.pagerank(self.G, alpha=0.85)
        print(self.pr)

if __name__ == '__main__':
    parse = Parser('../data/GoogleWeb.txt')
    parse.read()
    parse.PageRank()
