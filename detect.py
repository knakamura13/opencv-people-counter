#!/usr/bin/env python

import os
import cv2
import time
import datetime
import urllib.request
from PIL import Image
from imageai.Detection import ObjectDetection
import json
import requests

# Prepare video capture on camera #0.
cap = cv2.VideoCapture(0)
cv2.namedWindow("PyCam")

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

	# Initalize counter for naming new files.
	img_counter = 0

	file_to_delete = ""

	start_time = 0

	while(True):		
		# Capture the current frame.
		ret, frame = cap.read()

		# Display the resulting frame.
		cv2.imshow('frame',frame)

		# Quit program on Escape key press.
		k = cv2.waitKey(1)
		if k % 256 == 27:
			break

		if time.time() - start_time > 5:
			# Record the time for this specific frame capture.
			current_time = str(datetime.datetime.now())

			# Define the current input file and output file to run the detector script on.
			inputfile = "images/in/input_frame_{}.png".format(img_counter)
			outputfile = "images/out/output_frame_{}.png".format(img_counter)

			# Increment img_counter for naming image files.
			img_counter += 1

			# Create a new image file from the current frame.
			cv2.imwrite(inputfile, frame)

			# Detect objects and create an output file with squares around objects.
			detections = detector.detectCustomObjectsFromImage(
				custom_objects=custom_objects,
				input_image=inputfile,
				output_image_path=outputfile,
				minimum_percentage_probability=40
			)

			# Get the length of the detections npArray as a String.
			num_detections = str(len(detections))

			# Pepare JSON data to be sent to the API.
			data_json = json.dumps({
				"people": num_detections,
				"time" : current_time
			})

			# POST the data to the API.
			response = requests.post("http://127.0.0.1:5000/", data=data_json, headers={'Content-type': 'application/json'})

			# Delete the input file.
			os.remove(inputfile)

			# Delete the previous output file.
			try:
				os.remove(file_to_delete)
			except:
				# Do nothing.
				pass

			# Set the next file to be deleted to the current output file.
			file_to_delete = outputfile

			# Open output image on user's device.
			Image.open(outputfile).show()
			
			start_time = time.time()

		# Sleep the CPU for 0.2 seconds to preserve energy.
		time.sleep(0.2)

if __name__ == "__main__":
	main()