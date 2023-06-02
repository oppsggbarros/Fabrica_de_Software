maior_temp = -1
mneor_temp = 9999
temperatura = 0
menor_mes = 0
menor_ano = 0
maio_mes = 0
maior_ano = 0
temp = []
while temperatura != 'x' :
    temperatura = input("Digite a temperatura ou digite x para encerrar ")
    if temperatura == 'x':
        print("Fim!")
        break
    mes = input("Digite o Mês ")
    mes = int(mes)
    ano = input("Digite o ano ")
    ano = int(ano)
    temperatura = int(temperatura)
    temp.append(temperatura)
    if temperatura < mneor_temp :
        mneor_temp = temperatura
        menor_mes = mes
        menor_ano = ano
    if temperatura > maior_temp :
        maior_temp = temperatura
        maio_mes = mes
        maior_ano = ano
media = sum(temp)/len(temp)
print("A maior temperatura  foi %d no ano de %d no mês %d"%(maior_temp,maior_ano,maio_mes))
print("A menor temperatura  foi %d no ano de %d no mês %d"%(mneor_temp,menor_ano,menor_mes))
print("A mediafoi = ",media)
   