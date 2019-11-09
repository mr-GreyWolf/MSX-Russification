#!/usr/bin/python
# coding=utf8
import binascii, sys

if __name__ == '__main__':
    if len (sys.argv) == 3:
	file_i = sys.argv[1]		# исходный файл
	file_o = sys.argv[2]		# файл с таблицей
	fragment = [ ["DA5",288], ["1033",40] ]	# фрагменты (адрес, длина) для MSX 1 и 2
    elif len (sys.argv) == 4 and sys.argv[3] == '2+':
        file_i = sys.argv[1]		# исходный файл
        file_o = sys.argv[2]		# файл с таблицей
        fragment = [ ["DA5",288], ["0FF8",40] ]	# фрагменты (адрес, длина) для MSX 2+
    else:
        print ('Не заданы параметры!')
	print ('Пример: ' + sys.argv[0] + ' file.bin table.txt' + ' [2+]')
	sys.exit (1)

# Переменные
table = []; 		# таблица
sep=" "			# разделитель
line_end = "\r\n"	# конец строки

# Чтение исходного файла
file_in = open(file_i, 'rb')
data_out = ''
for f in [0,1]:
    offset = fragment [f] [0]
    length = fragment [f] [1]
    file_in.seek( int(offset, base = 16) )
    data_in = file_in.read(1)
    while length:
	code_hex = binascii.b2a_hex(data_in)
	code_hex = code_hex.upper()
	table.append(code_hex);
	length = length-1
	data_in = file_in.read(1)
file_in.close()

# Таблица 1
for i in range (48):
    i_hex = '{0:x}'.format(int(i))
    if i < 16:
	i_hex = "0"+i_hex
    i_hex = i_hex.upper()
    i_hex = "0x"+i_hex
    data_out = data_out + i_hex + sep
    for t in [0,1,2,3,4,5]:
	n = i+(t*48)
	if t == 5:
	    data_out = data_out + table[n] + line_end
	else:
		data_out = data_out + table[n] + sep
# Таблица 2
for i in range (40):
    i_hex = '{0:x}'.format(int(i+48))
    i_hex = i_hex.upper()
    i_hex = "0x"+i_hex
    data_out = data_out + i_hex + sep
    data_out = data_out + table[int(288+i)] + line_end
# Запись в файл
file_out = open(file_o, 'wb')
file_out.write(data_out)
file_out.close()
