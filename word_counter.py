import re

#import word doc
line_n = 0
words_l = []
words_s = [] #split words
words_d = [] #display words
words_t = [] #word & total

with open('/Users/TiredOrangeCat/GitHub/Python/HRG.txt', encoding='utf-8') as word_list:
    for a_line in word_list:
        line_n += 1
        line_s = words_l.append(a_line.rstrip())
        for a_word in a_line.split(' '):
            words_s.append(a_word)

# isolate words
    for w_word in words_s:
        if w_word not in words_d:
            word_count = words_s.count(w_word)
            words_d.append(str(w_word)+' '+str(word_count))
            #words_d.extend(w_word, word_count)
            #words_d.append(w_word)
            #words_d.append(word_count)

            #print(w_word, + word_count)

        elif w_word in words_d:
            continue


    #words_s.sort()
    words_d.sort()
            #isolate all the words, fun a for loop on the isoilated words against the file using count to print out isolated + count

        #print('{:4} {}'.format(line_n, a_line.rstrip()))
    for p_word in words_d:
        print(p_word, '\n')
    #print(words_s)
#define beginning
#define end
#scan doc
    #store words without whitespace
        #persistant importer
            #2 databases
                #2 tables
                    #word
                    #location

#display results
    #total words
    #total sentences
    #total paragraphs

    #word / # / sylables / letters



#''.match()
#''.search()

