# # !/usr/bin/env python3
import grabtoken
import exceptions
import keep 

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('note', help='String to use as Note\'s Text')
parser.add_argument('title', nargs='?', help='String to use as Note\'s Title') 
parser.add_argument('-l', '--label', action='store', help='Label to assign the Note to')    # catch multiple lablels 
parser.add_argument('-p', '--pinned', action='store_true', help='Pin note')
parser.add_argument('--color', choices=[color for color in keep.noteColors], help='Choose note color')

args = parser.parse_args()





