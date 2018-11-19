#! /usr/bin/env python

# Copyright (c) 2017 Martin Rosellen

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

__author__ = 'Martin Rosellen'
__docformat__ = "restructuredtext en"


import matplotlib.pyplot as plt
import argparse
import sys
import re


def main(argv):
    parser = argparse.ArgumentParser(description='plot data from agr_var.py script')
    parser.add_argument('file', help='data file structured as follows: (mutation \n mean: 1.2 \n variance: 0.002')
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        keys = []
        means = []
        vars = []
        p = re.compile("[A-Z]\d+[A-Z]")

        content = f.readlines()
        for i in range(len(content)):
            line =  content[i]
            l = p.search(line)
            if l:
                keys.append(l.string)
                if 'mean' in content[i+1]:
                    means.append(float(content[i+1].split()[1]))
                if 'var' in content[i+2]:
                    vars.append(float(content[i+2].split()[1]))
                i = i + 2
                
    fig, ax = plt.subplots()
    ax.scatter([str(i) for i in range(len(keys))],vars)
    ax.set_xticks([i for i in range(len(keys))])
    ax.set_xticklabels(keys, rotation=45)
    plt.show()

if __name__ == '__main__':
    main(sys.argv)

