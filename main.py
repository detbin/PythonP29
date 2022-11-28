from functools import reduce
def suma (a,b):
    return a+b
def impares(x):
    if x%2!=0:
        return True
def main():
 lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
 listaimpares=list(filter(impares,lista))
 print(listaimpares)
 print(reduce(suma,listaimpares))

if __name__ == '__main__':
    main()