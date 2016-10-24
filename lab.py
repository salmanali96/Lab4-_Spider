import os
import sys
from socket import *
import pickle
from sys import exit
import time
import datetime
import mmap
import test

checkpath = "";

filepath = '/home'     	#specifying the root
words_dict = dict()
word_path = dict()
for root,dirs,files in os.walk(filepath):
	
	for file in files:
		if file.endswith('.txt'): 		#files ending with .txt
			#print file
			path1 = os.path.join(root, file)
                        #print path1
			with open (path1, "r") as myfile:
				data=myfile.read()
				#print data
				word_path[path1]  = file 			#storing the filename        
				words_dict[path1] = data			#storing its path
				
				checkpath = words_dict[path1]


Word = raw_input('Enter the Word you want to find:')			#getting the input word to find

count =0;
for k,v in word_path.items():
	#print v;
        f = open(k)
	s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)					

	if s.find(Word) != -1:						#finding the word in the file
    		filepath = "The word is found in the file: " + word_path[k]  + " and its path is: " + str(k); 
		print filepath;
	
	elif v == Word:							#if the word is the text file
		filepath = "The word is found in the file: " + word_path[k]  + " and its path is: " + str(k); 
		print filepath;
		
    



   



							

                                 
							
						

