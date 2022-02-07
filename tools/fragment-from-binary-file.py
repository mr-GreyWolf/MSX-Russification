#!/usr/bin/python
# coding=utf8
import binascii,sys

if __name__=='__main__':
	if len(sys.argv)==5:
		file_i=sys.argv[1]		# файл
		file_o=sys.argv[2]		# фрагмент файла
		offset=sys.argv[3]		# сдвиг от начала файла (в шестнадцатиричной системе исчисления)
		length=int(sys.argv[4])	# длина (количество байт)
	else:
		print ('Не заданы параметры!')
		print ('Пример: '+sys.argv[0]+' file.bin fragment.bin AB01 128')
		sys.exit(1)

file_in=open(file_i,'rb')
offset = (int(offset,base=16)-1)
if offset < 0:
	offset = 0

file_in.seek(int(offset))
data_out=b''

while length:
	data_out=data_out+file_in.read(1)
	length=length-1

file_out=open(file_o,'wb')
file_out.write(data_out)

file_out.close()
file_in.close()
