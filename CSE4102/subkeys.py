
pc1 = [56, 48, 40, 32, 24, 16, 8, 0,
       57, 49, 41, 33, 25, 17, 9, 1,
       58, 50, 42, 34, 26, 18, 10, 2,
       59, 51, 43, 35, 62, 54, 46, 38,
       30, 22, 14, 6, 61, 53, 45, 37,
       29, 21, 13, 5, 60, 52, 44, 36,
       28, 20, 12, 4, 27, 19, 11, 3]

txt="1011010100111010100001101010001010011110100111110111111001000111"
print(txt)
print(len(txt))
pc1_txt=''
for i in range(56):
    pc1_txt+=txt[pc1[i]-1]
left_half = pc1_txt[:28]
right_half = pc1_txt[28:]
print("first 28 bit: ",left_half)
print("Second 28 bit: ",right_half)
print(len(pc1_txt))
