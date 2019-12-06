#!/usr/bin/python
# coding=utf8
import binascii,sys

if __name__=='__main__':
	if len(sys.argv)== 5:
		file_o=sys.argv[1]		# исходный файл в который записывается фрагмент (файл открывается только на чтение, скрипт создаёт новый файл добавляя к имени исходного суффикс _new)
		file_i=sys.argv[2]		# фрагмент
		offset=sys.argv[3]		# сдвиг от начала файла (в шестнадцатиричной системе исчисления)
		length=int(sys.argv[4])	# длина (количество байт)
	else:
		print ('Не заданы параметры!')
		print ('Пример: '+sys.argv[0]+' file.bin fragment.bin AB01 128')
		sys.exit(1)

new_file_prefix='_new'
offset=int(offset,base=16)-1
i=0
data_out_new=''
file_in=open(file_i, 'rb')
file_out=open(file_o, 'rb')

data_out=file_out.read(1)
while data_out:
	if i>offset and i<(offset+length) :
		data_in=file_in.read(1)
		data_out_new=data_out_new+data_in
		data_out=file_out.read(1)
	else:
		data_out_new=data_out_new+data_out
		data_out=file_out.read(1)
	i=i+1

file_out_new=open(file_o+new_file_prefix,'wb')
file_out_new.write(data_out_new)

file_out_new.close()
file_out.close()
file_in.close()
