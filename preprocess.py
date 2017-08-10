import PIL.Image
import os
import cv2 as cv2
import csv
import numpy as np



print("Listando arquivos...")
arqs = os.listdir("./boneage-train-dataset/")
print("Arquivos listados.")

rows,cols = 300,300

M = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(30):
    M[i] = cv2.getRotationMatrix2D((cols/2,rows/2),(i-15),1)

much_data = []
conta = 0
bloco = 0
divide = 0

with open('train-gt-mod.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        
        img = cv2.imread("D:/boneage-train-dataset-win/boneage-train-dataset/"+row[0]+".png")
        img = cv2.resize(img, (rows, cols))
        cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        
        
        conta = conta + 1
        divide = divide + 1
        
        if divide < 8:
            grupo = 'treino'
        elif divide == 8:
            grupo = 'valida'
        elif divide > 8:
            grupo = 'teste'
            if divide == 10:
                divide = 0
        
        print(conta)
        
        for i, m in enumerate(M):
            #print(row[0],row[1],row[2],i)
            dst = cv2.warpAffine(img,m,(cols,rows))
            
            local = "C:/boneage-train-dataset-win/Preprocessed/" + str(row[2]) + '/' + grupo + '/' + str(row[1]) + '/'

            if not os.path.exists(local):
                os.makedirs(local)
                
            local = local + str(row[0]) + '_' + str(i) + '.png'
            
            cv2.imwrite(local, dst)
            
            #cv2.imshow('dst_rt', dst)
            #much_data.append([dst,row[1],row[2]])
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()

#        if conta == 100:
#            conta = 0
#            bloco = bloco + 1
#            print("Bloco: " + str(bloco))
#            print(" ")
#            print(" ")
#            print(" ")
#            print(" ")
#            print(" ")
            
#            np.save('BoneAgeNormRot' + str(bloco) + '.npy', much_data)
#            much_data = []

print("Finalizado.")

    #image.show()

