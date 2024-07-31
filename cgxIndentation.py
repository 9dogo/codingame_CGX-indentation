
class CgxIndentation:
    def __init__(self, test_dir) -> None:
        self.input_file_name = test_dir + "/input.txt"
        self.output_file_name = test_dir + "/output.txt"
        self.input_file = open(self.input_file_name, 'r')
        self.output_file = open(self.output_file_name, 'w')
        self.expected_file_name = test_dir + "/expected.txt"
        pass

    def write(self,*args):
        for i in args:
            print(i, file=self.output_file, end="")

    def generateCgx(self):
        lines_list = self.input_file.readlines()
        # nb_lines = int(lines_list[0])
        lines = ''.join(lines_list[1:]).replace('\n','').replace(' ','')
        self.write(lines)
    
    def closeFiles(self):
        self.input_file.close()
        self.output_file.close()

