Dependencies:
Install python3, pip3

Install matplotlib.pyplot:
$ pip3 install matplotlib

Install python mpl_toolkits:
$ pip3 install matplotlib

install scipy:
$ pip3 install scipy

install numpy:
$ pip3 install numpy

# Bioinformatics
Description:
This program provides three-dimensional curve and prepare a unique representation
of the DNA sequence based on Xn,Yn and Zn components.

Definition of components:
Xn is the distribution of Purines (A,G) and Pyrimidins (C,T)
Xn = (An+Gn) - (Cn+Tn)

Yn is the distribution of Amino (A,C) and Keto (G,T)
Yn = (An+Cn) - (Gn+Tn)

Zn is the distribution of Weak hydrogen bonds (A,T) and Strong hydrogen bonds (C,G)
Zn = (An+Tn) - (Cn+Gn)

List of functions:
There are four defined functions used in this program.
- readfasta function to read the fasta files.
- frequency function to calculate the abondancy of each nucleotide.
- slide_win function, this function parses the fasta file based on window size
and step. Both window size and step should be defined by user.
- Z_curve function to calculate the Z curve components based on the formula for
the components X, Y and Z.

Procedure:
Program name: Z_curve.py
fin: fasta_file.fna

Usage:
./Z_curve.py input.fna [integer window size] [integer step]
