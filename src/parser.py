"""
Parser to read the files
"""

class Parser:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        file1 = open(self.filename, 'r')
        count = 0
        while True:
            count += 1
            line = file1.readline()

            if not line:
                break
            #print("Line{}: {}".format(count, line.strip()))

        file1.close()
        print("Read : " + str(count) + " Files")

if __name__ == '__main__':
    parse = Parser('../data/GoogleWeb.txt')
    parse.read()
