import os
import csv
import shutil


with open('train-gt-mod.csv') as csvfile:
    	readCSV = csv.reader(csvfile, delimiter=',')

	print("Running...")    	

    	for row in readCSV:
        	img = 'boneage-train-dataset/'+row[0]+'.png'
		if row[2] == 'False':
			local = 'Female/' + str(row[1]) + '/'  
			if not os.path.exists(local):
        	        	os.makedirs(local)
			shutil.copy(img, local)
		if row[2] == 'True':
			local = 'Male/' + str(row[1]) + '/' 
			if not os.path.exists(local):
        	        	os.makedirs(local)
			shutil.copy(img, local)
            
print("The End")

