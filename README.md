# sequence-checker

## O que faz
Organiza números de 8 dígitos bagunçados em uma ordem sequencial numérica.

## Como faz
1. Recebe os números de atendimento (8 dígitos cada) e valida cada um — precisa ter exatamente 8 dígitos e conter apenas números.
2. Ordena os atendimentos do menor para o maior.
3. Exibe a lista ordenada no formato padrão de 8 dígitos, preservando os zeros à esquerda.

## Motivação
Nasceu inspirado diretamente no processo real que eu executava no setor do S.A.M.E, no hospital Unimed Piracicaba. 
Lá eu organizava prontuários, onde cada um era único e possuía um número de atendimento. 
Minha tarefa era colocar um montante desses prontuários em ordem sequencial.

## Nota técnica
A ordenação foi implementada manualmente (algoritmo de inserção / insertion sort), em vez de usar a função `sorted()` pronta do Python. 
A escolha foi proposital: entender e construir a lógica de ordenação do zero, em vez de apenas chamá-la, em prol do aprendizado próprio. 

## Como usar

Feito em Python. Requer Python 3 instalado.

1. Clone o repositório:
```
git clone https://github.com/XXX76767/sequence-checker.git
```

2. Entre na pasta:
```
cd sequence-checker
```

3. Rode o script:
```
python sequence_checker.py
```

Digite os números de atendimento (8 dígitos cada). Digite `keyword` para encerrar e ver a lista ordenada.