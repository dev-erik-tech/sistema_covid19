# sistema_covid19
Um programa para comparar, após os exames, se o paciente está infectado ou não pela COVID-19

Este é um programa que faz leitura da entrada padrão o nome de dois
arquivos texto a serem processados. O primeiro arquivo contém em cada linha o nome e o
RNA de um coronavírus identificado, separados por um “#”. O segundo arquivo representa uma
população de uma cidade, contendo em cada linha o CPF e o DNA de uma pessoa, separados
por um “#”. Para cada coronavírus processe o arquivo da população, indivíduo por indivíduo,
observando que contenha núcleos base nas mesmas posições do vírus. Os indivíduos com
mais de cinquenta por cento de igualdade, letra a letra, é tida como possivelmente infectada.
Escreva na saída padrão o nome de um coronavírus e todos os CPF daquelas pessoas
possivelmente infectadas por aquele coronavírus. Por simplicidade, suponha que o RNA e DNA
sempre possuam mesmo comprimento.
Nossa definição de RNA: É uma string de comprimento maior que zero contendo os núcleos
base representados apenas por letras “A”, “G”, “C”, “U”.
Nossa definição de DNA: É uma string de comprimento maior que zero contendo os núcleos
base representados apenas por letras “A”, “G”, “C”, “T”.
