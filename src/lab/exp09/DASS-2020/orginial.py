# Read the file and get the DNA string
file = open('me.txt', 'r')
dna = file.read()
dna=dna
cna=dna

# DNA codon table
codon={'UUU':'Phe','UUC':'Phe','UUA':'Leu','UUG':'Leu',
'CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu','AUU':'Ile',
'AUC':'Ile','AUA':'Ile','AUG':'Met','GUU':'Val','GUC':'Val',
'GUA':'Val','GUG':'Val','UCU':'Ser','UCC':'Ser','UCA':'Ser',
'UCG':'Ser','CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr','GCU':'Ala',
'GCC':'Ala','GCA':'Ala','GCG':'Ala','UAU':'Tyr','UAC':'Tyr',
'UAA':'STOP','UAG':'STOP','CAU':'His','CAC':'His','CAA':'Gln',
'CAG':'Gln','AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys',
'GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu','UGU':'Cys',
'UGC':'Cys','UGA':'STOP','UGG':'Trp','CGU':'Arg','CGC':'Arg',
'CGA':'Arg','CGG':'Arg','AGU':'Ser','AGC':'Ser','AGA':'Arg',
'AGG':'Arg','GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}

protein_sequence = ""


#Generate RNA Sequence by converting dna with the following process
# --> Compliment TAGC to AUCG and then just reverse it

new=""

for i in range(len(dna)):
    if(dna[i]=="t"):
        new+="a"
    elif(dna[i]=="a"):
        new+="u"
    elif(dna[i]=="g"):
        new+="c"
    elif(dna[i]=="c"):
        new+="g"


reversedme=''.join(reversed(new))

reversedme=reversedme.upper()
#print("DNA Sequence: ",reversedme)


start=0
end=0
# Generate protein sequenceprotein
i=0
while(1):
    index=reversedme.find("AUG",i,len(reversedme)-1)
    start=1
    temp_string=""
    for i in range(index, len(reversedme),3):
        #print(reversedme[i:i+3])
        if(i+2<=len(reversedme)-1):
                    if(reversedme[i:i+3]=="UAA" or reversedme[i:i+3]=="UGA" or reversedme[i:i+3]=="UAG"):
                        protein_sequence =protein_sequence + temp_string +"\n" + "\n"
                        break
                    else:
                        #print(reversedme[i:i+3])
                        temp_string += codon[reversedme[i:i+3]] + " "
    

    if(len(reversedme)-3<i):
        break

# Print the protein sequence
print("Protein Sequence: ", protein_sequence)

# End of program
