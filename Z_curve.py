#!/usr/local/bin/env python3
'''
Title: Z curve (Population genetic project)
Version: 1.0
Date : 2020-03-15
Author : Mostafa Torbati

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
'''
import sys
from collections import Counter
import matplotlib.pyplot as plt
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# Open the fasta file
fin =sys.argv[1]
winSize = int(sys.argv[2])
step =int(sys.argv[3])
def readfasta(fin):
    seq = open(fin, 'r')
    fasta_dict = {}
    l = list()
    header = None
    for line in seq:
        if line.startswith('>'):
            if header:
                fasta_dict[header] = ''.join(l)
                del l[:]
            header = line.strip().replace(">", "").split()[0]
        else:
            l.append(line.strip())
    fasta_dict[header] = ''.join(l)
    return fasta_dict

def frequency(seq):
  NT = Counter(seq)
  return NT

def slide_win(sequence, winSize, step):
    ChunksList = []
    for index in range(0,len(sequence),step):
        #print(index,min(index + winSize,len(sequence)))
        ChunksList.append(sequence[index:min(index + winSize,len(sequence))])
    return ChunksList

def Z_curve(slides):
    coordinates = {}
    Xcoords = []
    Ycoords = []
    Zcoords = []
    for slide in slides:
        #print(slide)
        freq = frequency(slide)
        Xcoords.append((freq["A"]+freq["G"])-(freq["C"]+freq["T"]))
        Ycoords.append((freq["A"]+freq["C"])-(freq["G"]+freq["T"]))
        Zcoords.append((freq["A"]+freq["T"])-(freq["C"]+freq["G"]))
    return [Xcoords,Ycoords,Zcoords]

sequence=list(readfasta(fin).values())[0]
#print(sequence)
slides = slide_win(sequence, winSize, step)
#print(slides)
coordinates = Z_curve(slides)
#print(coordinates)

#now we get all the knots and info about the interpolated spline
tck, u= interpolate.splprep(coordinates, k=3)
#here we generate the new interpolated dataset,
#increase the resolution by increasing the spacing, 50 in this example
new = interpolate.splev(np.linspace(0,1,500), tck, der=0)

#now lets plot it!
fig = plt.figure()
ax = Axes3D(fig)
#ax.plot(coordinates[0], coordinates[1], coordinates[2], label='Original curve', lw =2, c='Dodgerblue')
#If you do not want to show the fit chart, just comment the next line;)
ax.plot(new[0], new[1], new[2], label='Smoothed curve', lw =2, c='red')
ax.legend()
ax.set_xlabel('X (R/Y)', c="blue")
ax.set_ylabel('Y (M/K)', c="red")
ax.set_zlabel('Z (S/W or GC profile)', c="green")

plt.show()
