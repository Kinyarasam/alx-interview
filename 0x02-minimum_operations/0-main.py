#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 625
print("Min # of operations to reach {} char: {}".format(
    n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char {}".format(
    n, minOperations(n)))

n = 36
print("Min # of operations to reach {} char {}".format(
    n, minOperations(n)))
