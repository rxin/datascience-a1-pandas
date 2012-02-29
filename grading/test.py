#!/usr/bin/python

"""
This is used to semi-automatically grade students' submissions.

Reynold Xin
rxin@cs.berkeley.edu
Feb 2012
"""

from __future__ import division
import math
import re
import sys
import time

import numpy as np
from pandas import *

import ref  # this is the reference solution
import a1   # this is student's submission


def compareTupleOrList(v1, v2):
    if len(v1) != len(v2):
        return False
    for a, b in zip(v1, v2):
        if not compare(a, b):
            return False
    return True


def compareFloat(v1, v2):
    FLOAT_DELTA = 0.0001
    if (v1 < v2 + FLOAT_DELTA and v1 > v2 - FLOAT_DELTA):
        return True
    return False


def compare(v1, v2):
    if type(v1) is float or type(v1) is np.float64:
        return compareFloat(v1, v2)
    elif type(v1) is tuple or type(v2) is list:
        return compareTupleOrList(v1, v2)
    else:
        return v1 == v2


def testFunction(index, function_name, df, refdf, *args):
    # run reference solution
    t = time.time()
    ref_out = getattr(ref, function_name)(refdf, *args)
    ref_time = time.time() - t

    # run student submission
    t = time.time()
    student_out = getattr(a1, function_name)(df, *args)
    student_time = time.time() - t

    # Compare outputs. The execution time comparison is not rigorous but good
    # enough.
    correct = compare(ref_out, student_out)
    print index,
    print ' ',
    print correct,
    print '  ' + function_name
    print '  ',
    print student_out
    print '  ',
    print ref_out
    print '  ',
    print '%.2f\t%.2f\t%.2f' % (student_time / ref_time, student_time, ref_time)
    return (function_name, correct, ref_out, student_out)


def main(*args):

    # basic unit testing
    # Should be: True, True, True, True, False, False, False, False
    """
    print compare(1, 1)
    print compare(1.234, 1.2340000001)
    print compare('lalala', 'lalala')
    print compare(('lalala', 1.234), ('lalala', 1.2340000001))
    print compare(1, 2)
    print compare(1.234, 2.133)
    print compare('mine', 'yours')
    print compare(('lalala', 1.234), ('lalala', 1.235))
    """

    # print the python source header (for confirming student name)
    src = open('a1.py').read()
    print re.search(r'""".+?"""', src, flags=re.DOTALL).group(0)

    # now do the testing
    df = read_csv('P00000001-ALL.txt')
    df = a1.add_party_column(df)

    refdf = read_csv('P00000001-ALL.txt')
    refdf = ref.add_party_column(refdf)
    
    testFunction(2, 'num_donation_records', df, refdf)
    testFunction(3, 'num_refund_records', df, refdf)
    testFunction(4, 'num_donors', df, refdf, 'CA')
    testFunction(5, 'top_candidate_by_num_donors', df, refdf, 'CA')
    testFunction(6, 'top_candidate_by_amount', df, refdf, 'CA')
    testFunction(7, 'top_party_by_num_donors', df, refdf, 'CA')
    testFunction(8, 'top_party_by_amount', df, refdf, 'CA')
    testFunction(9, 'num_bipartisan_donors', df, refdf)
    testFunction(10, 'bucketize_donation_amounts', df, refdf)


if __name__ =='__main__':
    sys.exit(main(*sys.argv[1:]))

