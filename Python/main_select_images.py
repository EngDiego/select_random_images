import os
import shutil
import random

#Pasta a ser escolhida as fotos aleatorizamente
input_dir="E:\\OneDrive\\Imagens"
#input_dir="C:\\Users\\layds\\OneDrive\\Imagens\\Imagens Aleatorias"

#Pasta destino onde serão copiadas as images
output_dir="C:\\imagens_importadas\\Laydsmar"

#Quantidade de imagens a serem copiadas
qtda= 2000

print("Etapa  1 - Mapeamento de imagens")
file_list = [os.path.join(path, name) for path, subdirs, files in os.walk(input_dir) for name in files]
#file_list

print("Etapa  1.1- Qtda de imagens mapeadas:"+str(len(file_list)))


included_extensions = ['jpg','JPG','jpeg','JPEG','png','PNG', 'gif','GIF','bmp','BMP']
file_list_filter = [fn for fn in file_list
              if any(fn.endswith(ext) for ext in included_extensions)]
#print(file_list_filter)

print("Etapa  1.2- Qtda de imagens que sao jpeg jpg png:"+str(len(file_list_filter)))


print("Etapa  2 - Rondomizando fotos")
select_files = random.sample(file_list_filter, qtda)# randomly select 2 pictures from each category folder
#select_files


print("Etapa  3 - Copiando Fotos")
for foto_n in range(len(select_files)):
    shutil.copy2(select_files[foto_n], output_dir)

print("Etapa  4 - FIM")
