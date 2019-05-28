#!/bin/bash


echo "final hand-in for nur"
echo "creating the plotting directory if it does not exist"

if [ ! -d "plots" ]; then
        echo "directory does not exist so i'll create it......."
        mkdir plots
fi

echo "downloading various required data files first......"
if [ ! -e randomnumbers.txt ]; then
    wget https://home.strw.leidenuniv.nl/~nobels/coursedata/randomnumbers.txt
fi

if [ ! -e GRBs.txt ]; then      
    wget strw.leidenuniv.nl/~nobels/coursedata/GRBs.txt
fi

if [ ! -e colliding.hdf5 ]; then
    wget strw.leidenuniv.nl/~nobels/coursedata/colliding.hdf5
fi

echo "running problem 1.........................."
python3 p1a.py > p1a.txt
python3 p1b.py
python3 p1c.py
python3 p1d.py
python3 p1e.py

echo "running problem 2.........................."
python3 p2.py

echo "running problem 3.........................."
python3 p3.py

echo "running problem 4.........................."
python3 p4a.py > p4a.txt
python3 p4b.py > p4b.txt
# python3 p4c.py
# python3 p4d.py

echo "running problem 5.........................."
python3 p5a.py
# python3 p5b.py
# python3 p5c.py
# python3 p5d.py
# python3 p5e.py
# python3 p5f.py
# python3 p5g.py

echo "running problem 6.........................."
python3 p6.py > p6.txt

echo "running problem 7.........................."
python3 p7.py > p7.txt

echo "running problem 8.........................."
# python3 p8.py

pdflatex handin2.tex
pdflatex handin2.tex # for hyperref
