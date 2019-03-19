#!/usr/bin/python

from imageai.Detection import ObjectDetection
import os
import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print('Try using the syntax: test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	execution_path = os.getcwd()

	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel(detection_speed="fast")

	custom_objects = detector.CustomObjects(car=True, person=True)

	detections = detector.detectCustomObjectsFromImage(
		custom_objects=custom_objects,
		input_image=inputfile,
		output_image_path=outputfile,
	)

if __name__ == "__main__":
	main(sys.argv[1:])
