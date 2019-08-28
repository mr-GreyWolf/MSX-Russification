#!/usr/bin/python
# coding=utf8
import binascii, sys

if __name__ == '__main__':
    if len (sys.argv) == 3:
	file_i = sys.argv[1]		# исходный файл
	file_o = sys.argv[2]		# файл шрифта
    else:
        print ('Не заданы параметры!')
	print ('Пример: ' + sys.argv[0] + ' file.bin font.txt')
	sys.exit (1)

# Переменные
offset = "1BBF"		# смещение
length = 2048		# длина
table = []; 		# таблица
line_end = "\r\n"	# конец строки
replace_0 = ' ' # замена для 0
replace_1 = '@' # замена для 1

# Чтение исходного файла
file_in = open(file_i, 'rb')
data_out = ''

file_in.seek( int(offset, base = 16) )
data_in = file_in.read(1)
while length:
    code_hex = binascii.b2a_hex(data_in)
    code_hex = code_hex.upper()
    table.append(code_hex);

    length = length-1
    data_in = file_in.read(1)
file_in.close()

# Шрифт
s=0
for i in range (0,2047,8):
    i_hex = ('{0:x}'.format(int(s))).upper()
    s_hex = ('{0:x}'.format(int(s*8))).upper()
    if s <= 16:
	i_hex = '0x0' + i_hex
    else:
	i_hex = '0x' + i_hex
    data_out =  data_out + 'Смещение: '+ '0x' + str(s_hex)+ ' ('  + str (s*8)+ ')   Код: ' + i_hex + ' (' + str(s) + ')' + line_end + \
    '_12345678' + line_end
    for t in range (0,8):
	string_of_pixels=((bin(int(table[i+t], 16))[2:].zfill(8)).replace('0', replace_0)).replace('1', replace_1)
	data_out = data_out + str (t+1) + string_of_pixels + line_end
    data_out =  data_out + line_end
    s=s+1
# Запись в файл
file_out = open(file_o, 'wb')
file_out.write(data_out)
file_out.close()
