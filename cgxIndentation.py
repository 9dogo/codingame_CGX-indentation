import re
import string

class CgxIndentation:
    def __init__(self, test_dir) -> None:
        self.input_file_name = test_dir + "/input.txt"
        self.output_file_name = test_dir + "/output.txt"
        self.input_file = open(self.input_file_name, 'r')
        self.output_file = open(self.output_file_name, 'w')
        self.expected_file_name = test_dir + "/expected.txt"

    def write(self,*args):
        for i in args:
            print(i, file=self.output_file, end="")

    def isIndexInBounds(self, index, bounds):
        for b in bounds:
            if index > b[0] and index < b[1]:
                return True
        return False

    def replaceMatchingPattern(self, c, replacement):
        # retrieve position of single quotes
        quotes = [m.start() for m in re.compile("\'").finditer(self.all)]
        strings = [(quotes[i], quotes[i+1]) for i in range(len(quotes)-1) if i%2==0]
        print("strings ", strings)
        # retrieve the position of all the characters 'c'
        char_indexes = [(m.start(), m.end()) for m in re.compile(c).finditer(self.all)][::-1]
        print("indexes of ", c, " : ", char_indexes)
        # insert an end of line behind all these characters, if they are not in a string
        for cs, ce in char_indexes:
            if not self.isIndexInBounds(cs, strings):
                self.all = self.all[:cs] + replacement + self.all[ce:]


    def generateCgx(self):
        lines_list = self.input_file.readlines()
        # put everything in the same line
        self.all = ''.join(lines_list[1:]).replace('\n','')

        print(self.all)

        # we don't want to work with the first or the last character
        self.all = "\n" + self.all + "\n"

        # remove spaces and tabs after equals
        self.replaceMatchingPattern("[\s]*[\t]*\=[\s]*[\t]*", "=")
        # insert an end of line after ; unless they are followed by a (
        self.replaceMatchingPattern(";", ";\n")
        # insert an end of line before and after (
        self.replaceMatchingPattern("\(", "\n(\n")
        # insert an end of line before )
        self.replaceMatchingPattern("\)", "\n)")
        
        # remove consecutive end of line
        self.all = re.sub("[\n]+", "\n", self.all)

        # remove indentation
        self.all = self.all.strip()
        self.all = re.sub("\n\s*\t*", "\n", self.all)

        print(self.all)

        # add the correct indentation
        # -> split self.all into lines, add the correct number of tabulation for each line by counting the opening and closing parenthesis
        lines = self.all.split("\n")

        res = ""
        indent = 0
        for l in lines:
            if l[0] == ')':
                indent -= 4
                res += '\n' + indent * ' ' + l.rstrip()
            else:
                res += '\n' + indent * ' ' + l.rstrip()
                if l[0] == '(':
                    indent += 4

        # remove the first line as it is empty
        res = res.lstrip()

        # write the result into the output file
        self.write(res)
    
    
    def closeFiles(self):
        self.input_file.close()
        self.output_file.close()

