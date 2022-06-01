class Agent:
    def __init__(self):
        self.MundoWumpus = [
                 ['','','B',''], # Casa [1,1] - [4,1]
                 ['','','',''], # Casa [1,2] - [4,2] 
                 ['W','','',''], # Casa [1,3] - [4,3]
                 ['','','',''],  # Casa [1,4] - [4,4]
                ]
        self.__curLoc = [1,1]
        self.__isAlive = True
        self.__hasExited = False

    def IndicesParaLocalizacao(self,loc):
        x,y = loc
        i,j = y-1, x-1
        return i,j

    def VerificaSeTemAbsimoWumpus(self):
        Agent = self.MundoWumpus
        i,j = self.IndicesParaLocalizacao(self.__curLoc)
        if 'B' in Agent[i][j] or 'W' in Agent[i][j]:
            print(Agent[i][j])
            self.__isAlive = False
            print('Você morreu')
        return self.__isAlive

    def Movimentacao(self,action):
        validActions = ['Cima','Baixo','Esquerda','Direita']
        assert action in validActions, 'Ação invalida'
        if self.__isAlive == False:
            print('A ação não pode ser executada. Voce morreu no local:{0}'.format(self.__curLoc))
            return False
        if self.__hasExited == True:
            print('A ação não pode ser executada. Voce pegou o tesouro.'.format(self.__curLoc))
            return False

        index = validActions.index(action)
        MovimentacaoValida = [[0,1],[0,-1],[-1,0],[1,0]]
        move = MovimentacaoValida[index]
        newLoc = []
        for v, inc in zip(self.__curLoc,move):
            z = v + inc #aumentar o índice de localização
            z = 4 if z>4 else 1 if z<1 else z #Certifique-se de que o índice esteja entre 1 e 4
            newLoc.append(z)
        self.__curLoc = newLoc
        print('Medida tomada: {0}, Localização atual {1}'.format(action,self.__curLoc))
        if self.__curLoc[0]==4 and self.__curLoc[1]==4:
            self.__hasExited=True
        return self.VerificaSeTemAbsimoWumpus()
    
    def EncontraQuartoProximos(self):
        cLoc = self.__curLoc
        MovimentacaoValida = [[0,1],[0,-1],[-1,0],[1,0]]
        adjCasas = []
        for vM in MovimentacaoValida:
            room = []
            valid = True
            for v, inc in zip(cLoc,vM):
                z = v + inc
                if z<1 or z>4:
                    valid = False
                    break
                else:
                    room.append(z)
            if valid==True:
                adjCasas.append(room)
        return adjCasas
                
        
    def PercebaLocalizacaoAtual(self):
        Brisa, Fedor = False, False
        Agent = self.MundoWumpus
        if self.__isAlive == False:
            print('Voce não pode perceber. Morreu no local:{0}'.format(self.__curLoc))
            return [None,None]
        if self.__hasExited == True:
            print('Voce não pode perceber. Pegou o tesouro.'.format(self.__curLoc))
            return [None,None]

        adjCasas = self.EncontraQuartoProximos()
        for room in adjCasas:
            i,j = self.IndicesParaLocalizacao(room)
            if 'B' in Agent[i][j]:
                Brisa = True
            if 'W' in Agent[i][j]:
                Fedor = True
        return [Brisa,Fedor]
    
    def EncontrarlocalizacaoAtual(self):
        return self.__curLoc

def main():
    ag = Agent()
    print('curLoc',ag.EncontrarlocalizacaoAtual())
    print('Percepcao [Brisa, Fedor] :',ag.PercebaLocalizacaoAtual())
    ag.Movimentacao('Direita')
    print('Percepcao',ag.PercebaLocalizacaoAtual())
    ag.Movimentacao('Direita')
    print('Percepcao',ag.PercebaLocalizacaoAtual())
    ag.Movimentacao('Direita')
    print('Percepcao',ag.PercebaLocalizacaoAtual())
    ag.Movimentacao('Cima')
    print('Percepcao',ag.PercebaLocalizacaoAtual())
    ag.Movimentacao('Cima')
    print('Percepcao',ag.PercebaLocalizacaoAtual())
    ag.Movimentacao('Cima')
    print('Percepcao',ag.PercebaLocalizacaoAtual())


if __name__=='__main__':
    main()
