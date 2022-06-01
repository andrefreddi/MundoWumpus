# Mundo Wumpus
Objetivo criar um mundo Wumpus, André F. e Willian C.

Para iniciarmos vamos rodar nosso código antes de tentarmos entender.

![20220531_232241](https://user-images.githubusercontent.com/52337680/171315247-c903c1ce-4f00-4608-afb7-9c91bd32ff8b.gif)

Bom com uso de Algoritmo DPLL temos um total de 2070 chamadas que faz a resolução do nosso problema.

Algoritimo DPLL segundo a [Wiki](https://en.wikipedia.org/wiki/DPLL_algorithm)

"O algoritmo DPLL/Davis-Putnam-Logemann-Loveland é um algoritmo completo baseado em backtracking (re-leitura ou voltar atrás) para decidir a satisfatibilidade das fórmulas de lógica proposicional na forma normal clausal, isto é, para solucionar o problema SAT."

O caminho final como resultado temos o log:
```
Local de início: [1, 1]
Medida tomada: Cima, Localização atual [1, 2]
Medida tomada: Baixo, Localização atual [1, 1]
Medida tomada: Direita, Localização atual [2, 1]
Medida tomada: Esquerda, Localização atual [1, 1]
Medida tomada: Cima, Localização atual [1, 2]
Medida tomada: Baixo, Localização atual [1, 1]
Medida tomada: Direita, Localização atual [2, 1]
Medida tomada: Cima, Localização atual [2, 2]
Medida tomada: Esquerda, Localização atual [1, 2]
Medida tomada: Baixo, Localização atual [1, 1]
Medida tomada: Direita, Localização atual [2, 1]
Medida tomada: Esquerda, Localização atual [1, 1]
Medida tomada: Cima, Localização atual [1, 2]
Medida tomada: Direita, Localização atual [2, 2]
Medida tomada: Cima, Localização atual [2, 3]
Medida tomada: Baixo, Localização atual [2, 2]
Medida tomada: Esquerda, Localização atual [1, 2]
Medida tomada: Baixo, Localização atual [1, 1]
Medida tomada: Direita, Localização atual [2, 1]
Medida tomada: Esquerda, Localização atual [1, 1]
Medida tomada: Cima, Localização atual [1, 2]
Medida tomada: Direita, Localização atual [2, 2]
Medida tomada: Cima, Localização atual [2, 3]
Medida tomada: Cima, Localização atual [2, 4]
Medida tomada: Esquerda, Localização atual [1, 4]
Medida tomada: Direita, Localização atual [2, 4]
Medida tomada: Baixo, Localização atual [2, 3]
Medida tomada: Baixo, Localização atual [2, 2]
Medida tomada: Direita, Localização atual [3, 2]
Medida tomada: Cima, Localização atual [3, 3]
Medida tomada: Cima, Localização atual [3, 4]
Medida tomada: Esquerda, Localização atual [2, 4]
Medida tomada: Esquerda, Localização atual [1, 4]
Medida tomada: Direita, Localização atual [2, 4]
Medida tomada: Baixo, Localização atual [2, 3]
Medida tomada: Direita, Localização atual [3, 3]
Medida tomada: Baixo, Localização atual [3, 2]
Medida tomada: Esquerda, Localização atual [2, 2]
Medida tomada: Esquerda, Localização atual [1, 2]
Medida tomada: Baixo, Localização atual [1, 1]
Medida tomada: Direita, Localização atual [2, 1]
Medida tomada: Esquerda, Localização atual [1, 1]
Medida tomada: Cima, Localização atual [1, 2]
Medida tomada: Direita, Localização atual [2, 2]
Medida tomada: Direita, Localização atual [3, 2]
Medida tomada: Cima, Localização atual [3, 3]
Medida tomada: Esquerda, Localização atual [2, 3]
Medida tomada: Cima, Localização atual [2, 4]
Medida tomada: Direita, Localização atual [3, 4]
Medida tomada: Esquerda, Localização atual [2, 4]
Medida tomada: Esquerda, Localização atual [1, 4]
Medida tomada: Direita, Localização atual [2, 4]
Medida tomada: Baixo, Localização atual [2, 3]
Medida tomada: Direita, Localização atual [3, 3]
Medida tomada: Baixo, Localização atual [3, 2]
Medida tomada: Direita, Localização atual [4, 2]
Medida tomada: Esquerda, Localização atual [3, 2]
Medida tomada: Cima, Localização atual [3, 3]
Medida tomada: Cima, Localização atual [3, 4]
Medida tomada: Esquerda, Localização atual [2, 4]
Medida tomada: Esquerda, Localização atual [1, 4]
Medida tomada: Direita, Localização atual [2, 4]
Medida tomada: Baixo, Localização atual [2, 3]
Medida tomada: Baixo, Localização atual [2, 2]
Medida tomada: Esquerda, Localização atual [1, 2]
Medida tomada: Baixo, Localização atual [1, 1]
Medida tomada: Direita, Localização atual [2, 1]
Medida tomada: Esquerda, Localização atual [1, 1]
Medida tomada: Cima, Localização atual [1, 2]
Medida tomada: Direita, Localização atual [2, 2]
Medida tomada: Cima, Localização atual [2, 3]
Medida tomada: Cima, Localização atual [2, 4]
Medida tomada: Direita, Localização atual [3, 4]
Medida tomada: Baixo, Localização atual [3, 3]
Medida tomada: Baixo, Localização atual [3, 2]
Medida tomada: Direita, Localização atual [4, 2]
Medida tomada: Baixo, Localização atual [4, 1]
Medida tomada: Cima, Localização atual [4, 2]
Medida tomada: Cima, Localização atual [4, 3]
Medida tomada: Cima, Localização atual [4, 4]
[4, 4] Chegou até o Tesouro
```

Codigo: 

Iniciamos com o Mundo do Wumpus

![image](https://user-images.githubusercontent.com/52337680/171315907-3daf9c69-72db-4a47-bff3-8c98a50d1d2e.png)

Iniciamos os Índices e uma verificação se tem os Abismos e Wumpus.

![image](https://user-images.githubusercontent.com/52337680/171315954-f7107f96-dc44-4b90-af98-b5d9a0798839.png)

A função executa uma ação e retorna se o Agente está vivo, fazendo uma verificação.

![image](https://user-images.githubusercontent.com/52337680/171316451-3bac5adb-08c2-43b0-88f2-031c6b68e88d.png)


Encontra os quartos ao lado do Agente (você).

![image](https://user-images.githubusercontent.com/52337680/171316493-6dad66df-c9e6-4ecf-aa6c-d8ffb1457dc7.png)


Verifica a posição atual e retorna se existe Brisa ou Fedor, Lembrando que próximos a Abismos existe brisa e Próximo ao Wumpus existe Fedor.

![image](https://user-images.githubusercontent.com/52337680/171316781-eaff2b78-ec4d-4e79-80c4-953547bf0262.png)

Define as regras do Wumpus e Abismo.

![image](https://user-images.githubusercontent.com/52337680/171317011-e31b516d-b4b2-485b-9aa6-d8b98ad2d8f3.png)

Regras do Fedor do Wumpus.

![image](https://user-images.githubusercontent.com/52337680/171317050-2be84ebf-d3a6-4e18-9dea-98d88117c681.png)

Regras Brisa do Abismo.

![image](https://user-images.githubusercontent.com/52337680/171317090-cba51892-dc21-474e-bb90-8c3088d0640d.png)


Sem Abismos e Wumpus na localização [1,1] onde o jogador começa.

![image](https://user-images.githubusercontent.com/52337680/171317187-2b6b49be-f126-4b94-ba2d-629ec8e84378.png)

Seleciona e encontra os Símbolos puros e as clausulas unitárias para uso do algorítimo DPLL.

![image](https://user-images.githubusercontent.com/52337680/171317419-6da57967-0f81-4bf7-ba4b-8a0f47735993.png)

![image](https://user-images.githubusercontent.com/52337680/171317430-f3752115-672d-4dc0-9746-37fdf9fc4b49.png)


Função DPLL fazendo uso das clausulas, símbolos e modelos.

![image](https://user-images.githubusercontent.com/52337680/171317723-e9ce8fc4-ab42-4d83-8277-5320a5b68734.png)

Movimenta para salas não visitadas, busca possibilidade.

![image](https://user-images.githubusercontent.com/52337680/171317821-7638abd8-8186-4c5b-ba6f-f95854e78547.png)


Função que encontra o tesouro.

![image](https://user-images.githubusercontent.com/52337680/171318100-55a65904-f318-453d-8965-53dbd549b2cd.png)

E por fim retorna as informações na tela.

![image](https://user-images.githubusercontent.com/52337680/171318197-579f77fc-079b-4339-b19f-ce6091905fae.png)

