#!/usr/bin/python
# coding=utf8
import binascii,sys

if __name__=='__main__':
	if len(sys.argv)==3:
		file_i=sys.argv[1] # текстовый файл шрифта
		file_o=sys.argv[2] # бинарный файл шрифта
	else:
		print ('Не заданы параметры!')
		print ('Пример: '+sys.argv[0]+' font.txt font')
		sys.exit(1)

# Переменные
offset='1BBF'	# смещение
length=2048		# длина
replace_0='.' 	# замена для 0
replace_1='@'	# замена для 1
ext_file_bin='.bin' # расширение бинарного файла

# Чтение исходного файла
file_in=open(file_i,'r')
data_out=b''

for data_in in file_in:
	line_str=data_in.strip()
	if line_str.find(replace_0)==1 or line_str.find(replace_1)==1:
		line_str=line_str.replace(replace_0,'0')
		line_str=line_str.replace(replace_1,'1')
		line_str=line_str[1:9]
		code_dec=int(line_str, 2)
		code_hex=(hex(code_dec))[2:]
		if code_dec<16:
			code_hex='0'+code_hex
		data_out=data_out+binascii.unhexlify(code_hex)
# Запись в файл
file_out_name=file_o+'_'+offset+'-'+str(length)+ext_file_bin

# Запись программы в файл
file_out=open(file_out_name,'wb')
file_out.write(data_out)
file_out.close()

print ('Для изменения исходного файла используйте команду:')
print ('../tools/fragment-to-binary-file.py file.bin ' + file_out_name + ' ' + str(offset) + ' ' + str(length))
