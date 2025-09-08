# Local script imports
from wt_imports import *
from wt_classes import CustomNameSpace
from wt_runner_functions import *
from wt_helper_functions import *

def runner(args: CustomNameSpace):
	show_metadata()

def update_options(value: str) -> list[str]:
	# Split the input st ring by commas and return as a list
	items = value.split(',')
	capitalized_items = [item.upper() for item in items]

	# Define the allowed choices
	allowed_choices = {'LPS', 'DDS'}

	# Check if all the items are in the allowed choices
	for item in capitalized_items:
		if item not in allowed_choices:
			raise argparse.ArgumentTypeError(f"Invalid choice: {item}. Allowed choices are: {', '.join(allowed_choices)}")
	return capitalized_items

def arg_parse() -> CustomNameSpace:
	parser = argparse.ArgumentParser(description="FIXME", prefix_chars='-+', formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('--date',
					 	type=str,
						required=False,
						default=f"{date.today().strftime('%Y-%m-%d')}",
						help='(str) - aowowwoww')
	parser.add_argument('--update', '-u',
					 	type=update_options,
						required=False,
						default=[],
						help="(list[str]) - Forcefully update modules within the program. If an update is requested, all downstream modules will re-run as well.\nAllowed values:\n\tblah\nModules will automatically update themselves if necessary\n")
	parser.add_argument('--debug', '-d',
						action='store_true',
						required=False,
						default=False,
						help='(bool) - Add debug messages to stdout')
	parser.add_argument('--verbose', '-v',
						action='store_true',
						required=False,
						default=False,
						help='(bool) - Add extra debug messages to stdout')

	return parser.parse_args(namespace=CustomNameSpace())

if __name__ == '__main__':
	# Get and process command line arguments
	args = arg_parse()
	print(args)

	# Start program
	runner(args)