def carga(arre,i,j):
    if i<2:
        if j<2:
            arre[i][j]=3
            carga(arre,i,j+1)
        else:
            carga(arre,i+1,0)

if __name__=="__main__":
    lis=[[0,0],[0,0]]
    carga(lis,0,0)
    print(lis)
