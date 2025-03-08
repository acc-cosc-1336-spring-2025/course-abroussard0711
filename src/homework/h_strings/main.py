# define the main function to call the get_hamming_distance function and the get_dna_complement function

import strings

def main():
    
    DNA1 = "GAGCCTACTAACGGGAT"
    DNA2 = "CATCGTAATGACGGCCT"

    print ("Hamming distance: ", strings.get_hamming_distance(DNA1,DNA2))

    DNA = "AAAACCCGGT"

    print ("Reverse compliment is: ", strings.get_dna_complement(DNA))
    
main ()


