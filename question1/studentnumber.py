#!/usr/bin/env python3

import numpy as np
import random

number = "7654321"
mid_number = int(number[3])


def create_column_contain_Consecutive(COLUMN_START,COLUMN_END,CONSACITVE_VALUE):
	#generate column contain cosacitve values in random position:
	start = int(COLUMN_START)
	end = int(COLUMN_END) + 1
	student_num_digit = int(CONSACITVE_VALUE)
	random_start  = random.randint(start,(start+student_num_digit)-1)
	first = np.arange(start,random_start)
	mid = np.array([[student_num_digit]*student_num_digit])
	last = np.arange(random_start+student_num_digit,end)
	return np.concatenate((first,mid,last), axis=None)


def test_even_odd(mid_number):
	#global MID_NUM
	if (mid_number % 2) == 0:
		return 'even'
	else:
		return 'odd'


def Distribution_digits_to_columns(MID_NUM):
	global a0
	a0 = np.arange(1,16)
	if MID_NUM  == 'even':
		COLUMN_START = 0
		COSACTIVE_INDEX = 0
		for ARRAY_COLUMNS in range(1,15,2):
			COLUMN_START = (ARRAY_COLUMNS - 1) * 14
			COLUMN_END = COLUMN_START + 13
			globals()[f'a{ARRAY_COLUMNS}'] = np.arange(COLUMN_START,COLUMN_END+1)
			if int(number[COSACTIVE_INDEX]) != 0:
				globals()[f'a{ARRAY_COLUMNS+1}'] = create_column_contain_Consecutive(COLUMN_START+14,COLUMN_END+14,number[COSACTIVE_INDEX])
			elif int(number[COSACTIVE_INDEX]) == 0:
				globals()[f'a{ARRAY_COLUMNS+1}'] = np.arange(COLUMN_START+14,COLUMN_END+14+1)
			COSACTIVE_INDEX = COSACTIVE_INDEX + 1
	elif MID_NUM  == 'odd':
		COLUMN_START = 0
		COSACTIVE_INDEX = 0
		for ARRAY_COLUMNS in range(1,15,2):
			COLUMN_START = (ARRAY_COLUMNS - 1) * 14
			COLUMN_END = COLUMN_START + 13
			if int(number[COSACTIVE_INDEX]) != 0:
				globals()[f'a{ARRAY_COLUMNS}'] = create_column_contain_Consecutive(COLUMN_START,COLUMN_END,number[COSACTIVE_INDEX])
			elif int(number[COSACTIVE_INDEX]) == 0:
				globals()[f'a{ARRAY_COLUMNS}'] = np.arange(COLUMN_START,COLUMN_END+1)
			globals()[f'a{ARRAY_COLUMNS+1}'] = np.arange(COLUMN_START+14,COLUMN_END+14+1)
			COSACTIVE_INDEX = COSACTIVE_INDEX + 1

def asign_columns_to_create_matrix():
	global matrix
	matrix = np.arange(1, 211).reshape(14,15)
	matrix[:,0] = a0[:14]
	for i in range(1,15):
		matrix[:,i] = globals()[f'a{i}']	 

def save_to_text():
	with open(f"studentnumber_<r{number}>.txt", "wb") as f:
		np.savetxt(f,matrix.astype(int),fmt='%i')
		f.write(b'15')



if __name__ == "__main__":
	Distribution_digits_to_columns(test_even_odd(mid_number))
	asign_columns_to_create_matrix()
	save_to_text()











