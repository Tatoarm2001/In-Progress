try:
    grade=float(input('Nota?(Entre 1.0 y 0.0)-->'))
 
    def computegrade(grade):
        if grade< 0.6:
            print('F')
            quit
        elif grade <=  0.6:
            print('D')
        elif grade <= 0.7:
            print('C')
        elif grade <= 0.8:
            print('B')
        elif grade <= 0.9:
            print('A')

    computegrade(grade)
except:
    print('Error')