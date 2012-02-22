#!/usr/bin/python
"""
CS194-16 Data Science Assignment 1
UC Berkeley

[STUDENT NAME]
[STUDENT EMAIL]

"""

from __future__ import division
import math
import sys

import numpy as np
from pandas import *


def add_party_column(df):
    """Add a column representing the candidate's party to the data frame.

    Args:
        df: A DataFrame generated from the campaign finance data csv file.

    Returns:
        A DataFrame based on df with an additional column keyed "party" whose
        values represent the party of the candidates.
        For Democratic candidates, use value "Democrat".
        For Republicans, use "Republican".
        For Libertarian candidates, use value "Libertarian".
    """
    # TODO: Implement this function.
    pass


def num_donation_records(df):
    """Return the total number of donation records.
    
    Args:
        df: A DataFrame generated from the campaign finance data csv file.

    Returns:
        An integer count of the number of donation records.
    """
    # TODO: Implement this function.
    pass


def num_refund_records(df):
    """Return the number of refund records.
    
    Args:
        df: A DataFrame generated from the campaign finance data csv file.

    Returns:
        An integer count of the number of refund records.
    """
    # TODO: Implement this function.
    pass


def num_donors(df, state):
    """Return the number of people that have donated in the given state.
    
    Assume people have unique names (i.e. no two person share the same name).
    Do not count the same person twice.

    Args:
        df: A DataFrame generated from the campaign finance data csv file.
        state: The state of interest in capitalized two-letter format,
            e.g. "CA".

    Returns:
        An integer count of the number of donors.
    """
    # TODO: Implement this function.
    pass


def top_candidate_by_num_donors(df, state):
    """Find the candidate that received the most donations (by the number of
    donation records) in a given state.

    Args:
        df: A DataFrame generated from the campaign finance data csv file.
        state: The state of interest in capitalized two-letter format,
            e.g. "CA".

    Returns:
        A tuple consisting of a pair of values. The first value should be the
        name of the candidate, and the second value should be the fraction of
        the number of donations he received compared with all candidates.
        E.g. ('Cain, Herman', 0.115).
    """
    # TODO: Implement this function.
    pass


def top_candidate_by_amount(df, state):
    """Find the candidate that received the highest amount of donations in
    a given state.

    Args:
        df: A DataFrame generated from the campaign finance data csv file.
        state: The state of interest in capitalized two-letter format,
            e.g. "CA".

    Returns:
        A tuple consisting of a pair of values. The first value should be the
        name of the candidate, and the second value should be the fraction of
        donations he received compared with all candidates.
        E.g. ('Cain, Herman', 0.05).
    """
    # TODO: Implement this function.
    pass


def top_party_by_num_donors(df, state):
    """Find the party that received the most donations (by the number of
    donation records) in a given state.

    Args:
        df: A DataFrame generated from the campaign finance data csv file
            with the column "party" added.
        state: The state of interest in capitalized two-letter format,
            e.g. "CA".

    Returns:
        A tuple consisting of a pair of values. The first value should be the
        name of the party, as defined in add_party_column(df), and the second
        value should be the fraction of the number of donations the party
        received compared with other parties. E.g. ('Democrat', 0.115).
    """
    # TODO: Implement this function.
    pass


def top_party_by_amount(df, state):
    """Find the party that received the highest amount of donations in a given
    state.

    Args:
        df: A DataFrame generated from the campaign finance data csv file
            with the column "party" added.
        state: The state of interest in capitalized two-letter format,
            e.g. "CA".

    Returns:
        Return a tuple consisting of a pair of values. The first value should be
        the name of the party, as defined in add_party_column(df), and the
        second value should be the fraction of the amount of donations the party
        received compared with other parties. E.g. ('Democrat', 0.21).
    """
    # TODO: Implement this function.
    pass


def num_bipartisan_donors(df):
    """Find the number of people that have donated to more than one parties.
    
    Args:
        df: A DataFrame generated from the campaign finance data csv file
            with the column "party" added.

    Returns:
        An integer count of the number of people that have donated to more than
        one parties.
    """
    # TODO: Implement this function.
    pass


def bucketize_donation_amounts(df):
    """Generate a histogram for the donation amount.

    Put donation amount into buckets and generate a histogram for these buckets.
    The buckets are: (0, 1], (1, 10], (10, 100], (100, 1000], (1000, 10000],
    (10000, 100000], (100000, 1000000], (1000000, 10000000].

    Args:
        df: A DataFrame generated from the campaign finance data csv file.

    Returns:
        A list containing 8 integers. The Nth integer is the count of donation
        amounts that fall into the Nth bucket. E.g. [2, 3, 4, 5, 4, 3, 1, 1].
    """
    # TODO: Implement this function.
    pass


def main(*args):
    df = read_csv('P00000001-ALL.txt')
    add_party_column(df)

    # TODO: Put the code you used to explore the data set here.


if __name__ =='__main__':
    sys.exit(main(*sys.argv[1:]))

