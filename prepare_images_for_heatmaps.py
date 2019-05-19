# create 3 folders: temporary, temporary_negative, temporary_positive
import os 
from shutil import copy, copyfile, rmtree, copytree
from csv import reader
from random import sample


def solve(tpos, tneg, vpos, vneg):
	for kind in ['humerus', 'elbow', 'finger', 'wrist', 'hand', 'forearm', 'shoulder']:
		solve_helper(kind, 'train', tpos, tneg)
		solve_helper(kind, 'valid', vpos, vneg)
		
def solve_helper(kind, torv, positive_samples, negative_samples):
	add_to_temp_np(kind, torv, positive_samples, negative_samples)
	src1 = 'C:\\Users\\Admin\\Desktop\\python\\temporary_positive'
	src2 = 'C:\\Users\\Admin\\Desktop\\python\\temporary_negative'
	dst  = 'C:\\Users\\Admin\\Desktop\\python\\MURA-v1.1\\heatmaps\\'+ kind + '\\images'
	copy_and_clear(src1, dst)
	copy_and_clear(src2, dst)
			
def copy_and_clear(src, dst):
	for fname in os.listdir(src):
		copy(src + '\\' + fname, dst)
		os.remove(src + '\\' + fname)

def add_to_temp_np(kind, torv, positive_samples, negative_samples):
	os.chdir('C:\\Users\\Admin\\Desktop\\python\\MURA-v1.1\\'+torv+'_specific_paths')
	file = open(torv+'_image_paths_'+kind+'.csv')
	readCSV = reader(file)
	positive_paths = []
	negative_paths = []
	source = 'C:\\Users\\Admin\\Desktop\\python\\'
	for row in readCSV:
		if 'positive' in row[0]:
			positive_paths.append(row[0])
		else:
			negative_paths.append(row[0])
			
	positive_paths = sample(positive_paths, positive_samples)
	negative_paths = sample(negative_paths, negative_samples)
	add_helper(kind, 'positive', torv, positive_paths)
	add_helper(kind, 'negative', torv, negative_paths)
	
def add_helper(kind, norp, torv, paths):
	fdst = 'C:\\Users\\Admin\\Desktop\\python\\temporary_'+norp
	dst  = 'C:\\Users\\Admin\\Desktop\\python\\temporary'
	source = 'C:\\Users\\Admin\\Desktop\\python\\'
	i = 1
	for src in paths:
		copy(source + src, dst)
		for fname in os.listdir(dst):
			new_name = kind+'_'+torv + '_' + norp + str(i) + '.png'
			os.rename( dst+'\\'+fname, dst+'\\'+new_name)
		copy(dst+'\\'+new_name, fdst)
		os.remove(dst+'\\'+new_name)
		i+=1
