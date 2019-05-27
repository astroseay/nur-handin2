#!/bin/bash


echo "final hand-in for nur"
echo "creating the plotting directory if it does not exist"

if [ ! -d "plots" ]; then
        echo "directory does not exist so i'll create it......."
        mkdir plots
fi

echo "downloading various required data files first......"
wget https://home.strw.leidenuniv.nl/~nobels/coursedata/randomnumbers.txt
wget strw.leidenuniv.nl/~nobels/coursedata/GRBs.txt
wget strw.leidenuniv.nl/~nobels/coursedata/colliding.hdf5

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


