#!/usr/bin/env python

#This code asks the user to select an option to manipulate their DNA sequence.

#import random library
import random

#Output the options for the user to select. Letters A  or B are the options.
letter= input('Select one option using letters A or B:\nA:Tranlate a protein coding sequence to amino acids\n\
B:Randomly draw a codon from your sequence\nYour selection: ')

# DB: Good to leave some space after the instructions so that it's obvious you want user to provide input.

#if user selects option A this code is executed to convert sequence into respective aminoacids
if letter == "A":

		#asks user to type in their DNA sequence.
        DNAseq=input ('Enter your DNA sequence here: ')
        
		#if sequence is lower case it is converted to upper case        
        DNAseq=DNAseq.upper()
        print (DNAseq)
        
		#Table of codons and their respective amino acids
        codontable = {
                'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
                'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
                'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
                'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
                'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
                'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
                'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
                'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
                'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
                'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
                'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
                'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
                'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
                'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
                }
                
		#my output variable
        proteinsequence = ''
        
		#extract codons from sequence provided and output respective aminoacids using table above
        for n in range(0,len(DNAseq),3):
                        proteinsequence += codontable[DNAseq[n:n+3]]
        print (proteinsequence)
        
else:
		#if option B is selected
        #if letter =="B":	# DB: I'm not sure you need this, since you've already used "else"

		#asks user to type in their DNA sequence
        DNAseq=input ('Enter your DNA sequence here: ')  # DB: Leave space after prompt

		#convert sequence into upper case   
        DNAseq=DNAseq.upper()
        print (DNAseq)
				
		#Define the codon and output each codon as an individual string
        codon=[(''.join(DNAseq[i:i +3])) for i in range(0,len(DNAseq),3)]
        print (codon)
        
		#randomly select one of the codons 
        print (random.choice(codon))


# DB: Good! Just a few minor comments (see above). For ease of reading the code, I'd recommend
#     using more spacing between lines and keeping comments with the same level of indentation
#     as the code they're referring to.

#     Also, it's always good to name files with Python code using a .py extension.