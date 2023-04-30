import re
import sys
import getopt


def read_input_file(filepath: str) -> (int, list[list[int]]):
    """
    Reads a file of the format of pyramid_sample_input.text and outputs 
    a target value and the pyramid
    
    Args:
        filepath (str): path of file to open
    
    Returns:
        int: target value
        List[List[int]]: pyramid of values; each entry of the
            outermost list corresponds to a row of the pyramid
    """
    infile = open(filepath)

    # First line is the target
    line = infile.readline()
    target = int(re.split('[ \n]', line)[1])

    # Other lines comprise the pyramid
    pyramid = []
    while True:
        line = infile.readline()
        if line == '':
            break
        else:
            slist = re.split('[,\n]', line)[0:-1]
            nlist = [int(n) for n in slist]
            pyramid.append(nlist)
    infile.close()
    return target, pyramid


def int_to_lr(num: int, length: int) -> str:
    """
    Converts integers to the corresponding left/right path in a 
    corresponding pyramid.
    Args:
        num (int): index in dp[-1] indicating LR path
        length (int): expected length of output string
    Returns:
        str: corresponding LR path
    """
    output = []
    for j in range(length - 1, -1, -1):
        # Converting to L's and R's is the same as conversion to binary
        if num % (2 ** (j + 1)) >= (2 ** j):
            output.append('R')
        else:
            output.append('L')
    return ''.join(output)


def solve_pyramid(target: int, pyramid: list[list[int]]) -> str:
    """
    Returns a path in a pyramid such that the product of entries along
    the path equals the target value
    
    Args:
        target (int): target value
        pyramid (List[List[int]]): pyramid of values; each entry of the
            outermost list corresponds to a row of the pyramid
    
    Returns:
        str: string indicating the appropriate path down the pyramid,
            of the form "LRLLR". If no such path exists, returns
            "no solution".
    """
    dp = [[(1, 0)] * 2 ** j for j in range(len(pyramid))]
    # each entry is a tuple, with first entry being the product so far, and second 
    # entry being the current entry's index from the left within the pyramid.
    dp[0][0] = (pyramid[0][0], 0)
    for j in range(1, len(dp)):
        for k in range(len(dp[j])):
            parent = dp[j - 1][k // 2]  # parent entry in dp
            idx = parent[1] + ((k % 2) + 1) // 2  # corresponding index in pyramid
            dp[j][k] = (parent[0] * pyramid[j][idx], idx)
    # Searches for entry in dp[-1] that matches target
    for j in range(len(dp[-1])):
        if dp[-1][j][0] == target:
            # If this entry is target, convert to L's and R's and output
            return int_to_lr(j, len(dp) - 1)
    return "no solution"


def main(argv):
    input_file = ''
    output_file = ''
    opts, args = getopt.getopt(argv, "hi:o:")
    for opt, arg in opts:
        if opt == '-h':
            print('pyramid_solver.py -i <input_file> -o <output_file>')
            sys.exit()
        elif opt == "-i":
            input_file = arg
        elif opt == "-o":
            output_file = arg
    if input_file == '' or output_file == '':
        raise Exception("Need input and output file, indicated"
                        + " by -i <input_file> -o <output_file>")
    target, pyramid = read_input_file(input_file)
    solution = solve_pyramid(target, pyramid)
    print("Solution is: {}".format(solution))
    outfile = open(output_file, "w")
    outfile.write(solution)
    outfile.close()


if __name__ == "__main__":
    main(sys.argv[1:])
