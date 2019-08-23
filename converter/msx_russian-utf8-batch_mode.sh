#!/bin/bash

# Пакетное преобразование файлов из формата MSX в UTF-8

files_path='.'		# путь к исходныи и конечным файлам
file_ext_msx='.tor'	# расширение исходного файла (MSX)
file_msx_mask='bas*'	# маска исходного файла (MSX)
file_ext_utf='.txt'	# расширение конечного файла (UTF-8)

file_msx_mask=$file_msx_mask$file_ext_msx
for file_msx in `find $files_path -type f -name "$file_msx_mask"`
    do
	file_utf=${file_msx//$file_ext_msx/$file_ext_utf}
	python ./msx_russian-utf8.py $file_msx $file_utf
    done
exit
