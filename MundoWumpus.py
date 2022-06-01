from Agente import *
import copy
numberOfCalls=0

class KnowledgeBase:
    def __init__(self):
        self.Clausulas= []

        DefineWumpus= {}
        DefineAbismo = {}
        for i in range (16):
            DefineWumpus[i]=1
            DefineAbismo[i+32]=1
            DefineAbismo[i+40]=1
        self.Clausulas.append(DefineWumpus)
        self.Clausulas.append(DefineAbismo)

        for i in range(16):
            for j in range(i+1, 16):
                MaximoWumpus={}
                MaximoAbismo={}
                MaximoWumpus[i]=-1
                MaximoWumpus[j]=-1
                MaximoAbismo[i+32]=-1
                MaximoAbismo[j+32]=-1
                MaximoAbismo[i+32]=-1
                MaximoAbismo[j+32]=-1
                self.Clausulas.append(MaximoWumpus)
                self.Clausulas.append(MaximoAbismo)

        for i in range(16):
            FedorWumpus={}
            FedorWumpus[i+16]=-1
            if (i+4)//4 < 4:
                FedorWumpus[i+4]=1
                RegraFedor={}
                RegraFedor[i+16]=1
                RegraFedor[i+4]=-1
                self.Clausulas.append(RegraFedor)
            if(i-4)//4 >= 0:
                FedorWumpus[i-4]=1
                RegraFedor={}
                RegraFedor[i+16]=1
                RegraFedor[i-4]=-1
                self.Clausulas.append(RegraFedor)
            if i//4 == (i+1)//4:
                FedorWumpus[i+1]=1
                RegraFedor={}
                RegraFedor[i+16]=1
                RegraFedor[i+1]=-1
                self.Clausulas.append(RegraFedor)
            if i//4 == (i-1)//4:
                FedorWumpus[i-1]=1
                RegraFedor={}
                RegraFedor[i+16]=1
                RegraFedor[i-1]=-1
                self.Clausulas.append(RegraFedor)
            self.Clausulas.append(FedorWumpus)
        

        for i in range(16):
            BrisaAbsimo={}
            BrisaAbsimo[i+48]=-1
            if(i+4)//4 < 4:
                BrisaAbsimo[i+4+32]=1
                RegraBrisa={}
                RegraBrisa[i+48]=1
                RegraBrisa[i+4+32]=-1
                self.Clausulas.append(RegraBrisa)
            if(i-4)//4 >= 0:
                BrisaAbsimo[i-4+32]=1
                RegraBrisa={}
                RegraBrisa[i+48]=1
                RegraBrisa[i-4+32]=-1
                self.Clausulas.append(RegraBrisa)
            if i//4 == (i+1)//4:
                BrisaAbsimo[i+1+32]=1
                RegraBrisa={}
                RegraBrisa[i+48]=1
                RegraBrisa[i+1+32]=-1
                self.Clausulas.append(RegraBrisa)
            if i//4 == (i-1)//4:
                BrisaAbsimo[i-1+32]=1
                RegraBrisa={}
                RegraBrisa[i+48]=1
                RegraBrisa[i-1+32]=-1
                self.Clausulas.append(RegraBrisa)
            self.Clausulas.append(BrisaAbsimo)

        SemWumpus={0:-1}
        SemAbismo={32:-1}
        self.Clausulas.append(SemWumpus)
        self.Clausulas.append(SemAbismo)

    def AdicionaClausula(self, clause): 
        self.Clausulas.append(clause)
    
    def ObterClausula(self): 
        return copy.deepcopy(self.Clausulas)
    

def EncontreSimboloPuro(Clausulas, Simbolos):
    for Simbolo in Simbolos:
        positive=0
        negative=0
        for clause in Clausulas:
            if Simbolo in clause:
                if clause[Simbolo]==1:
                    positive= positive+1
                else:
                    negative= negative+1
        if negative==0:
            return Simbolo, 1
        elif positive==0:
            return Simbolo, -1
    return -1, 0

def EncontrarClausulaUnitaria(Clausulas):
    for clause in Clausulas:
        if len(clause)==1:
            for Simbolo in clause:
                return Simbolo, clause[Simbolo]
    return -1, 0

def SelecionaSimbolo(Clausulas, Simbolos):
    count={}
    positive={}
    negative={}
    for clause in Clausulas:
        for literal in clause:
            if literal not in count:
                count[literal]=0
                positive[literal]=0
                negative[literal]=0

            count[literal]= count[literal]+1
            if clause[literal]==1:
                positive[literal]=positive[literal]+1
            else:
                negative[literal]=negative[literal]+1
    
    maxLiteral= list(Simbolos.keys())[0]
    maxCount=0
    for literal in count:
        if count[literal]>maxCount:
            maxLiteral= literal
            maxCount= count[literal]

    if positive[maxLiteral]>negative[maxLiteral]:
        return maxLiteral, 1
    return maxLiteral, -1

def FuncaoDPLL(Clausulas, Simbolos, model):
    global numberOfCalls
    numberOfCalls= numberOfCalls+1
    removeClauses=[]
    for clause in Clausulas:
        valueUnknown=True
        deleteLiterals=[]
        for literal in clause.keys():
            if literal in model.keys():
                if model[literal]==clause[literal]:
                    removeClauses.append(clause)
                    valueUnknown=False
                    break
                else:
                    deleteLiterals.append(literal)
        
        for literal in deleteLiterals:
            del clause[literal]
        if valueUnknown==True and not bool(clause):
            return False

    Clausulas= [ x for x in Clausulas if x not in removeClauses]

    if len(Clausulas)==0:
        return True

    SimboloPuro, value = EncontreSimboloPuro(Clausulas, Simbolos)
    if value!=0:
        del Simbolos[SimboloPuro]
        model[SimboloPuro]=value
        return FuncaoDPLL(Clausulas, Simbolos, model)
    
    UnidadeSimbolo, value = EncontrarClausulaUnitaria(Clausulas)
    if value!=0:
        del Simbolos[UnidadeSimbolo]
        model[UnidadeSimbolo]=value
        return FuncaoDPLL(Clausulas, Simbolos, model)

    Simbolo, value= SelecionaSimbolo(Clausulas, Simbolos)
    del Simbolos[Simbolo]
    model[Simbolo]= value

    if FuncaoDPLL(copy.deepcopy(Clausulas), copy.deepcopy(Simbolos), copy.deepcopy(model)):
        return True
    
    model[Simbolo]= -value
    return FuncaoDPLL(Clausulas, Simbolos, model)


def DPLLSatisfiable(Clausulas):
    Simbolos={}
    for clause in Clausulas:
        for literal in clause:
            Simbolos[literal]=True
    
    model={}
    return FuncaoDPLL(Clausulas, Simbolos, model)

def MoveParaNaoVisitado(ag, Visitado, goalLoc, dfsVisitados):
    curPos=ag.EncontrarlocalizacaoAtual()
    curLoc= 4*(curPos[0]-1)+curPos[1]-1
    if(curLoc==goalLoc):
        return True
    dfsVisitados[curLoc]=True
    
    if curPos[1]+1 <=4 and (Visitado[curLoc+1]==True or (curLoc+1)==goalLoc) and dfsVisitados[curLoc+1]==False:
        ag.Movimentacao('Cima')
        QuartoAcessivel= MoveParaNaoVisitado(ag, Visitado, goalLoc, dfsVisitados)
        if QuartoAcessivel:
            return True
        ag.Movimentacao('Baixo')

    if curPos[0]+1 <=4 and (Visitado[curLoc+4]==True or (curLoc+4)==goalLoc) and dfsVisitados[curLoc+4]==False:
        ag.Movimentacao('Direita')
        QuartoAcessivel= MoveParaNaoVisitado(ag, Visitado, goalLoc, dfsVisitados)
        if QuartoAcessivel:
            return True
        ag.Movimentacao('Esquerda')

    if curPos[0]-1 >0 and (Visitado[curLoc-4]==True or (curLoc-4)==goalLoc) and dfsVisitados[curLoc-4]==False:
        ag.Movimentacao('Esquerda')
        QuartoAcessivel= MoveParaNaoVisitado(ag, Visitado, goalLoc, dfsVisitados)
        if QuartoAcessivel:
            return True
        ag.Movimentacao('Direita')

    if curPos[1]-1 >0 and (Visitado[curLoc-1]==True or (curLoc-1)==goalLoc) and dfsVisitados[curLoc-1]==False:
        ag.Movimentacao('Baixo')
        QuartoAcessivel= MoveParaNaoVisitado(ag, Visitado, goalLoc, dfsVisitados)
        if QuartoAcessivel:
            return True
        ag.Movimentacao('Cima')

    return False

def EncontrarTesouro(ag, kb):
    Visitado = [False for i in range(16)] # Quartos visitados até agora 
    while(ag.EncontrarlocalizacaoAtual()!=[4, 4]):
        perceber= ag.PercebaLocalizacaoAtual()
        curPos = ag.EncontrarlocalizacaoAtual()
        curLocIndex= 4*(curPos[0]-1)+ curPos[1]-1
        Visitado[curLocIndex]=True
        
        BrisaClausula={}
        RegraFedor={}

        if perceber[0]==True: # brisa
            BrisaClausula[curLocIndex+48]=1
        else:
            BrisaClausula[curLocIndex+48]=-1
        kb.AdicionaClausula(BrisaClausula) #presença/ausência de brisa

        if perceber[1]==True: # Fedor
            RegraFedor[curLocIndex+16]=1
        else:
            RegraFedor[curLocIndex+16]=-1
        kb.AdicionaClausula(RegraFedor) # presença/ausência de fedor
            
        for NovaLocalizacao in range(16):
            if Visitado[NovaLocalizacao]==False:
                tempclauses= kb.ObterClausula()
                checkClause={NovaLocalizacao:1, NovaLocalizacao+32:1}  
                tempclauses.append(checkClause)
                if DPLLSatisfiable(tempclauses)==False:
                    # O quarto é seguro
                    noWumpus={NovaLocalizacao:-1}
                    noPit={NovaLocalizacao+32:-1}
                    kb.AdicionaClausula(noWumpus)
                    kb.AdicionaClausula(noPit)
                    dfsVisitados = [False for i in range(16)] 
                    QuartoAcessivel=MoveParaNaoVisitado(ag, Visitado, NovaLocalizacao, dfsVisitados) # Nova sala segura
                    if QuartoAcessivel:
                        break

def main():
    ag = Agent()
    kb= KnowledgeBase()
    print('Local de início: {0}'.format(ag.EncontrarlocalizacaoAtual()))
    EncontrarTesouro(ag, kb)
    print('{0} Chegou até o Tesouro'.format(ag.EncontrarlocalizacaoAtual()))
    print('Número total de vezes que a função FuncaoDPLL é chamada: {0}'.format(numberOfCalls))


if __name__=='__main__':
    main()
