def main():
    import json
    from difflib import get_close_matches

    myfile = json.load(open("data.json"))

    def define(i):
        i = i.lower()
        if i in myfile:
            return myfile[i]

        elif len(get_close_matches(word, myfile.keys(), cutoff = 0.74)) > 0:
            chk = input("Did you mean?\n %s\n If Yes press Y otherwise N: " % get_close_matches(word, myfile.keys())[0])
            chk = chk.lower()
            if chk == 'y':
                return myfile[get_close_matches(word, myfile.keys(), cutoff = 0.74)[0]]
            elif chk == 'n':
                if len(get_close_matches(word, myfile.keys(), cutoff = 0.74)) > 1 :
                    chk = input(
                       "Did you mean?\n %s\n If Yes press Y otherwise N: " % get_close_matches(word, myfile.keys())[1])
                    chk = chk.lower()
                    if chk == 'y':
                      return myfile[get_close_matches(word, myfile.keys(), cutoff = 0.74)[1]]
                    elif chk == 'n':
                      if len(get_close_matches(word, myfile.keys(), cutoff = 0.74)) > 2:
                         chk = input(
                                 "Did you mean?\n %s\n If Yes press Y otherwise N: " % get_close_matches(word, myfile.keys())[2])
                         chk = chk.lower()
                         if chk == 'y':
                             return myfile[get_close_matches(word, myfile.keys(), cutoff = 0.74)[2]]
                         elif chk == 'n':
                             return "I dont know"
                      else:
                          return 'idk'
                else:
                    return "The word doesn't exist then double check it"
            else:
                return "We don't understand the input"

        else:
            return "Check your query!"


    word = input("enter any word: ")

    output = define(word)
    k = 1
    if type(output) == list:
        for j in output:
            print('%d:-' % k, j)
            k = k+1
        print('Note :- We have %d definations of %s.' % (k-1, word))
    else:
        print(output)

    reload = input('For another search, press Y\n To Close press any other button.')
    reload.lower()
    if reload == 'y':
        main()


main()
