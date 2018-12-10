#!/usr/bin/env python

#asks the user to output the DNA sequence
DNAseq=input ('Enter your DNA sequence here: ')

#convert DNA sequence into uppercase 
DNAseq=DNAseq.upper()
print (DNAseq)

#first replace "T"s and "G"s with other letters to confusion
DNAseq=DNAseq.replace("T","x")
DNAseq=DNAseq.replace("G","y")

#replace "A"s and "C"s to "T"s and "G"s.
DNAseq=DNAseq.replace("A","T")
DNAseq=DNAseq.replace("C","G")

#replace "y" and "x" to "A"s and "C"s
DNAseq=DNAseq.replace("x","A")	# DB: Clever strategy!
DNAseq=DNAseq.replace("y","C")

#reverse the complementary strand formed above
DNAseq=(DNAseq[::-1])
print(DNAseq)

# DB: Overall, looks good! I'd suggest adding spaces between logical
#     blocks of code to improve readability. This is particularly true
#     when you have comments.