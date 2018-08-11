#!/usr/bin/env python
import os
import re
import sys

nargs = len(sys.argv)

if not 3 <= nargs <= 5:
    raise SystemExit("usage: %s search_pattern replacement [infile [outfile]]" %
          os.path.basename(sys.argv[0]))
else:
    stext = sys.argv[1]
    rtext = sys.argv[2]
    input_file = sys.stdin
    output_file = sys.stdout

    if nargs > 3:
        input_arg = sys.argv[3]
        print("Reading from %s" % input_arg)
        input_file = open(input_arg, 'r')

    if nargs > 4:
        output_arg = sys.argv[4]
        print("Writing to %s..." % output_arg)
        output_file = open(output_arg, 'w')

    for line in input_file:
        output_file.write(re.sub(stext, rtext, line))

    print("\n\nExiting")
    output_file.close()
    input_file.close()
    sys.exit(1)
