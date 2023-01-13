import argparse
#Script params
parser = argparse.ArgumentParser(description='Split text files')
#requiered
parser.add_argument('-i', '--inputFile', type=str, help='Param inputFile')
#optional
parser.add_argument('-n', '--numberParts', type=int, help='Param numberParts (default = 10)')

args = parser.parse_args()
filename = args.inputFile
number_parts = args.numberParts

def splitfile(filename, number_parts=10):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        lines_per_part = len(lines) // number_parts
        for i in range(number_parts):
            with open(str(i+1) + "-" + filename, 'w') as f:
                f.writelines(lines[i * lines_per_part:(i + 1) * lines_per_part])
            
if __name__ == '__main__':
    splitfile(filename, number_parts)