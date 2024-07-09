"""
difflib is a Python library module that provides tools for computing and working with differences between sequences.
It's particularly useful for tasks such as comparing files,generating difference reports, and performing text
analysis.
"""

import difflib

with open('test.txt') as g_data:
    g_config = g_data.read()

with open('test1.txt') as n_data:
    n_config = n_data.read()


delta = difflib.Differ().compare(g_config.splitlines(), n_config.splitlines())

print(delta)

for data in delta:
    print(data)

"""
In a diff output, the - symbol indicates that a line or element is present in the first sequence but not 
in the second sequence.
"""

"""
In a diff output, the + symbol indicates that a line or element is present in the second sequence 
but not in the first sequence (original sequence).
"""

