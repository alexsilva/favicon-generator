#!/usr/bin/python3
import os
import logging
from PIL import Image
from pilkit.processors import ProcessorPipeline, ResizeToFit

logger = logging.getLogger(__name__)

SIZES_DEFAULT = [
	##
	# FileName   LogoSize   BoxSize
	##
	["favicon-32", [32, 32], [32, 32]],
	["favicon-57", [57, 57], [57, 57]],
	["favicon-76", [76, 76], [76, 76]],
	["favicon-96", [96, 96], [96, 96]],
	["favicon-120", [120, 120], [120, 120]],
	["favicon-128", [128, 128], [128, 128]],
	["smalltile", [128, 128], [128, 128]],
	["favicon-144", [144, 144], [144, 144]],
	["favicon-152", [152, 152], [152, 152]],
	["favicon-180", [180, 180], [180, 180]],
	["favicon-196", [196, 196], [196, 196]],
	["favicon-228", [228, 228], [228, 228]],
	["mediumtile", [270, 270], [270, 270]],
	["widetile", [270, 270], [558, 270]],
	["largetile", [558, 558], [558, 558]],
]


# Function that downloads images
def favicon_generator(original_image, directory, sizes=None) -> list:
	if sizes is None:
		sizes = SIZES_DEFAULT
	results = []
	for filename, logo_size, box_size in sizes:
		im = Image.open(original_image)
		processor = ProcessorPipeline([ResizeToFit(logo_size[0], logo_size[1])])
		result = processor.process(im)
		background = Image.new('RGBA', box_size, (255, 255, 255, 0))
		background.paste(
			result, (int((box_size[0] - result.size[0]) / 2), int((box_size[1] - result.size[1]) / 2))
		)
		background.save(background.save(os.path.join(directory, filename + ".png")))
		logger.info("{}.png generated".format(filename))
		results.append(result)
	return results


