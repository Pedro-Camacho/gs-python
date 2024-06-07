temperaturas = []
phs = []
turbidez = []
datas = [] 
nomes = []


def inserir_dados():
    nomes.append(input("Digite o nome de quem realiza os registros:"))
    datas.append(input("Digite a data de registro dd/mm/aaaa"))
    temperaturas.append(input("Digite o valor da temperatura"))
    phs.append(input("Digite o ph registrado"))
    turb_atual=int(input("Digite o valor da turbidez entre 0 a 5"))
    while turb_atual >5 and turb_atual<0:
        turb_atual=int(input("Digite o valor da turbidez entre 0 a 5"))
    turbidez.append(turb_atual)


def acha_index(lista,elemento):
    for i in range(len(lista)):
        if elemento == lista[i]:
            return i


def analiza_temperatura(temperatura):
    print("Analise temperatura:")
    if temperatura > 26:
        print(f"Temperatura alta isso pode afetar os peixes! ({temperatura}°)")
    elif temperatura <20:
        print(f"Temperatura muito abaixo do normal ({temperatura}°)")
    else:
        print(f'Temperatura estável {temperatura}')

def analiza_ph(ph):
    print("Analise do Ph:")
    if ph >0 and ph<4:
        print(f"Ph em estado critico ({ph})")
    elif ph>4 and ph<6:
        print(f"ph levemente perigoso ({ph})")
    elif ph>6 and ph<9:
        print(f"Ph na faixa desejada ({ph})")
    elif ph>9 and ph<11:
        print(f"ph levemente perigoso ({ph})")
    elif ph>11 and ph<14:
        print(f"Ph em estado critico ({ph})")
    else:
        print("Valor de ph não aceito por favor editar")

def analiza_turbidez(turbi):
    print("Analise de turbidez:")
    if turbi == 1:
        print("Agua  muita clara")
    elif turbi == 2:
        print("Agua clara")
    elif turbi == 3:
        print("Agua media")
    elif turbi == 4:
        print("Agua turva")
    elif turbi == 5:
        print("Agua muito turva")

def analizar_dados(data):
    analizando=acha_index(datas, data)
    temp_analizando = temperaturas[analizando]
    ph_analizando = phs[analizando]
    turb_analizando = turbidez[analizando]
    data_analizada = datas[analizando]
    nome_analizado = nomes[nome_analizado]

    print(f"Aqui está o relatório feito por {nome_analizado} na data {data_analizada}")
    analiza_temperatura(temp_analizando)
    analiza_ph(ph_analizando)
    analiza_turbidez(turb_analizando)

def editar_dados(data):
    editando=acha_index(datas, data)
    novo_nome = input("Digite o novo Nome do Registro:")
    nomes[editando]=novo_nome
    nova_temperatura = input("Digite o nova temperatura:")
    temperaturas[editando]=nova_temperatura
    novo_ph = input("Digite o novo valor do ph:")
    phs[editando] = novo_ph
    nova_turb = input("Digite o valor de turbidez atualizado:")
    turbidez[editando] = nova_turb 

print("bem vindo ao programa de registro de dados da qualidade de agua")

