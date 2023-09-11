import argparse
import os

from faviconGenerator import favicon_generator


def main(original_image, directory_name):
	print("\nFaviconGenerator by Hecsall\n")

	# Manage the directory name
	if directory_name == "threadDirectory":
		directory = "faviconGenerator"
	else:
		directory = directory_name[1:] if directory_name[0] == '/' else directory_name

	# Creates the directory
	if not os.path.exists(directory):
		os.makedirs(directory)

	# Start the favicon generator
	favicon_generator(original_image, directory)
	print("\nAll the Favicons generated in \"{}\" folder\n".format(directory))


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Generate web favicons from an image.')

	parser.add_argument('originalimage', nargs='+', help='Original Image of the favicon')
	parser.add_argument('-o', '--output', default='threadDirectory',
	                    help='Directory name where the script saves the images. '
	                         'Default directory name will be \"faviconGenerator\".')

	args = parser.parse_args()

	main(*args.originalimage, args.output)
