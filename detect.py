#!/usr/bin/env python

from imageai.Detection import ObjectDetection
import os
import urllib.request
import datetime

def main():
	# Current working directory.
	execution_path = os.getcwd()

	# Initialize ObjectDetection() class.
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath("models/resnet50_coco_best_v2.0.1.h5")
	detector.loadModel(detection_speed="fast")

	# Select which object types will be detected.
	custom_objects = detector.CustomObjects(person=True)

	# Download file from any URL.
	url = "https://si.wsj.net/public/resources/images/BN-RT702_0124ch_H_20170124110410.jpg"
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	file_in = "images/in/" + str(now) + '.jpg'
	urllib.request.urlretrieve(url, file_in)

	# Detect objects and create an output file with squares around objects.
	detections = detector.detectCustomObjectsFromImage(
		custom_objects=custom_objects,
		input_image=file_in,
		output_image_path="images/out/output.jpg",
		minimum_percentage_probability=27
	)

	# Delete the input file after detecting objects.
	os.remove(file_in)

	# Write the number of detected objects to a text file.
	with open('output.txt', 'w+') as f:
		f.write("Detections: {}".format(str(len(detections))))

if __name__ == "__main__":
	main()