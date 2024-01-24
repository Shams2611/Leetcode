#My initial wrong approach 
def DNA_strand(dna):
    char = list(dna)
    for i in char:
        if i == 'A':
            char.replae('A', 'C')
        elif i == 'T':
            char.replace('T', 'G')
            
    return ''.join(char)
'''
Thought process behind this:
taking the string 
then convering it to list composed of each character in the string 
then iterating through the list and replacing each character 
two things: this is very tedious 

'''

#Correct approach 
def DNA_strand(dna):
    complement = {'A':'T', 'C': 'G', 'T': 'A', 'G':'C'}
    
    return ''.join(complement[base] for base in dna)