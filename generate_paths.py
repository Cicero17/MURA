import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import io
import os
import csv
from PIL import Image

source = os.getcwd()
os.chdir('D:\\python\MURA-v1.1') # instead of 'D:\\python\MURA-v1.1' one can write source+ '\MURA-v1.1 -- it doesn't work well with imp.reload()

shoulder_imgs = []
humerus_imgs = []
finger_imgs = []
elbow_imgs = []
wrist_imgs = []
forearm_imgs = []
hand_imgs = []


class image:
	def __init__(self, source, path):
		self.array_rep = np.array(Image.open(source+'\\'+path))
		self.value = 0
		if 'positive' in path:
			self.value = 1
			
	
f = open('valid_image_paths.csv')
readCSV = csv.reader(f)

os.chdir("valid_specific_paths")

f_elbow = open('valid_image_paths_elbow.csv','w' ,newline='')
f_forearm = open('valid_image_paths_forearm.csv','w',newline='')
f_finger = open('valid_image_paths_finger.csv','w',newline='')
f_hand = open('valid_image_paths_hand.csv','w',newline='')
f_humerus = open('valid_image_paths_humerus.csv','w',newline='')
f_shoulder = open('valid_image_paths_shoulder.csv','w',newline='')
f_wrist = open('valid_image_paths_wrist.csv','w',newline='')

g_elbow = csv.writer(f_elbow)
g_finger = csv.writer(f_finger)
g_forearm = csv.writer(f_forearm)
g_humerus = csv.writer(f_humerus)
g_shoulder = csv.writer(f_shoulder)
g_wrist = csv.writer(f_wrist)
g_hand = csv.writer(f_hand)



for row in readCSV:
	if 'SHOULDER' in row[0]:
		g_shoulder.writerow([row[0]])
	elif 'HUMERUS' in row[0]:
		g_humerus.writerow([row[0]])
	elif 'FINGER' in row[0]:
		g_finger.writerow([row[0]])
	elif 'ELBOW' in row[0]:
		g_elbow.writerow([row[0]])
	elif 'WRIST' in row[0]:
		g_wrist.writerow([row[0]])
	elif 'FOREARM' in row[0]:
		g_forearm.writerow([row[0]])
	elif 'HAND' in row[0]:
		g_hand.writerow([row[0]])

f.close()

f_elbow.close()
f_humerus.close()
f_hand.close()
f_forearm.close()
f_wrist.close()
f_shoulder.close()
f_finger.close()	


