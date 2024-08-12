
round_keys = [None] * 16

def shift_left_once(key_chunk):
    shifted = key_chunk[1:] + key_chunk[0]
    return shifted

def shift_left_twice(key_chunk):
    shifted = key_chunk[2:] + key_chunk[0] + key_chunk[1]
    return shifted

def generate_keys(key):

    pc1 = [57,49,41,33,25,17,9, 
           1,58,50,42,34,26,18, 
           10,2,59,51,43,35,27, 
           19,11,3,60,52,44,36,		 
           63,55,47,39,31,23,15, 
           7,62,54,46,38,30,22, 
           14,6,61,53,45,37,29, 
           21,13,5,28,20,12,4]

    pc2 = [14,17,11,24,1,5, 
           3,28,15,6,21,10, 
           23,19,12,4,26,8, 
           16,7,27,20,13,2, 
           41,52,31,37,47,55, 
           30,40,51,45,33,48, 
           44,49,39,56,34,53, 
           46,42,50,36,29,32]

    perm_key = ""
    for i in pc1:
        perm_key += key[i-1]

    left = perm_key[:28]
    right = perm_key[28:]

    for i in range(16):
        if i == 0 or i == 1 or i == 8 or i == 15:
            left = shift_left_once(left)
            right = shift_left_once(right)
       
        else:
            left = shift_left_twice(left)
            right = shift_left_twice(right)

        combined_key = left + right
        round_key = ""

        for j in pc2:
            round_key += combined_key[j-1]

        round_keys[i] = round_key

        # Print the left and right 28-bit halves of the key for each round
        print(f"Round {i+1}: C = {left} \nD ={right}\n")

key = "1010101010111011000010010001100000100111001101101100110011011101"
generate_keys(key)
