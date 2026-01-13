# Hospital-das-clinicas-challenge
📌 Descrição do Projeto  O Atende+HC é um sistema de atendimento hospitalar desenvolvido em Python, com foco na simulação de serviços do Hospital das Clínicas. O projeto foi criado para fins acadêmicos e educacionais, aplicando conceitos fundamentais de programação estruturada, boas práticas de código, menus interativos no terminal, consumo de APIs públicas.

O sistema permite o gerenciamento de pacientes, agendamento de consultas, simulação de atendimento via WhatsApp, exportação de dados e consulta de endereço do hospital via API.

🎯 Objetivos

Simular o fluxo básico de atendimento de um hospital público

Aplicar validações de dados (CPF, e-mail, telefone, idade)

Trabalhar com menus hierárquicos e navegação no terminal

Utilizar APIs públicas (ViaCEP)

Exportar dados em formato JSON

Seguir boas práticas de organização e legibilidade do código

⚙️ Funcionalidades
👤 Gestão de Pacientes

Cadastro de pacientes

Busca por CPF

Listagem de pacientes

Edição de telefone e e-mail

Exclusão de registros

🗓️ Gestão de Consultas

Agendamento de consultas por CPF

Listagem de consultas agendadas

💬 Atendimento WhatsApp (Simulado)

Assistente virtual do Hospital das Clínicas

Opções de:

Marcação de consultas

Consulta de exames

Informações sobre horários e especialidades

Encaminhamento para atendente humano

📄 Exportação de Dados

Exportação de pacientes e consultas para arquivo dados_hc.json

🌐 Integração com API

Consulta do endereço do Hospital das Clínicas via API ViaCEP

🧠 Tecnologias Utilizadas

Python 3.10+

Biblioteca padrão do Python:

os

json

Biblioteca externa:

requests (para consumo de API)

📁 Estrutura do Projeto
atende-hc/
│
├── main.py            # Código principal do sistema
├── dados_hc.json      # Arquivo gerado na exportação de dados
└── README.md          # Documentação do projeto

▶️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/atende-hc.git

2️⃣ Acesse a pasta do projeto
cd atende-hc

3️⃣ Instale a dependência necessária
pip install requests

4️⃣ Execute o sistema
python main.py

📌 Requisitos

Python 3.10 ou superior

Conexão com a internet (para consulta da API ViaCEP)

🧩 Boas Práticas Aplicadas

Código modularizado por responsabilidade

Funções com docstrings explicativas

Validação de dados de entrada

Separação de menus principais e secundários

Tratamento básico de erros

Uso de if __name__ == "__main__"

⚠️ Observações Importantes

O projeto não utiliza banco de dados, os dados ficam em memória durante a execução

O atendimento via WhatsApp é uma simulação, sem integração real com a plataforma

O sistema não realiza diagnósticos médicos

👩🏻‍💻 Autora

Giovana Souza Vieira
Estudante de Análise e Desenvolvimento de Sistemas
Projeto acadêmico desenvolvido em Python

