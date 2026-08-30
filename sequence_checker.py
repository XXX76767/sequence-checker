lista_baguncada = []

while True:
  atend = input('Digite o número do atendimento: ')  

  if atend == 'keyword': 
    break
  else:
    isdigit = atend.isdigit()   
    tamanho = len(atend) 

   
    if isdigit == True and len(atend) == 8:
      lista_baguncada.append(int(atend))
    else:   # 3ª saída: qualquer outra coisa -> avisa e volta a pedir
      print('Formato inválido. Tente novamente.')

def ordenar(recebido):        
  lista = []   
  for num in recebido:        
    for i, item in enumerate(lista):
      if item > num:       
        lista.insert(i, num)    
        break 
    else:
      lista.append(num)

  return lista                 

resultado = ordenar(lista_baguncada)  

formatada = []                     
for o in resultado:                
  formatada.append(str(o).zfill(8))  

print(formatada)                   