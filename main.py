import filecmp

test_dir = "tests/test1"
input_file = test_dir + "/input.txt"
output_file = test_dir + "/output.txt"
expected_file = test_dir + "/expected.txt"
output = open(output_file, 'w')
input = open(input_file, 'r')


def write(*args):
    for i in args:
        print(i, file=output, end="")

def main():
    # write("cou","cou")
    lines_list = input.readlines()
    # nb_lines = int(lines_list[0])
    lines = ''.join(lines_list[1:]).replace('\n','').replace(' ','')
    write(lines)
    # print(nb_lines)



def check():
    input.close()
    output.close()
    assert(open(output_file, 'r').read() == open(expected_file, 'r').read())



main()
check()