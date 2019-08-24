#!/usr/bin/python
# coding=utf8
import binascii, sys

if __name__ == '__main__':
    if len (sys.argv) == 3:
	file_i = sys.argv[1]		# исходный файл
	file_o = sys.argv[2]		# имя файл (без расширения)
    else:
        print ('Не заданы параметры!')
	print ('Пример: ' + sys.argv[0] + ' table.txt table')
	sys.exit (1)
# Переменные
fragment = [ ['0DA5',288], ['1033',40]]	# фрагменты (адрес, длина)
sep=" "			# разделитель
line_end = '\r\n'	# конец строки
basic_line_end = '\r'	# конец строки
ext_file_basic = '.bas'
ext_file_bin = '.bin'

# Названия специальных символов для таблицы 2
def hex_to_symbol (hex):
    hex_name = {
	'00':'NULL',
	'01':'GRAPH',
	'02':'CTRL+B',
	'03':'CTRL+C',
	'04':'CTRL+D',
	'05':'CTRL+E',
	'06':'CTRL+F',
	'07':'BEEP',
	'08':'BS',
	'09':'TAB',
	'0a':'LF',
	'0b':'HOME',
	'0c':'CLS',
	'0d':'RET',
	'0e':'CTRL+N',
	'0f':'CTRL+O',
	'10':'CTRL+P',
	'11':'CTRL+Q',
	'12':'INS',
	'13':'CTRL+S',
	'14':'CTRL+T',
	'15':'CTRL+U',
	'16':'CTRL+V',
	'17':'CTRL+W',
	'18':'SEL',
	'19':'CTRL+Y',
	'1a':'CTRL+Z',
	'1b':'ESC',
	'1c':'Right',
	'1d':'Left',
	'1e':'Up',
	'1f':'Down',
	'20':'SPC',
	'7f':'DEL'
    }
    if hex in hex_name:
	hex_to_symbol = (hex_name[hex])+'"'
    else:
	hex_to_symbol='"+chr$('+str(int(str(hex),16))+')'
    return hex_to_symbol
# Чтение текстового файла
file_in = open(file_i)
data_out = ''
table1 = [];
for i in range ((fragment [0] [1])+1):table1.append(0);
table2 = [];
for i in range ((fragment [1] [1])+1):table2.append(0);
basic_l = ''
n=0
for line in file_in.readlines():
    n=n+1
    l = line.replace('\r','').replace('\n','').split(sep)
    l0 = l[0].replace('0x','') # номер клавиши в шестнадцатиричной системе
    l0_dec = int(l0, 16) # номер клавиши в десятичной системе
    if l0_dec < 48:
	# Таблица, часть 1
	if l0_dec > 23:
	    # Колонка 2
	    basic_l = str(l0_dec + 1) +' locate 17,'+ str(l0_dec - 24) +': ? "'+ str(l0) +'"'
	else:
	    # Колонка 1
	    basic_l = str(l0_dec + 1) +' locate 0,'+ str(l0_dec) +': ? "' + str(l0) + '"'
	for q in [1,2,3,4,5,6]:
		l_dec = int(l[q],16)	# Десятичный код символа
		table1[int(n+(q*48)-48)]=l[q]
		if l_dec <= 31:
		    # "Оранжевые" символы
		    lq = 'chr$(1)+'+'chr$(' + str(l_dec + 64) + ')'
		else:
		    lq = 'chr$(' + str(l_dec) + ')'
		basic_l = basic_l + '+" "+' + lq
	l0 = str('0x'+l0)
    else:
	# Таблица, часть 2
	l0 = str('0x' + l0)
	l1 = str(int(l[1],16)) # Код символа в режиме 1
	table2[n-48] = l[1]
	name = hex_to_symbol(l[1].lower()) # Код символа в режиме 1
	if l0_dec < 68:
	    # Колонка 1
	    basic_l = (str(l0_dec + 10) + ' locate 0,'+ str(l0_dec - 48) + ': ? "' + l0 + ' ' + name)
	else:
	    # Колонка 2
	    basic_l = (str(l0_dec + 10) + ' locate 17,'+ str(l0_dec - 68) + ': ? "' + l0 + ' ' + name)
    # Формирование программы
    data_out = data_out + basic_l + ';' + basic_line_end
# Дополнительные строки программы
data_out = data_out + \
    '0 color 1,15,15:screen 1:key off:width 32' + basic_line_end + \
    '50 if inkey$="" then 50' + basic_line_end + \
    '51 cls:locate 0,0:print' + basic_line_end + \
    '100 if inkey$="" then 100' + basic_line_end + \
    '101 goto 0' + basic_line_end + \
    '\x1A'
# Запись программы в файл
file_out = open(file_o + ext_file_basic, 'wb')
file_out.write(data_out)
file_out.close()
# Вывод содержимого таблиц
print 'Для изменения исходного файла используйте команды:'
for f in [0,1]:
    offset = fragment [f] [0]
    length = fragment [f] [1]
    data_out = ''
    for n in range (1,length+1):
	var_name = 'table'+str(f+1)
	code_hex = globals()[var_name][n]
	code_bin = binascii.unhexlify(code_hex)
	data_out = data_out + code_bin
    # Запись в файл
    file_out_name = file_o + '_' + offset + '-' + str(length) + ext_file_bin
    print '../tools/fragment-to-binary-file.py ' + file_out_name + ' ' + str(offset) + ' ' + str(length)
    file_out = open(file_out_name, 'wb')
    file_out.write(data_out)
    file_out.close()
sys.exit (0)
