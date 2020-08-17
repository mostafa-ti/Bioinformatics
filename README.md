Dependencies:<br/>
Install python3, pip3

Install matplotlib.pyplot:<br/>
$ pip3 install matplotlib

Install python mpl_toolkits:<br/>
$ pip3 install matplotlib

install scipy:<br/>
$ pip3 install scipy

install numpy:<br/>
$ pip3 install numpy

# Bioinformatics
Description:<br/>
This python script parses the genome based on two integer number which defines window size and number of steps, calculate coordinates of nodes for each window size based on Xn,Yn and Zn components and then construct a unique representation of the DNA sequence.<br/>


Definition of Z-curve components: <br/>
Xn is the distribution of Purines (A,G) and Pyrimidins(C,T)
Xn = (An+Gn) - (Cn+Tn)

Yn is the distribution of Amino (A,C) and Keto (G,T) <br/>
Yn = (An+Cn) - (Gn+Tn)

Zn is the distribution of Weak hydrogen bonds (A,T) and Strong hydrogen bonds (C,G) <br/>
Zn = (An+Tn) - (Cn+Gn)

List of functions: <br/>
There are four defined functions used in this program.<br/>
- readfasta function to read the fasta files.<br/>
- frequency function to calculate the abondancy of each nucleotide.<br/>
- slide_win function, this function parses the fasta file based on window size<br/>
and step. Both window size and step should be defined by user.<br/>
- Z_curve function to calculate the Z curve components based on the formula for
the components X, Y and Z.<br/>

At the end The Z curves have been smoothed by using the interpolation module from the SciPy library in python.<br/>

Procedure:<br/>
Program name: Z_curve.py<br/>
fin: fasta_file.fna<br/>

Usage:<br/>
./Z_curve.py input.fna [integer window size] [integer step]
