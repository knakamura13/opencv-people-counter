#!/usr/bin/env python

import sys

def main(args):
	# Remove first item from list (filename).
	args.pop(0)

	# Loop over parameters and their arguments.
	for arg in args:
		pair = arg.split("=")

		if len(pair) == 1:
  			param = arg
			print(arg)
		else:
			print(pair[0] + " = " + pair[1])
			param = ""
			arg = ""

# Call main() func on file load.
if __name__ == '__main__':
	main(sys.argv)