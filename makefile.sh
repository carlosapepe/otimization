#! /bin/sh

#sudo apt-get install lp_solve_5

full_path=$(readlink -e makefile.sh)
dir_path=$(dirname $full_path)

ld='LD_LIBRARY_PATH='$dir_path'/lp_solve_dev/'
export $ld

pyt='PYTHONPATH='$dir_path'/usr/lib/python2.5/site-packages'
export $pyt

echo "EXEMPLO 01:"
python2.7 tarefas.py < exemplo1.txt

echo "EXEMPLO 02:"
python2.7 tarefas.py < exemplo2.txt

echo "Exemplo 03:"
python2.7 tarefas.py < exemplo3.txt
