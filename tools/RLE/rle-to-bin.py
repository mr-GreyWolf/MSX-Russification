#!/usr/bin/python3
#coding=utf8
import sys

if __name__=='__main__':
	if len(sys.argv)==3:
		file_rle=sys.argv[1] # исходный файл (RLE)
		file_bin=sys.argv[2] # конечный файл (Binary)
		quantity_limit=255   # RLE 8 бит 
	elif len(sys.argv)==4 and sys.argv[3]=='16':
		file_rle=sys.argv[1] # исходный файл (RLE)
		file_bin=sys.argv[2] # конечный файл (Binary)
		quantity_limit=65535 # RLE 16 бит 
	else:
		print ('Параметры заданы не правильно!')
		print ('Пример: '+sys.argv[0]+' test.rle test.bin 16')
		sys.exit(1)

data_out=b''
value=b''
file_rle=open(file_rle,'rb')
data_in=file_rle.read(1)

while data_in:
	# Значение
	value=data_in
	# Количество 
	if quantity_limit<=255:
		data_in=file_rle.read(1)
	elif quantity_limit<=65535:
		data_in=file_rle.read(2)
	n=int.from_bytes(data_in, byteorder='big')
	while 0 < n:
		n=n-1
		data_out=data_out+value
	# Читаем входной файл (следующий байт)
	data_in=file_rle.read(1)

file_bin=open(file_bin,'wb')
file_bin.write(data_out)

file_bin.close()
file_rle.close()
