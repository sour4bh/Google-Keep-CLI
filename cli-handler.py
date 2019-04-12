# # !/usr/bin/env python3
# import grabtoken
# import exceptions
import keep

import argparse

# seperate usage cases for put, fetch, labels


parser = argparse.ArgumentParser()
parser.add_argument('command', choices=['put', 'fetch', 'labels'], help='Action to perform')
parser.add_argument('note', help='String to use as Note\'s Text')
parser.add_argument('title', nargs='?', help='String to use as Note\'s Title')
parser.add_argument('-l', '--label', action='store', help='Label to assign the Note to')    # catch multiple lablels 
parser.add_argument('-p', '--pinned', action='store_true', help='Pin note')
parser.add_argument('--color', choices=[color for color in keep.noteColors], help='Choose note color')

args = parser.parse_args()
if args.command == 'put':
    keep.postNote(args.title, args.note, labels=[label for label in args.label], pin=True if args.pinned else False, color=args.color)
elif args.command == 'fetch':
    print(keep.findNote(queryStr=args.note, labels=args.label, pinned=args.pinned))
elif args.command == 'labels':
    # list labels; note arg nargs = ?;
    # procced using empty string for note arg
    keep.listLabels()
