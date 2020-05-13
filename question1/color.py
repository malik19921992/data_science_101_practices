#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np
import time

#global vars:
A = {}
number = "8045250"

def read_array_from_text_file(number):
	global student_number_array
	with open(f'studentnumber_<r{number}>.txt', 'rb') as infile:
		for NUM in range(0,15):
			g = infile.readline().decode('utf-8')
			A[NUM] = g.strip().split()[0:15]
	student_number_array = np.vstack([A[i] for i in range(0,14)])
	#change numbers inside array to integers 
	student_number_array = np.array(student_number_array,dtype=np.int16)


def duplicated_index(arr, num):
	duplicated = []
	for i, x in enumerate(arr):
		if x == num:
			duplicated.append(i)
	return duplicated


def change_duplicated_to_200(COLUMN,duplicated):
	student_number_array
	for NUM in duplicated:
		student_number_array[NUM,COLUMN] = -80


def change_duplicated_fields_color():
	global student_number_array

	if test_even_odd(int(number[3])) == 'odd':
		COLUMN_NUM = 1
	if test_even_odd(int(number[3])) == 'even':
		COLUMN_NUM = 2

	NUMBER_INDEX = 0
	for COLUMN_NUM in range(COLUMN_NUM,15,2):
		change_duplicated_to_200(COLUMN=COLUMN_NUM,duplicated=duplicated_index(student_number_array[:,COLUMN_NUM],int(number[NUMBER_INDEX])))
		NUMBER_INDEX = NUMBER_INDEX + 1 


def test_even_odd(mid_number):
	global MID_NUM
	if (mid_number % 2) == 0:
		return 'even'
	else:
		return 'odd'

def matplotlib_save_image():
	# plt.rcParams['toolbar'] = 'None' 
	time.sleep(0.6)
	plt.axis("off")
	fig = plt.imshow(student_number_array,interpolation='nearest')
	fig.axes.get_xaxis().set_visible(False)
	fig.axes.get_yaxis().set_visible(False)
	plt.savefig(f'<r{number}>image',bbox_inches='tight', pad_inches=0, format='jpg', dpi=1200)


if __name__ == '__main__':
	read_array_from_text_file(number)
	change_duplicated_fields_color()
	matplotlib_save_image()



