This repository contains the code to solve any pyramid puzzle, for the job application to AoPS.
Joshua Schroeder

The pyramid_solver.py file contains all the code to read in an input file, solve the corresponding pyramid puzzle, then write the solution to an output file. Note that this code will return the first path found down the pyramid whose product is equal to the input 'target', rather than a list of all possible solutions. You can call it from the command line with the following:

\>\> python pyramid_solver.py -i <input_file.txt> -o <output_file.txt>

There is also a corresponding test file to run the code from pyramid solver on 5 test cases; it can be run with the following:

\>\> python pyramid_test.py
