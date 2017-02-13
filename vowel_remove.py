def remove_vowel():
    word = input("Enter a word: ")
    vowel_l = ['i', 'e', 'a', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    w_list = list(word)
    vowel_sp = []
    f_word = []
        
    for vowel in vowel_l:
        while vowel in w_list:
            vowel_sp = w_list.remove(vowel)
    #print(w_list)
    
    f_word = ''.join(w_list)
    print(f_word)

while True:
    remove_vowel()

