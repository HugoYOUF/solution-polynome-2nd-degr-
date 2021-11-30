from math import sqrt


def polynome():
    a=float(input("entrez un nombre a : "))
    b=float(input("entrez un nombre b : "))
    c=float(input("entrez un nombre c : "))
    delta = b*b -4*a*c
    if delta < 0 :
        print ("Il n'y a pas de solution pour ce polynome")
    elif delta > 0 :
        solution_1 =(-b-sqrt(delta))//2*a
        solution_2 =(-b +sqrt(delta))//2*a
        print (" Il ya deux solutions pour ce polynome qui sont :  \n"
               +"x1 =  "+str(solution_1) +"\n"
               +"x2 = "+ str(solution_2))
    elif delta ==0:
        solution_0 = (-b)//2*a
        print ("Il ya une seule solution pour ce polynome qui est :  \n"
               +"x0 = "+str(solution_0))




polynome()
