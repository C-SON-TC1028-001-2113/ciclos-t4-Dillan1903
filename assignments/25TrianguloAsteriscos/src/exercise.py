
def main():
    #escribe tu código abajo de esta línea
    h = int(input("Enter triangle heigh:"))
    for i in range(1,h + 1):
        print(''*(h - 1)+'*'*i)

if __name__=='__main__':
    main()
