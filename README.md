This repository contains the code to solve pyramid puzzles. Consider a pyramid such that each row of the pyramid is a list of integers, with the length increasing by one each row. Ex:

<pre>
    1    
   2 3
  4 5 6
 7 8 9 1 </pre>

The goal is to find a path down the pyramid such that the product of entries along the path is equal to a given target value. The output is a string of 'L' and 'R' characters indicating left or right steps that create the desired path. 

The pyramid_solver.py file contains all the code to read in an input file, solve the corresponding pyramid puzzle, then write the solution to an output file. Note that this code will return the first path found down the pyramid whose product is equal to the input 'target', rather than a list of all possible solutions. You can call it from the command line with the following:

\>\> python pyramid_solver.py -i <input_file.txt> -o <output_file.txt>

There is also a corresponding test file to run the code from pyramid solver on 5 test cases; it can be run with the following:

\>\> python pyramid_test.py

(for the job application to AoPS)
<br>Joshua Schroeder
