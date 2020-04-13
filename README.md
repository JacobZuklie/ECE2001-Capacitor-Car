# ECE2001-Capacitor-Car
2020 ECE2001 Capacitor Car Material Calculator
In order for this calculator to work you will need to install numpy and matplotlib, you can pip install into the environment 
you post the code in.

  In "Main Calculator.py" you are able to enter information on the materials into the given lists.  There is no function
that checks to make sure that the lists are the same size, having lists that are smaller or larger than analagous lists 
will cause problems.  However entering new materials in is easy,  just need to follow the units above the lists.


Most of the calculations are done in SubCalc.py, this has 4 different classes that are called by "Main Calculator.py"
  
The series class iterates over all possible material combinations for a series based design, and then saves and returns the 
values that correspond to the lowest calculated weight.

The parallel class iterates over all possible material combinations for a parallel based design, and then saves and returns the 
values that correspond to the lowest calculated weight.

Both the WvS and WvT classes are repsonsible for collecting data that is used for generating the graphs.
