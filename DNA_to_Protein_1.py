
dna=input("Enter DNA string :")

for letter in dna:  
    rna=dna.replace('T','U')
             
protein_string=""

for i in range(0,(len(rna)+1),3):
       
    if rna[i:i+3]=="UUU" or rna[i:i+3]=="UUC":
        protein_string+="Phe"
    elif rna[i:i+3]=="UCU" or rna[i:i+3]=="UCC" or rna[i:i+3]=="UCA" or rna[i:i+3]=="UCG" or rna[i:i+3]=="AGU" or rna[i:i+3]=="AGC":
        protein_string+="Ser"
    elif rna[i:i+3]=="UAU" or rna[i:i+3]=="UAC":
        protein_string+="Tyr"
    elif rna[i:i+3]=="UGU" or rna[i:i+3]=="UGC":
        protein_string+="Cys"    
    elif rna[i:i+3]=="UUA" or rna[i:i+3]=="UUG" or rna[i:i+3]=="CUU" or rna[i:i+3]=="CUA" or rna[i:i+3]=="CUG":
        protein_string+="Leu" 
    elif rna[i:i+3]=="UGG" :
        protein_string+="Trp"        
    elif rna[i:i+3]=="CCU" or rna[i:i+3]=="CCC" or rna[i:i+3]=="CCA" or rna[i:i+3]=="CCG" :
        protein_string+="Pro" 
    elif rna[i:i+3]=="CAU" or rna[i:i+3]=="CAC":
        protein_string+="His"    
    elif rna[i:i+3]=="CGU" or rna[i:i+3]=="CGC" or rna[i:i+3]=="CGA" or rna[i:i+3]=="CGG" or rna[i:i+3]=="AGA" or rna[i:i+3]=="AGG":
        protein_string+="Arg"
    elif rna[i:i+3]=="AUU" or rna[i:i+3]=="AUC" or rna[i:i+3]=="AUA":
        protein_string+="Ile"
    elif rna[i:i+3]=="ACU" or rna[i:i+3]=="ACC" or rna[i:i+3]=="ACA" or rna[i:i+3]=="ACG" :
        protein_string+="Thr"   
    elif rna[i:i+3]=="AAU" or rna[i:i+3]=="AAC":
        protein_string+="Asn"            
    elif rna[i:i+3]=="AAA" or rna[i:i+3]=="AAG":
        protein_string+="Lys"     
    elif rna[i:i+3]=="GUU" or rna[i:i+3]=="GUC" or rna[i:i+3]=="GUA" or rna[i:i+3]=="GUG" :
        protein_string+="Val"  
    elif rna[i:i+3]=="GCU" or rna[i:i+3]=="GCC" or rna[i:i+3]=="GCA" or rna[i:i+3]=="GCG" :
        protein_string+="Ala"  
    elif rna[i:i+3]=="GAU" or rna[i:i+3]=="GAC":
        protein_string+="Asp"    
    elif rna[i:i+3]=="GGU" or rna[i:i+3]=="GGC" or rna[i:i+3]=="GGA" or rna[i:i+3]=="GGG" :
        protein_string+="Gly"
    elif rna[i:i+3]=="GAA" or rna[i:i+3]=="GAG":
        protein_string+="Glu"
    elif rna[i:i+3]=="AUG":
        protein_string+="Met"
    elif rna[i:i+3]=="CAA" or rna[i:i+3]=="CAG":
        protein_string+="Gln"
    elif rna[i:i+3]=="UAA" or rna[i:i+3]=="UAG" or rna[i:i+3]=="UGA":
        protein_string+="Stop"
        

print(protein_string)         