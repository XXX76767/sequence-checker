lista_baguncada = []

# ===== ENTRADA E VALIDAÇÃO =====
# Recebe os números de atendimento digitados, um por um, e guarda os válidos.
# Três saídas possíveis: guarda / para / rejeita.
while True:
  atend = input('Digite o número do atendimento: ')  # sempre chega como TEXTO (string)

  if atend == 'keyword':   # 1ª saída: palavra de parada -> encerra o loop
    break

  else:
    isdigit = atend.isdigit()   # é só dígitos? (funciona em string) -> True/False
    tamanho = len(atend)        # quantos caracteres tem

    # 2ª saída: passa nos dois testes (só dígitos E exatamente 8) -> guarda
    # int() converte pra número: precisamos comparar por valor lá na ordenação
    # (como texto, '9' > '10' daria True, ordem de dicionário, errado)
    if isdigit == True and len(atend) == 8:
      lista_baguncada.append(int(atend))

    else:   # 3ª saída: qualquer outra coisa -> avisa e volta a pedir
      print('Formato inválido. Tente novamente.')


# ===== ORDENAÇÃO (insertion sort feito à mão) =====
# Recebe uma lista bagunçada e devolve uma nova, ordenada.
# Ideia = meu gesto no SAME: pego cada número e procuro, na pilha já ordenada,
# a posição exata onde ele se encaixa (entre um menor e um maior).
def ordenar(recebido):          # 'recebido' = parâmetro: a lista que entrar pela porta
  lista = []                    # a pilha nova, nasce vazia e vai crescer JÁ ordenada

  for num in recebido:          # for de fora: pega cada número da bagunçada
    # for de dentro: varre a pilha ordenada procurando onde 'num' se encaixa.
    # enumerate dá a posição (i) E o valor (item) de cada casa ao mesmo tempo.
    for i, item in enumerate(lista):
      if item > num:            # achei o 1º item maior que num -> a brecha é aqui
        lista.insert(i, num)    # enfia num nessa posição (empurra o maior pra frente)
        break                   # já achei o lugar, paro de procurar
    else:
      # 'else' do FOR (não do if): só roda se o for terminou SEM break.
      # Ou seja: percorreu tudo e nenhum era maior -> num é o maior de todos -> vai no fim.
      lista.append(num)

  return lista                  # entrega a pilha ordenada pra fora


resultado = ordenar(lista_baguncada)   # chama a função; lista_baguncada é o ARGUMENTO

# ===== FORMATAÇÃO PARA EXIBIÇÃO =====
# Os números viraram int pra ordenar, então perderam os zeros da frente
# (00123456 virou 123456). Aqui devolvo o formato oficial de 8 dígitos.
# int pra ordenar, texto formatado pra mostrar
formatada = []                         # lista nova pra guardar os números já formatados
for o in resultado:                    # percorre os ordenados, UM POR UM
  formatada.append(str(o).zfill(8))    # str() vira texto, zfill(8) enche de zero à esquerda até ter 8

print(formatada)                       # mostra a lista ordenada e com os 8 dígitos completos