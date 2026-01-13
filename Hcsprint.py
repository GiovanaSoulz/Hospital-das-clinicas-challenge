import os
import json
import requests

# ========================
# FUNÇÕES DE SUPORTE
# ========================

def limpar_tela():
    """Limpa o terminal conforme o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa a execução até o usuário pressionar ENTER."""
    input("\nPressione ENTER para continuar...")


def cabecalho(titulo):
    """Mostra um título formatado."""
    limpar_tela()
    print(f"\n{'=' * 10} {titulo} {'=' * 10}\n")


# ========================
# FUNÇÕES DE VALIDAÇÃO
# ========================
9 
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11


def validar_email(email):
    return "@" in email and "." in email


def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) >= 10


def validar_idade(idade):
    return idade.isdigit() and int(idade) > 0


# ========================
# FUNÇÕES DE PACIENTES
# ========================

def cadastrar_paciente(nomes, idades, cpfs, telefones, emails):
    cabecalho("Cadastro de Paciente")

    nome = input("Nome completo: ").strip()
    idade = input("Idade: ").strip()
    cpf = input("CPF (apenas números): ").strip()
    telefone = input("Telefone com DDD: ").strip()
    email = input("E-mail: ").strip()

    if not validar_idade(idade):
        print("Idade inválida.")
        return
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return
    if not validar_telefone(telefone):
        print("Telefone inválido.")
        return
    if not validar_email(email):
        print("E-mail inválido.")
        return

    nomes.append(nome)
    idades.append(int(idade))
    cpfs.append(cpf)
    telefones.append(telefone)
    emails.append(email)

    print("\nPaciente cadastrado com sucesso!")


def buscar_paciente(nomes, idades, cpfs, telefones, emails):
    cabecalho("Buscar Paciente")
    cpf_busca = input("Informe o CPF: ").strip()

    for i in range(len(cpfs)):
        if cpfs[i] == cpf_busca:
            print(f"\nPaciente encontrado:")
            print(f"Nome: {nomes[i]}")
            print(f"Idade: {idades[i]}")
            print(f"CPF: {cpfs[i]}")
            print(f"Telefone: {telefones[i]}")
            print(f"E-mail: {emails[i]}")
            return
    print("Paciente não encontrado.")


def listar_pacientes(nomes, idades, cpfs, telefones, emails):
    cabecalho("Lista de Pacientes")
    if not nomes:
        print("Nenhum paciente cadastrado.")
        return

    for i in range(len(nomes)):
        print(f"{i+1}. {nomes[i]} | Idade: {idades[i]} | CPF: {cpfs[i]} | "
              f"Tel: {telefones[i]} | E-mail: {emails[i]}")


def editar_paciente(cpfs, telefones, emails, nomes):
    cabecalho("Editar Paciente")
    cpf = input("CPF do paciente: ").strip()

    for i in range(len(cpfs)):
        if cpfs[i] == cpf:
            novo_tel = input("Novo telefone: ").strip()
            novo_email = input("Novo e-mail: ").strip()

            if validar_telefone(novo_tel) and validar_email(novo_email):
                telefones[i] = novo_tel
                emails[i] = novo_email
                print("Dados atualizados com sucesso!")
            else:
                print("Dados inválidos.")
            return
    print("Paciente não encontrado.")


def excluir_paciente(cpfs, nomes, idades, telefones, emails):
    cabecalho("Excluir Paciente")
    cpf = input("CPF do paciente a excluir: ").strip()

    for i in range(len(cpfs)):
        if cpfs[i] == cpf:
            print(f"Excluindo paciente: {nomes[i]}")
            nomes.pop(i)
            idades.pop(i)
            cpfs.pop(i)
            telefones.pop(i)
            emails.pop(i)
            print("Paciente excluído com sucesso!")
            return
    print("Paciente não encontrado.")


# ========================
# FUNÇÕES DE CONSULTAS
# ========================

def agendar_consulta(cpfs, nomes, agendamentos):
    cabecalho("Agendar Consulta")
    cpf = input("Informe o CPF do paciente: ").strip()

    for i in range(len(cpfs)):
        if cpfs[i] == cpf:
            data = input("Data da consulta (DD/MM/AAAA): ").strip()
            hora = input("Horário (HH:MM): ").strip()
            especialidade = input("Especialidade: ").strip()

            agendamento = f"{nomes[i]} | CPF: {cpf} | Data: {data} | Hora: {hora} | {especialidade}"
            agendamentos.append(agendamento)

            print("\nConsulta agendada com sucesso!")
            return

    print("Paciente não encontrado.")


def listar_agendamentos(agendamentos):
    cabecalho("Agendamentos")
    if not agendamentos:
        print("Nenhum agendamento registrado.")
    else:
        for i, ag in enumerate(agendamentos, start=1):
            print(f"{i}. {ag}")


# ========================
# ATENDIMENTO WHATSAPP
# ========================

def atendimento_whatsapp():
    cabecalho("Atendimento WhatsApp - Atende+HC")
    print("Olá! Eu sou a assistente virtual Helena do Hospital das Clínicas.")
    print("Como posso te ajudar hoje?\n")

    while True:
        print("1 - Marcar consulta")
        print("2 - Consultar resultados de exames")
        print("3 - Informações sobre horários e especialidades")
        print("4 - Falar com atendente humano")
        print("5 - Encerrar atendimento\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            print("\nAcesse o portal do paciente para agendar consultas.")
        elif opcao == "2":
            print("\nSeus exames estão disponíveis no app 'HC Paciente' ou no site do HC.")
        elif opcao == "3":
            print("\nFuncionamento: Seg. a Sex. das 7h às 19h | Especialidades: Clínica Geral, Pediatria, Cardiologia, Ortopedia, Dermatologia.")
        elif opcao == "4":
            print("\nUm atendente humano entrará em contato em instantes.")
        elif opcao == "5":
            print("\nAtendimento encerrado. Obrigado por usar o Atende+HC!")
            break
        else:
            print("Opção inválida.")

        pausar()
        cabecalho("Atendimento WhatsApp - Atende+HC")


# ========================
# EXPORTAR DADOS
# ========================

def exportar_dados_json(nomes, idades, cpfs, telefones, emails, agendamentos):
    cabecalho("Exportar Dados JSON")

    dados = {
        "pacientes": [
            {"nome": n, "idade": i, "cpf": c, "telefone": t, "email": e}
            for n, i, c, t, e in zip(nomes, idades, cpfs, telefones, emails)
        ],
        "agendamentos": agendamentos
    }

    try:
        with open("dados_hc.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print("Dados exportados com sucesso para 'dados_hc.json'!")
    except Exception as e:
        print(f"Erro ao exportar: {e}")


# ========================
# API DE ENDEREÇO (CEP)
# ========================

def mostrar_endereco_hospital():
    cabecalho("Endereço do Hospital das Clínicas")
    cep = "05403000"
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            print(f"Logradouro: {dados.get('logradouro')}")
            print(f"Bairro: {dados.get('bairro')}")
            print(f"Cidade: {dados.get('localidade')} - {dados.get('uf')}")
            print(f"CEP: {dados.get('cep')}")
            print("\nReferência: Entrada principal — Av. Dr. Enéas de Carvalho Aguiar, 255")
        else:
            print("Erro ao consultar o endereço.")
    except requests.exceptions.RequestException:
        print("Erro de conexão. Verifique sua internet.")


# ========================
# MENUS SECUNDÁRIOS
# ========================

def menu_pacientes(nomes, idades, cpfs, telefones, emails):
    while True:
        cabecalho("Menu Pacientes")
        print("1. Cadastrar paciente")
        print("2. Buscar paciente")
        print("3. Listar pacientes")
        print("4. Editar paciente")
        print("5. Excluir paciente")
        print("6. Voltar\n")

        opc = input("Escolha: ").strip()

        if opc == "1":
            cadastrar_paciente(nomes, idades, cpfs, telefones, emails)
        elif opc == "2":
            buscar_paciente(nomes, idades, cpfs, telefones, emails)
        elif opc == "3":
            listar_pacientes(nomes, idades, cpfs, telefones, emails)
        elif opc == "4":
            editar_paciente(cpfs, telefones, emails, nomes)
        elif opc == "5":
            excluir_paciente(cpfs, nomes, idades, telefones, emails)
        elif opc == "6":
            break
        else:
            print("Opção inválida.")
        pausar()


def menu_consultas(cpfs, nomes, agendamentos):
    while True:
        cabecalho("Menu Consultas")
        print("1. Agendar consulta")
        print("2. Listar agendamentos")
        print("3. Voltar\n")

        opc = input("Escolha: ").strip()

        if opc == "1":
            agendar_consulta(cpfs, nomes, agendamentos)
        elif opc == "2":
            listar_agendamentos(agendamentos)
        elif opc == "3":
            break
        else:
            print("Opção inválida.")
        pausar()


# ========================
# MENU PRINCIPAL
# ========================

def menu_principal():
    nomes, idades, cpfs, telefones, emails, agendamentos = [], [], [], [], [], []

    while True:
        cabecalho("Menu Principal - Atende+HC")
        print("1. Menu Pacientes")
        print("2. Menu Consultas")
        print("3. Exportar dados JSON")
        print("4. Atendimento WhatsApp")
        print("5. Endereço do Hospital")
        print("6. Encerrar\n")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            menu_pacientes(nomes, idades, cpfs, telefones, emails)
        elif opcao == "2":
            menu_consultas(cpfs, nomes, agendamentos)
        elif opcao == "3":
            exportar_dados_json(nomes, idades, cpfs, telefones, emails, agendamentos)
        elif opcao == "4":
            atendimento_whatsapp()
        elif opcao == "5":
            mostrar_endereco_hospital()
        elif opcao == "6":
            print("\nEncerrando o sistema. Obrigado por usar o Atende+HC!")
            break
        else:
            print("Opção inválida.")
        pausar()


# ========================
# EXECUÇÃO
# ========================
if __name__ == "__main__":
    menu_principal()
