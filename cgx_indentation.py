"""
Provide class CgxIndentation
"""

from io import TextIOWrapper
import re

class CgxIndentation:
    """
    A class used to indent a content in a CGX way (codingame puzzle)

    Attributes
    ----------
    input_cgx : str
        the content to indent in CGX

    Methods
    -------
    __init__()
        Constructor
    
    write(*args)
        Write the *args in the output file

    is_index_in_bounds(index, bounds)
        Determine wheter or not an index is within one of the bounds
    
    replace_matching_patterns(c, replacement)
        Replace the character 'c' by 'replacement' in self.input_cgx
    
    generate_cgx
        Indent the content of the input_file, write the result in the output file

    close_files
        Close the input and output files opened in __init__
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.input_cgx = ""

    def is_index_in_bounds(self, index : int, bounds : list) -> bool:
        """
        Determine wheter or not an index is within one of the bounds

        Parameters
        ----------
        index : int
            The index to check
        bounds : list
            The list of bounds

        Return
        ------
        True if the index is in range of one of the bounds, else False
        """
        for (bs, be) in bounds:
            if bs < index < be:
                return True
        return False

    def replace_matching_patterns(self, c : str, replacement : str) -> None:
        """
        Replace each pattern 'c' by 'replacement' if it is not in a string of input_cgx

        Parameters
        ----------
        c : str
            the pattern to replace in self.input_cgx
        replacement : str
            the string ot insert in self.input_cgx to replace 'c'
        """
        # retrieve position of single quotes, defining the strings
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


    def generate_cgx(self, input_file : TextIOWrapper, output_file : TextIOWrapper) -> None:
        """
        Indent the content of the input_file, write the result in the output file
        """
        lines_list = input_file.readlines()
        # put everything in the same line
        self.input_cgx = ''.join(lines_list[1:]).replace('\n','')

        print(self.input_cgx)

        # we don't want to work with the first or the last character
        self.input_cgx = "\n" + self.input_cgx + "\n"

        # remove spaces and tabs after equals
        self.replace_matching_patterns(r'[\s]*[\t]*\=[\s]*[\t]*', "=")
        # insert an end of line after ; unless they are followed by a (
        self.replace_matching_patterns(";", ";\n")
        # insert an end of line before and after (
        self.replace_matching_patterns(r'\(', "\n(\n")
        # insert an end of line before )
        self.replace_matching_patterns(r'\)', "\n)")

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
        for i in res:
            print(i, file=output_file, end="")
