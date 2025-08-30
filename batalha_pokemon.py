import requests

def pegar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

def pegar_tipo(url_tipo):
    resposta = requests.get(url_tipo)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

def buscar_pokemon(nome):
    dados = pegar_pokemon(nome)
    if dados:
        print(f"\nNome: {dados['name'].title()}")
        print(f"ID: {dados['id']}")
        print("Tipos:")
        for t in dados["types"]:
            print(f" - {t['type']['name'].title()}")
        print("Habilidades:")
        for h in dados["abilities"]:
            print(f" - {h['ability']['name'].title()}")
    else:
        print("Pokémon não encontrado!")


while True:
    # POKÉMON DE ATAQUE
    nome_atk = input("\nDigite o nome do Pokémon de ataque (ou 'sair' para encerrar): ")
    if nome_atk.lower() == "sair":
        break
    pokemon_atk = pegar_pokemon(nome_atk)

    if not pokemon_atk:
        print("Pokémon de ataque não encontrado!")
        continue

    tipos_atk = [pegar_tipo(t['type']['url']) for t in pokemon_atk['types']]

    print("\n--- Tipos do Pokémon de Ataque ---")
    for tipo in tipos_atk:
        print("Tipo:", tipo['name'])
        for tipodano in tipo['damage_relations']['double_damage_to']:
            print("  Super efetivo contra:", tipodano['name'])

    # POKÉMON DE DEFESA
    nome_def = input("\nDigite o nome do Pokémon de defesa (ou 'sair' para encerrar): ")
    if nome_def.lower() == "sair":
        break
    pokemon_def = pegar_pokemon(nome_def)

    if not pokemon_def:
        print("Pokémon de defesa não encontrado!")
        continue

    tipos_def = [pegar_tipo(t['type']['url']) for t in pokemon_def['types']]

    print("\n--- Tipos do Pokémon de Defesa ---")
    for tipo in tipos_def:
        print("Tipo:", tipo['name'])

    # DANO
    try:
        dano = int(input('\nQuanto de dano vai sofrer? '))
    except ValueError:
        print("Digite um valor numérico para o dano!")
        continue

    dano_final = dano

    # Checa cada tipo de ataque contra cada tipo de defesa
    for tipo_atk in tipos_atk:
        for tipo_damage in tipo_atk['damage_relations']['double_damage_to']:
            for tipo_def in tipos_def:
                if tipo_damage['name'] == tipo_def['name']:
                    dano_final *= 2  # dano dobrado

    print(f"\n{nome_atk.title()} causou {dano_final} de dano em {nome_def.title()}!\n")
