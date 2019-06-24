global pesototal

class Grafo():
    def _init_(self,pos,indice):
        self.pos = pos
        self.indice = indice
        self.siguiente = None
        self.aristas = []
        self.caminocorto = []

    def InsertarVertices(self, pos,indice):
        if self.indice:
            if self.siguiente:
                self.siguiente.InsertarVertices(pos,indice)
            else:
                self.siguiente = Grafo(pos,indice)

    def Mostrar(self):
        if self.indice:
            print(self.indice)
            for i in range(len(self.aristas)):
                print("El peso de su arista",i,"es:",self.aristas[i].peso,"y la arista en la que estoy a punta hacia",self.aristas[i].nodoDestino.indice)
            if self.siguiente:
                self.siguiente.Mostrar()

    def TraerNodo(self,busca):
        if self.indice:
            if self.indice == busca:
                return self
            else:
                return self.siguiente.TraerNodo(busca)
        else:
            return None

    def AsignarArista(self,ppartida,pllegada,peso):
        nodopartida = self.TraerNodo(ppartida)
        nodollegada = self.TraerNodo(pllegada)
        arista = Arista(peso,nodollegada,nodopartida.indice)
        nodopartida.aristas.append(arista)
        return 1

    def ChecarNodo(self,pmeta,peso,posicion,pesomini,camino,caminoAux):
        if self.indice == pmeta:
            if peso < pesomini:
                print("peso",peso)
                print("pesomini",pesomini)
                pesomini=peso
                camino.insert(posicion,self.indice)
                print("Encontre mi camino ideal",camino)
                return peso
            else:
                print("El peso es mayor a pesomini")
                return 1
        else:
            if(peso >= pesomini):
                print("Aun no lo encuentro, pero ya me pase de peso")
                return 1
            else:
                if len(self.aristas) > 0:
                    print("Insertare en la posicion: ",posicion)
                    camino.insert(posicion,self.indice)
                    print("El camino va asi",camino)
                    self.ChecarArista(self.aristas,pmeta,peso,posicion,pesomini,self.indice,camino,caminoAux)
                    return 0
                else:
                    return 0

    def ChecarArista(self,listaArista,pmeta,peso,posicion,pesomini,panterior,camino,caminoAux):
        for i in range(len(listaArista)):
            print("Ire a checar el nodo de mi arista numero",i,"el nodo tiene por indice",listaArista[i].nodoDestino.indice)
            valor =listaArista[i].nodoDestino.ChecarNodo(pmeta,peso+listaArista[i].peso,posicion+1,pesomini,camino,caminoAux)
            if valor != 0 and valor!=None:
                if valor != 1:
                    print("Valor fue diferente de 1, por lo tanto encontre mi camino menor por el momento")
                    caminoAux.clear()
                    for a in range(len(camino)):
                        caminoAux.insert(a,camino[a])
                    camino.pop(posicion+1)
                    pesomini = valor
                else:
                    print("Valor fue igual a 1, encontre mi destino pero el peso fue mayor")
                    print("El dato que quiero eliminar es:",camino[posicion])
                    print("posi",posicion)
                    camino.pop(posicion)
                    print("camino es:",camino)
                    print("Por lo tanto mi camino ideal por el momento es:",caminoAux)
        return

    #falta arreglar el pesomini (acerlo global) y que el camino muestre solo el optimo no todos

class Arista():
    def _init_(self,peso,nodoDestino,nombreNodoPartida):
        self.nombreNodoPartida = nombreNodoPartida
        self.peso = peso
        self.nodoDestino=nodoDestino





bolita = Grafo(2,1)
bolita.InsertarVertices(3,2)
bolita.InsertarVertices(4,3)
bolita.InsertarVertices(5,4)
bolita.AsignarArista(1,3,20)
bolita.AsignarArista(1,4,50)
bolita.AsignarArista(1,2,20)
bolita.AsignarArista(3,4,10)
bolita.AsignarArista(2,3,10)
bolita.AsignarArista(2,4,5)
camino = []
caminoAux = []
nodo = bolita.TraerNodo(1)
nodo.ChecarNodo(4,0,0,100,camino,caminoAux)
#bolita.ChecarNodo(4,0,1,100,camino)
#bolita.Mostrar()