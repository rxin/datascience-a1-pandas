In this assignment, you will use Python and Pandas to explore and analyze the 2012 Presidential Campaign Finance data set.


## Data Set

- Download the data set from 2012 Presidential Campaign Finance website http://www.fec.gov/disclosurep/PDownload.do

- Make sure you download ALL.zip rather than records for individual states.

- Once you unzip the file, you will find P00000001-ALL.txt.

- Use command line programs such as “less” to view it (CSV format).

- Read the File Format page on the website to understand the CSV file’s schema.


## Python and Pandas

- Install Python if you haven’t yet on your workstation. If you are not familiar with Python, Google has a fairly good tutorial on it http://code.google.com/edu/languages/google-python-class/

- Install Pandas 0.7.0rc1. On most Mac and Linux workstations, this should be as simple as calling “easy_install pandas”. On other systems, read the Installation page on Pandas’ website for more details (http://pandas.sourceforge.net).

- Read Pandas documentation on its website. You will find the following parts particularly useful for this assignment: Intro to Data Structures, Essential basic functionality, Computational tools, Group By: split-apply-combine, API Reference.

- Play with the data set using Pandas and Python’s REPL mode (interactive mode).


## Assignment Python Script

- Download a1.py Python script from http://www.cs.berkeley.edu/~rxin/datascience/a1/a1.py

- Replace [STUDENT NAME] and [STUDENT EMAIL] in the header comment section with your name and your email address.

- There are 10 functions you need to implement in this file. The function signatures have already been defined for you and functionalities are specified in docstrings. Implement these 10 functions.

- Note that it might be helpful to test your data flows in Python REPL (interactive mode) before putting them in the function bodies.


## Questions

Answer the following questions and save your answers in a1.txt. Be succinct. You will be penalized for excessively verbose answers. Save the data flow you conducted for answering these questions in main function in a1.py.

1. Are there any outliers in the contribution amount column?

2. In num_donors() we assume people have unique names (i.e. no two person share the same name). Can you find examples of donation records that violate this assumption, and to what degree can we trust this assumption?

3. In how many states are President Obama the top candidate (by total amount of donations received)? Does this mean Obama is going to win the election?

4. In how many states have Republican candidates received more donations than President Obama?

5. Explore the data on your own and jot down three interesting things you find.


## Submissions

- Submit both a1.py and a1.txt on coursekit.


