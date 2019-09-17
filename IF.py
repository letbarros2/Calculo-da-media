#Escreva um programa para ler duas notas de um aluno, calcular a média e
#informar se ele foi aprovado ou não (a média é 7.0);

nota1=float(input("digite a sua primeira nota :"))
nota2=float(input("digite a segunda nota:"))

media=(nota1+nota2)/2
if media>=7:
 print("O ALUNO FOI APROVADOOOOOOO")
else:
 print("TENTE O ANO QUE VEM")

##A idade mínima para aposentadoria é 60. Escreva um programa que leia o ano atual o ano de nascimento e verifique se essa pessoa pode se aposentar;

#Altere o segundo exercício para calcular o tempo que falta para o usuário se aposentar, caso ele tenha idade menor que 60;

anoa=int(input("digite o ano atual:"))
anon=int(input("digite o ano de nascimento:"))
idade=(anoa-anon)
if idade>=60:
 print(" pode se aposentar")
else:
 print("não pode se aposentar")

 
