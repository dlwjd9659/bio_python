a = input("Your name : ")
print(a)

#######################
print()


d = {'A':'Adenine','C':'Cytosine','G':'Guanine','T':'Thymine','U':'Uracil'}

def base():
    a = input("Base : ")
    if a == 'A':
        return(d['A'])
    elif a == 'C':
        return(d['C'])
    elif a == 'G':
        return(d['G'])
    elif a == 'T':
        return(d['T'])
    else:
        return "error"
     
seq_b = base()
print(seq_b)


#######################

#def t_e():
#    n = int(input("input : "))
#    try:
#        a = 10/n
#        return a
#    except ZeroDivisionError:
#        print("Error")

#test = t_e()

######################

   
