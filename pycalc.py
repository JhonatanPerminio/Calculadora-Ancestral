# A calculadora Ancestral de Divictus!

while True:
    print('Saudações viajante! Vejo que está perdido, com problemas matemáticos!')
    diga = input('Estou certo? Diga, sim ou não? ')

    if diga.lower() == 'não':
        print('Ok então, convencido, até mais ver!')
        break  # Sai do loop

    else:
        print('Eu sempre estou!')
    #Verificação de idade
    ver_idade=int(input('Antes de prosseguirmos jovem mafagafo, deixe-me saber sua idade:'))
    if ver_idade >=18:
        print('Muito bem, és um transeunte experiênte, prosseguiremos...')
    else:
        print('Lamento, jovem mancebo, ainda és apenas uma criança, e os conhecimentos aqui não são para você, retorne quando estiver mais velho!')
        break

    #Entrada dos números
    num=input('Agora, nobre viajante, digite um número, qualquer número: ')
    operator=input('Agora, digitarás um destes operadores (+,-,*,/,**): ')
    num2=input('Digite aqui um outro número: ')
    num=int(num)
    num2=int(num2)

    if operator=='+':
        print('Eis o estupendo resultado!:', num+num2)
        print('Veja só, uma Soma!')
    elif operator=='-':
        print('Eis o magnífico resultado!:', num-num2)
        print('Quem diria? Uma Subtração!')
    elif operator=='*':
        print('Eis o resultado supimpa!:', num*num2)
        print('Minha favorita, a Multiplicação!')
    elif operator=='/':
        print('Eis o inenarrável resultado!:', num/num2)
        print('Dividir e conquistar, não é?')
    elif operator=='**':
        print('Eis o glorioso resultado!:', num**num2)
        print('Tá Potente!')

    print() # Linha vazia
    prosseguir=input('Mágico, não é? Deseja fazer mais alguns cálculos? Diga-me, sim ou não? ')
    if prosseguir.lower()=='não':
        print('Pois bem, faça uma boa viagem, viajante!')
        break
        #bye bye!
