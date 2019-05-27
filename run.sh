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

python3 p1a.py
python3 p1b.py
python3 p1c.py
python3 p1d.py
python3 p1e.py

python3 p2.py

python3 p3.py

python3 p4a.py
python3 p1b.py
# python3 p4c.py
# python3 p4d.py

python3 p5a.py
# python3 p5b.py
# python3 p5c.py
# python3 p5d.py
# python3 p5e.py
# python3 p5f.py
# python3 p5g.py

python3 p6.py

python3 p7.py

# python3 p8.py

pdflatex handin2.tex

# pdflatex p1a.tex
# pdflatex p1b.tex
# pdflatex p1c.tex
# pdflatex p1d.tex
# pdflatex p1e.tex

# pdflatex p2.tex

# pdflatex p3.tex

# pdflatex p4a.tex
# pdflatex p1b.tex
# pdflatex p4c.tex
# pdflatex p4d.tex

# pdflatex p5a.tex
# pdflatex p5b.tex
# pdflatex p5c.tex
# pdflatex p5d.tex
# pdflatex p5e.tex
# pdflatex p5f.tex
# pdflatex p5g.tex

# pdflatex p6.tex

# pdflatex p7.tex

# pdflatex p8.tex


