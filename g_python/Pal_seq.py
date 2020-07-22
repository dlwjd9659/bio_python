seq = input('input seq. :') 
i_Pal = 0

d_seq = {'G':'C','C':'G','A':'T','T':'A'}

if len(seq) % 2 == 1:
    print("Diff.")
else:
    for i in range(len(seq)):
        if seq[i] == d_seq[seq[-(i+1)]]:
            i_Pal += 0
        else:
            i_Pal += 1

    if i_Pal == 0:
        print('{0} is palindromic.'.format(seq))
    else:
        print('{0} base differ.'.format(i_Pal))
        

            
