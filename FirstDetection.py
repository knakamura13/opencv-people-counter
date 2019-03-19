#!/usr/bin/python

from imageai.Detection import ObjectDetection
import os
import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["inputfile=","outputfile="])
	except getopt.GetoptError:
		print('Try using the syntax: test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print('Usage:\t-h, --help:\t\t Get help')
			print('\t-i, --inputfile:\t Select input file')
			print('\t-o, --outputfile:\t Select output file')
			sys.exit(2)
		elif opt in ("-i", "--inputfile"):
			inputfile = arg
		elif opt in ("-o", "--outputfile"):
			outputfile = arg

	execution_path = os.getcwd()

	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel(detection_speed="fast")

	# Update the parameters to choose which objects are detected.
	'''
	Possible object types:
		person, bicycle, car, motorcycle, airplane,
        bus, train, truck, boat, traffic_light, fire_hydrant, stop_sign,
        parking_meter, bench, bird, cat, dog, horse, sheep, cow, elephant, bear, zebra,
        giraffe, backpack, umbrella, handbag, tie, suitcase, frisbee, skis, snowboard,
        sports_ball, kite, baseball_bat, baseball_glove, skateboard, surfboard, tennis_racket,
        bottle, wine_glass, cup, fork, knife, spoon, bowl, banana, apple, sandwich, orange,
        broccoli, carrot, hot_dog, pizza, donot, cake, chair, couch, potted_plant, bed,
        dining_table, toilet, tv, laptop, mouse, remote, keyboard, cell_phone, microwave,
        oven, toaster, sink, refrigerator, book, clock, vase, scissors, teddy_bear, hair_dryer, toothbrush
	'''
	custom_objects = detector.CustomObjects(car=True, person=True)

	detections = detector.detectCustomObjectsFromImage(
		custom_objects=custom_objects,
		input_image=inputfile,
		output_image_path=outputfile,
	)

if __name__ == "__main__":
	main(sys.argv[1:])
