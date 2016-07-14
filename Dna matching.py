sample = ['GTA','GGG','CAC']

'''When used, this method will take in a file, read it, add the file's contents to an empty string, and return the updated string
'''
def read_dna(dna_file):
    dna_data = ""
    with open(dna_file, "r") as f:
        for line in f:
            dna_data += line
    return dna_data
  
'''
we'll need a method that will take a string, create a list of codons from that string, and return the list. This will make the DNA analysis much easier later.
'''
def dna_codons(dna):
    codons = []
    for i in range(0,len(dna),3):
        if (i+3) < len(dna):
            codons.append(dna[i:i+3])
    return codons
  
'''
 The next step is to create a method that will iterate through both the sample and a suspect's DNA. The method should count the number of times a codon in the sample matches a codon in the suspect's DNA.
 '''
def match_dna(dna):
    matches = 0
    for codon in dna:
        if codon in sample:
            matches += 1
    return matches
  
def is_criminal(dna_sample): 
    dna_data = read_dna(dna_sample)
    codons = dna_codons(dna_data)
    num_matches = match_dna(codons)
    if num_matches >= 3:
        print "The number of matches is %s. The investigation should continue." % num_matches
    else:
        print "The number of matches is %s. The suspect can be freed." % num_matches
      
is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')
          
        
    
  
