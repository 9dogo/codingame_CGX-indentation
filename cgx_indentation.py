import re

class Cgx_indentation:
    def __init__(self, test_dir) -> None:
        self.input_file_name = test_dir + "/input.txt"
        self.output_file_name = test_dir + "/output.txt"
        self.input_file = open(self.input_file_name, 'r')
        self.output_file = open(self.output_file_name, 'w')
        self.expected_file_name = test_dir + "/expected.txt"

    def write(self,*args):
        for i in args:
            print(i, file=self.output_file, end="")

    def is_index_in_bounds(self, index, bounds):
        for (bs, be) in bounds:
            if bs < index < be:
                return True
        return False

    def replace_matching_pattern(self, c, replacement):
        # retrieve position of single quotes
        quotes = [m.start() for m in re.compile("\'").finditer(self.input_cgx)]
        strings = [(quotes[i], quotes[i+1]) for i in range(len(quotes)-1) if i%2==0]
        print("strings ", strings)
        # retrieve the position of input_cgx the characters 'c'
        char_indexes = [(m.start(), m.end()) for m in re.compile(c).finditer(self.input_cgx)][::-1]
        print("indexes of ", c, " : ", char_indexes)
        # insert an end of line behind input_cgx these characters, if they are not in a string
        for cs, ce in char_indexes:
            if not self.is_index_in_bounds(cs, strings):
                self.input_cgx = self.input_cgx[:cs] + replacement + self.input_cgx[ce:]


    def generate_cgx(self):
        lines_list = self.input_file.readlines()
        # put everything in the same line
        self.input_cgx = ''.join(lines_list[1:]).replace('\n','')

        print(self.input_cgx)

        # we don't want to work with the first or the last character
        self.input_cgx = "\n" + self.input_cgx + "\n"

        # remove spaces and tabs after equals
        self.replace_matching_pattern(r'[\s]*[\t]*\=[\s]*[\t]*', "=")
        # insert an end of line after ; unless they are followed by a (
        self.replace_matching_pattern(";", ";\n")
        # insert an end of line before and after (
        self.replace_matching_pattern(r'\(', "\n(\n")
        # insert an end of line before )
        self.replace_matching_pattern(r'\)', "\n)")

        # remove consecutive end of line
        self.input_cgx = re.sub("[\n]+", "\n", self.input_cgx)

        # remove indentation
        self.input_cgx = self.input_cgx.strip()
        self.input_cgx = re.sub(r'\n\s*\t*', "\n", self.input_cgx)

        print(self.input_cgx)

        # add the correct indentation
        # -> split self.input_cgx into lines, add the correct number of tabulation for each line,
        #  by counting the opening and closing parenthesis
        lines = self.input_cgx.split("\n")

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

    
    def close_files(self):
        self.input_file.close()
        self.output_file.close()
