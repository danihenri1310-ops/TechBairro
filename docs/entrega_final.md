# Entrega final da TechBairro

Aluno(a): Daniel Henrique · Versão entregue: 3.3.2

**Por que esta versão:** desde a 3.3.1 foram acrescentados o README, os requisitos, o manual de uso e o registro de testes, sem adicionar uma nova função ao programa. Por isso, o último número passa de 1 para 2.

| # | Item | Evidência |
|---|---|---|
| 1 | A aplicação funciona: os seis casos foram executados | `docs/registro_de_testes.md` |
| 2 | Versão da janela, CHANGELOG e README conferidas | `techbairro.py`, `CHANGELOG.md` e `README.md` mostram 3.3.2 |
| 3 | Pacote testado em pasta limpa | Conferido: extraí o pacote numa pasta temporária limpa; `python testar_validacao.py` passou e os seis casos de interface passaram em tela virtual |
| 4 | Tag e release publicadas, com ZIP anexado | Tag `v3.3.2` criada localmente; falta enviar com `git push` e `git push origin v3.3.2`, depois publicar a release no GitHub com `dist/TechBairro-3.3.2.zip` anexado |
| 5 | Banco, `__pycache__` e `dist` não são rastreados pelo Git | Conferido: `git ls-files` não lista `techbairro.db`, `__pycache__`, arquivos `.pyc` ou `dist/` |
| 6 | Histórico com mensagens claras | https://github.com/danihenri1310-ops/TechBairro/commits/main (o commit local 3.3.2 precisa ser enviado com `git push`) |
| 7 | README, manual e requirements no repositório | `README.md`, `docs/manual_de_uso.md`, `requirements.txt` |
| 8 | Issue “Teste do README” está fechada | Não encontrei uma issue existente com esse título no repositório consultado; conferir/criar a issue e fechar após verificar o README |

## Roteiro da apresentação (até 3 minutos)

| Bloco | Tempo | O que vou mostrar ou dizer |
|---|---:|---|
| Problema e solução | 30 s | A TechBairro organiza o cadastro de clientes; versão 3.3.2. |
| Demonstração ao vivo | 1 min 30 s | Cadastrar um cliente fictício, consultar, editar o telefone, tentar um telefone com espaços e excluir respondendo Não e depois Sim. |
| Como foi construída | 30 s | Python e Tkinter para a tela, SQLite para os dados, arquivos separados para organizar as responsabilidades, testes e Git para o histórico. |
| Aprendizado | 30 s | Aprendi a separar o código em módulos e a registrar mudanças com commits. Uma próxima melhoria seria deixar as mensagens de validação ainda mais fáceis de entender. |

## Plano B

Se a janela não abrir durante a apresentação, mostrar o `README.md`, o `docs/registro_de_testes.md` e a página da release quando ela estiver publicada. Deixei capturas de referência em `docs/img/cadastro.png` e `docs/img/consulta.png`, com dados fictícios. Elas foram feitas em tela virtual; se possível, refaça as capturas no computador da apresentação.

## Fichas de avaliação dos colegas

Preencher durante as apresentações de dois colegas. Não preencher antes de observar as apresentações.

| Pergunta | Colega 1 | Colega 2 |
|---|---|---|
| O problema e a solução ficaram claros? (sim, em parte, não) |  |  |
| A demonstração mostrou o CRUD e uma validação? |  |  |
| Ficou dentro dos 3 minutos? |  |  |
| O que ficou melhor na apresentação? |  |  |
| Uma sugestão específica de melhoria |  |  |

## Autoavaliação

Preencher depois da apresentação, em até cinco linhas:

- O que funcionou bem:
- O que eu mudaria:
- Qual comentário dos colegas foi mais útil:
