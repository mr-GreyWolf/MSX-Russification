#!/usr/bin/python
#coding=utf8
import binascii
import sys

if __name__ == '__main__':
    if len (sys.argv) == 3:
	file_msx = sys.argv[1]     # исходный файл (MSX)
	file_utf = sys.argv[2]     # конечный файл (UTF-8)
    else:
        print ('Не заданы файлы!')
	print ('Пример: ./msx_russian-utf8.py test.msx test.txt')
	sys.exit (1)

def hex_to_utf (hex):
    msx_to_utf = {
	'80':'e29681',		# 80 Нижняя одна восьмая блока U+2581
	'81':'e2969a',		# 81 Квадрант сверху слева и снизу справа U+259A
	'82':'e29687',		# 82 Нижние семь восьмых блока U+2587
	'83':'e29694',		# 83 Верхняя одна восьмая блока U+2594
	'84':'e28183',		# 84 Дефис маркер списка U+2043
	'85':'',		# 85
	'86':'e2968f',		# 86 Левая одна восьмая блока U+258F
	'87':'e2969e',		# 87 Квадрант сверху справа и снизу слева U+259E
	'88':'e2968a',		# 88 Левые три четверти блока U+258A
	'89':'e29695',		# 89 Правая одна восьмая блока U+2595
	'8b':'e296a8',		# 8B Квадрат с верхним правым и нижним левым заполнением U+25A8
	'8c':'e296a7',		# 8C Квадрат с верхним левым и нижним правым заполнением U+25A7
	'8d':'e296bc',		# 8D Чёрный треугольник с вершиной вниз U+25BC
	'8e':'e296b2',		# 8E Чёрный треугольник с вершиной вверх U+25B2
	'8f':'e296b6',		# 8F Чёрный треугольник с вершиной направо плей, проигрывать, старт U+25B6
	'90':'e29780',		# 90 Черный треугольник с вершиной налево U+25C0
	'91':'e2a797',		# 91 Закрашенные песочные часы U+29D7
	'92':'e2a793',		# 92 Закрашенная бабочка U+29D3
	'93':'e29698',		# 93 Квадрант сверху слева U+2598
	'94':'e29697',		# 94 Квадрант снизу справа U+2597
	'95':'e2969D',		# 95 Квадрант сверху справа U+259D
	'96':'e29696',		# 96 Квадрант снизу слева U+2596
	'97':'e29691',		# 97 Легкое затемнение U+2591
	'98':'ce94',		# 98 Греческая заглавная буква дельта U+0394
	'99':'e289a0',		# 99 Не равный U+2260
	'9a':'cF89',		# 9A Греческая строчная буква омега U+03C9
	'9b':'e29688',		# 9B Полный блок U+2588
	'9c':'e29684',		# 9C Нижняя половина блока U+2584
	'9d':'e2968c',		# 9D Левая половина блока U+258C
	'9e':'e29690',		# 9E Правая половина блока U+2590
	'9f':'e29680',		# 9F Верхняя половина блока U+2580
	'a0':'ceb1',		# A0 Греческая строчная буква альфа U+03B1
	'a1':'ceb2',		# A1 Греческая строчная буква бета U+03B2
	'a2':'ce93',		# A2 Греческая заглавная буква гамма U+0393
	'a3':'cf80',		# A3 Греческая строчная буква пи U+03C0
	'a4':'e28891',		# A4 N-ичное суммирование U+2211
	'a5':'cf83',		# A5 Греческая строчная буква сигма U+03C3
	'a6':'cebc',		# A6 Греческая строчная буква мю U+03BC
	'a7':'ceb3',		# A7 Греческая строчная буква гамма U+03B3
	'a8':'cea6',		# A8 Греческая заглавная буква фи U+03A6
	'a9':'e29fa0',		# A9 Ромбовидная фигура, разделённая горизонтальной линией U+27E0
	'aa':'cea9',		# AA Греческая заглавная буква омега U+03A9
	'ab':'ceb4',		# AB Греческая строчная буква дельта U+03B4
	'ac':'e2889e',		# AC Знак бесконечности U+221E
	'ad':'f09d9c99',	# AD Математическая курсивная фи (символ U+1D719
	'ae':'e28888',		# AE Принадлежит множеству U+2208
	'af':'e28b82',		# AF N-ичное пересечение U+22C2
	'b0':'e289a1',		# B0 Идентичный, тождество (тройное равно U+2261
	'b1':'c2b1',		# B1 Знак плюс-минус U+00B1
	'b2':'e289a5',		# B2 Больше чем или равно U+2265
	'b3':'e289a4',		# B3 Меньше или равный U+2264
	'b4':'e28ea7',		# B4 Левая фигурная скобка, верхний крючок U+23A7
	'b5':'e28ead',		# B5 Правая фигурная скобка, нижний крючок U+23AD
	'b6':'c3b7',		# B6 Знак деления U+00F7
	'b7':'e28988',		# B7 Почти равный U+2248
	'b8':'c2b0',		# B8 Знак градуса U+00B0
	'b9':'e28899',		# B9 Оператор точка маркер списка (скалярное умножение, знак умножения U+2219
	'ba':'efb9a3',		# BA Маленький дефис-минус U+FE63
	'bb':'e2889a',		# BB Квадратный корень U+221A
	'bc':'e281bf',		# BC Надстрочный знак латинская строчная буква n U+207F
	'bd':'c2b2',		# BD Верхний индекс 2 U+00B2
	'be':'e2888e',		# BE Конец доказательства U+220E
	'bf':'c2a4',		# BF Знак валюты U+00A4
	'c0':'d18e',		# ю U+044E
	'c1':'d0b0',		# а U+0430
	'c2':'d0b1',		# б U+0431
	'c3':'d186',		# ц U+0446
	'c4':'d0b4',		# д U+0434
	'c5':'d0b5',		# е U+0435
	'c6':'d184',		# ф U+0444
	'c7':'d0b3',		# г U+0433
	'c8':'d185',		# х U+0445
	'c9':'d0b8',		# и U+0438
	'ca':'d0b9',		# й U+0439
	'cb':'d0ba',		# к U+043A
	'cc':'d0bb',		# л U+043B
	'cd':'d0bc',		# м U+043C
	'ce':'d0bd',		# н U+043D
	'cf':'d0be',		# о U+043E
	'd0':'d0bf',		# п U+043F
	'd1':'d18f',		# я U+044F
	'd2':'d180',		# р U+0440
	'd3':'d181',		# с U+0441
	'd4':'d182',		# т U+0442
	'd5':'d183',		# у U+0443
	'd6':'d0B6',		# ж U+0436
	'd7':'d0b2',		# в U+0432
	'd8':'d18c',		# ь U+044C
	'd9':'d18b',		# ы U+044B
	'da':'d0b7',		# з U+0437
	'db':'d188',		# ш U+0448
	'dc':'d18d',		# э U+044D
	'dd':'d189',		# щ U+0449
	'de':'d187',		# ч U+0447
	'df':'d18a',		# ъ U+044A
	'e0':'d0ae',		# Ю U+042E
	'e1':'d090',		# А U+0410
	'e2':'d091',		# Б U+0411
	'e3':'d0a6',		# Ц U+0426
	'e4':'d094',		# Д U+0414
	'e5':'d095',		# Е U+0415
	'e6':'d0a4',		# Ф U+0424
	'e7':'d093',		# Г U+0413
	'e8':'d0a5',		# Х U+0425
	'e9':'d098',		# И U+0418
	'ea':'d099',		# Й U+0419
	'eb':'d09a',		# К U+041A
	'ec':'d09b',		# Л U+041B
	'ed':'d09c',		# М U+041C
	'ee':'d09d',		# Н U+041D
	'ef':'d09e',		# О U+041E
	'f0':'d09f',		# П U+041F
	'f1':'d0af',		# Я U+042F
	'f2':'d0a0',		# Р U+0420
	'f3':'d0a1',		# С U+0421
	'f4':'d0a2',		# Т U+0422
	'f5':'d0a3',		# У U+0423
	'f6':'d096',		# Ж U+0416
	'f7':'d092',		# В U+0412
	'f8':'d0ac',		# Ь U+042C
	'f9':'d0ab',		# Ы U+042B
	'fa':'d097',		# З U+0417
	'fb':'d0a8',		# Ш U+0428
	'fc':'d0ad',		# Э U+042D
	'fd':'d0a9',		# Щ U+0429
	'fe':'d0a7',		# Ч U+0427
	'0140':'',		# 140
	'0141':'e298ba',	# 141 Незакрашенное улыбающееся лицо U+263A
	'0142':'e298bb',	# 142 Закрашенное улыбающееся лицо U+263B
	'0143':'e299a5',	# 143 Черви закрашенные U+2665
	'0144':'e299a6',	# 144 Бубны закрашенные U+2666
	'0145':'e299a3',	# 145 Трефы закрашенные U+2663
	'0146':'e299a0',	# 146 Пики закрашенные U+2660
	'0147':'c2b7',		# 147 Точка по центру U+00B7
	'0148':'e29798',	# 148 Инвертированный маркер списка U+25D8
	'0149':'e2978b',	# 149 Белый круг U+25CB
	'014a':'e2978f',	# 14A Черный круг U+25CF
	'014b':'e29982',	# 14B марс U+2642
	'014c':'e29980',	# 14C венера U+2640
	'014d':'e299aa',	# 14D восьмая нота U+266A
	'014e':'e299ac',	# 14E шестнадцатая нота U+266C
	'014f':'e28897',	# 14F оператор звездочки U+2217
	'0150':'',		# 150
	'0151':'e294b4',	# 151 граница лёгкая вверх и горизонтально U+2534
	'0152':'e294ac',	# 152 граница лёгкая вниз и горизонтально U+252C
	'0153':'e294a4',	# 153 граница лёгкая вертикальная и налево U+2524
	'0154':'e2949c',	# 154 граница лёгкая вертикальная и направо U+251C
	'0155':'e294bc',	# 155 граница лёгкая вертикальная и горизонтальная U+253C
	'0156':'e29482',	# 156 граница лёгкая вертикальная U+2502
	'0157':'e29480',	# 157 граница лёгкая горизонтальная U+2500
	'0158':'e2948c',	# 158 граница лёгкая вниз в направо U+250C
	'0159':'e29490',	# 159 граница лёгкая вниз и налево U+2510
	'015a':'e29494',	# 15A граница лёгкая вверх и направо U+2514
	'015b':'e29498',	# 15B граница лёгкая вверх и налево U+2518
	'015c':'e295b3',	# 15C граница легкий диагональный крест U+2573
	'015d':'e295b1',	# 15D граница легкая диагональ с верхнего правого в нижний левый U+2571
	'015e':'e295b2',	# 15E граница легкая диагональ с верхнего левого в нижний правый U+2572
	'015f':''		# 15F
    }
    if hex in msx_to_utf:
	utf = (msx_to_utf[hex])
    else:
	utf='' # обработка отсутствия значения в словаре
    return utf

data_out = ''
file_in = open(file_msx, 'rb')
data_in = file_in.read(1)
prefix = 0

while data_in:
    code_dec = ord(data_in)
    code_hex = binascii.b2a_hex(data_in)
    data_in = file_in.read(1)
    code_bin = binascii.unhexlify(code_hex)

    if code_dec == 1 :
	prefix = 1
    elif prefix == 1 and  code_dec<128 :
	data_out=data_out + binascii.unhexlify(hex_to_utf('01'+code_hex))
	prefix=0
    elif code_dec == 26 :
	pass # A1 EOF (Конец файла)
    elif code_dec < 128 :
	data_out = data_out + code_bin
    elif code_dec >= 128 :
	data_out = data_out + binascii.unhexlify(hex_to_utf(code_hex))

file_out = open(file_utf, 'wb')
file_out.write(data_out)

file_out.close()
file_in.close()
