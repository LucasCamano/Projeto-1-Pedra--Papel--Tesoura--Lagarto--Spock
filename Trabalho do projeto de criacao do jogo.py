# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:09:06 2015

@author: lucascamano
"""

from random import randint
        

y = randint(0,4)
       
papel = 0
pedra = 1
tesoura = 2
spock = 3
lagarto = 4 

x = 0

jogador = 0
computador = 0 


while jogador <= 3 and computador <= 3:
    
    x = int(input('venha jogar o melhor jogo do mundo O jogo sera computador x jogador Vence o jogo a pessoa que fizer 3 vitorias seguidas''Papel:0'  'Pedra: Tesoura:2' 'Spock:3' 'Lagarto:4\n'))    
     
    if x == 0 and y == 1:
        print('boa escolha')
        jogador += 1

    elif x == 0 and y == 2 :
        print('otima jogada')
        computador += 1
        
    elif x == 0 and y == 3:
        print('boa escolha')
        jogador += 1
        
    elif x == 0 and y == 4:
        print('otima escolha')
        computador += 1
        
    elif x == 1 and y == 0:
        print('otima escolha')
        computador += 1
    
    elif x == 1 and y == 2:
        print('boa escolha')
        jogador += 1
        
    elif x == 1 and y == 3:
        print('otima escolha')
        computador += 1
        
    elif x == 1 and y == 4:
        print('boa escolha')
        jogador += 1
        
    elif x == 2 and y == 0:
        print('boa escolha')
        jogador += 1
    
    elif x == 2 and y == 1:
        print('otima escolha')
        computador += 1
        
    elif x == 2 and y == 3:
        print('otima jogada')
        computador += 1
        
    elif x == 2 and y == 4:
        print('boa escolha')
        jogador += 1
        
    elif x == 3 and y == 0:
        print('otima escolha')
        computador += 1
    
    elif x == 3 and y == 1:
        print('boa escolha')
        jogador += 1
        
    elif x == 3 and y == 2 :
        print('boa escolha')
        jogador += 1
        
    elif x == 3 and y == 4:
       print('otima escolha')
       computador += 1
       
    elif x == 4 and y == 0 :
        print('boa escolha')
        jogador += 1
    
    elif x == 4 and y == 1:
       print('otima escolha')
       computador += 1
       
    elif x == 4 and y == 2:
       print('otima escolha')
       computador += 1
       
    elif x == 4 and y == 3:
       print('boa escolha')
       jogador += 1
       
    elif x == y: 
        print('a escolha foi igual')
    
    elif x >= 5 or x < 0:
        print('essa opcao nao existe, jogue de novo.')
        
        print('placar: voce', jogador , 'computador' , computador)
        
        
        
        
if jogador == 3:
    print('Parabens, voce venceu o jogo')
            
if computador == 3:
    print('computador ganhou')
        
        