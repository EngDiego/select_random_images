import os
import shutil
import random

#Pasta a ser escolhida as fotos aleatorizamente
input_dir="C:\\Users\\layds\\OneDrive\\Imagens\\Imagens\\Input"

#Pasta destino onde serão copiadas as images
output_dir="C:\\Users\\layds\\OneDrive\\Imagens\\Imagens\\Output"

#Quantidade de imagens a serem copiadas
qtda= 1000

file_list = [os.path.join(path, name) for path, subdirs, files in os.walk(input_dir) for name in files]
#file_list

select_files = random.sample(file_list, qtda)# randomly select 2 pictures from each category folder
#select_files

for foto_n in range(len(select_files)):
    shutil.copy2(select_files[foto_n], output_dir)
print("fotos aleatorias copiadas")