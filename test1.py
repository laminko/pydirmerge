#!/usr/bin/env python

VERSION = '1.0.1'

import argparse

parser = argparse.ArgumentParser(description='To merge separated folders into one.')
parser.add_argument('-v', action = 'store_true', help = 'Verbose mode.')
parser.add_argument('-V', action = 'version', version = 'version %s' % VERSION)
parser.add_argument('-i', type = str, required = True, metavar = 'DIR', nargs = '+', help = 'Source folders. AT LEAST TWO FOLDERS REQUIRED.')
parser.add_argument('-o', type = str, required = True, metavar = 'DIR', nargs = 1, help = 'Destination folder.')
args = parser.parse_args()

print vars(args)