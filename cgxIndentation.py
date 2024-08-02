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

    def generateCgx(self):
        lines_list = self.input_file.readlines()
        # put everything in the same line
        all = ''.join(lines_list[1:]).replace('\n','')

        indent = 0
        in_string = False
        res = []
        # iterate through each characters of "all" and the next non-blank character
        for c,cn in [(all[i], all[i+1:].lstrip()[0]) for i in range(len(all)-1)]+[(all[-1], all[-1])]:
            # we don't want to modify the strings, delimited by ' '
            if c == '\'':
                in_string = not in_string
            if in_string:
                res += c
            else:
                if (c == '(' and cn == ')') or (c == '(' and cn == '('):
                    res += '\n' + ' '*indent + c
                    indent += 4
                elif c == '(':
                    res += '\n' + ' '*indent
                    indent += 4
                    res += c + '\n' + ' '*indent
                elif c == ')':
                    indent -= 4
                    res += '\n' + ' '*indent + c
                elif c == ';' and cn != '(':
                    res += c + '\n' + ' '*indent
                elif c != ' ':
                    res += c

        # remove the first line if it's empty (appends if the first char of "all" was a '(')
        if res[0] == '\n':
            res.remove('\n')
        if res[0] == '\t':
            res.remove('\n')
            
        # convert the result to a single string and write it in the output file
        self.write(''.join(res))
    
    
    def closeFiles(self):
        self.input_file.close()
        self.output_file.close()

