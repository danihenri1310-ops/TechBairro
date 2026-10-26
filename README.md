# TechBairro

**Versão atual: 3.3.2**

A TechBairro é um programa de cadastro de clientes feito em Python. A tela foi criada com Tkinter e os dados são guardados em um banco SQLite.

## O que o programa faz

- Cadastra clientes com nome, telefone, e-mail e endereço.
- Consulta os clientes cadastrados.
- Permite editar e excluir um cadastro.
- Confere se os campos foram preenchidos, se o telefone tem só números e se o e-mail parece válido.
- Guarda os dados no arquivo `techbairro.db`, criado automaticamente na pasta do programa.

## Requisitos

- Python 3 instalado.
- Tkinter disponível na instalação do Python.
- Não é necessário instalar bibliotecas externas com pip. O SQLite já vem com o Python.

## Como executar

1. Extraia ou abra a pasta do projeto.
2. Abra essa pasta no VS Code.
3. Abra o terminal do VS Code nessa pasta.
4. Execute:

```bash
python techbairro.py
```

## Como executar os testes de validação

No terminal, execute:

```bash
python testar_validacao.py
```

Os testes conferem as regras sem abrir a janela e sem modificar o banco de dados da aplicação.

## Arquivos principais

- `techbairro.py`: janela e ações do usuário.
- `cliente.py`: classe que representa um cliente.
- `banco.py`: operações com o SQLite.
- `validacao.py`: regras de validação.
- `testar_validacao.py`: testes automáticos das regras.
- `docs/manual_de_uso.md`: instruções para usar o programa.
- `docs/registro_de_testes.md`: casos testados e resultados.
- `CHANGELOG.md`: histórico das versões.

## Banco de dados e privacidade

O banco `techbairro.db` é criado quando o programa é executado. Use dados fictícios durante aulas e demonstrações. O `.gitignore` impede que o banco e arquivos temporários sejam incluídos no histórico do Git.
