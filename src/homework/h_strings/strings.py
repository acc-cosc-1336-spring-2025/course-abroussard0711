# to create the functions that determine the Hamming distance between two strings and the reverse complements of a string

# function to calculate and return the Hamming distance between two strings
def get_hamming_distance (dna1,dna2):
    
    # to validate the two strings are of equal length
    if len(dna1) != len(dna2):
        print ("DNA sequences must be of equal length")

    # to determine the number of corresponding symbols that differ in DNA1 and DNA2 and return the distance value
    distance = 0
    for seq in range (len(dna1)):
        if dna1[seq] != dna2[seq]:
            distance += 1

    return distance

# function to derive and return the reverse compliment of a string
def get_dna_complement(dna):
    
    complement = ""

    # for loop to assign the complementary values of a given string
    for num in range (len(dna)):
        
        if dna[num] == "A":
            complement += "T"
        elif dna[num] == "T":
            complement += "A"
        elif dna[num] == "C":
            complement += "G"
        elif dna[num] == "G":
            complement += "C"
        else:
            print ("Invalid DNA character found")

    
    reverse_complement = ""
    
    # for loop to reverse the order of the complementary values determined in the above for loop
    for num in range (len(complement) -1, -1, -1):
        reverse_complement += complement[num]        

    return reverse_complement