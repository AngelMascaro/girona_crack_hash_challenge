import argparse
#Script params
parser = argparse.ArgumentParser(description='Merge 2 text files into 1 and remove repeated values')
#requiered
parser.add_argument('-i1', '--inputFile1', type=str, help='Param inputFile1')
parser.add_argument('-i2', '--inputFile2', type=str, help='Param inputFile2')
args = parser.parse_args()
filename1 = args.inputFile1
filename2 = args.inputFile2

def merge(filename1, filename2):
    with open(filename1, 'r') as f1:
        with open(filename2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            lines1 = [x.strip() for x in lines1]
            lines2 = [x.strip() for x in lines2]
            lines1 = list(set(lines1))
            lines2 = list(set(lines2))
            lines = list(set(lines1 + lines2))
            with open('newFile.txt', 'w') as f:
                for line in lines:
                    f.writelines(line + "\r")
            
if __name__ == '__main__':
    merge(filename1, filename2)