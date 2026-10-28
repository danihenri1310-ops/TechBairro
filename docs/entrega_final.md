# Entrega final da TechBairro

Aluno: **Daniel Henrique** · Versão: **3.3.2**

**Por que a versão 3.3.2:** desde a 3.3.1 foram acrescentados documentação, manual, requisitos e registro de testes, sem criar uma nova função para o usuário. Por isso, o último número da versão aumentou de 1 para 2.

## Checklist de entrega

| # | Item pedido | Evidência / situação |
|---|---|---|
| 1 | Os seis casos de teste foram executados | `docs/registro_de_testes.md` registra os resultados de um ambiente de teste Linux com tela virtual. Repetir no Windows antes de gravar. |
| 2 | A versão está igual na janela, CHANGELOG e README | `techbairro.py`, `CHANGELOG.md` e `README.md` mostram `3.3.2`. Confirmar na janela do próprio computador. |
| 3 | Pacote testado numa pasta limpa | `dist/TechBairro-3.3.2.zip`; pacote extraído em pasta temporária, testes automáticos aprovados. Repetir a abertura no Windows. |
| 4 | Tag e Release publicadas com ZIP anexado | Tag `v3.3.2` e Release publicadas no GitHub, com `TechBairro-3.3.2.zip` anexado. [Abrir Release 3.3.2](https://github.com/danihenri1310-ops/TechBairro/releases/tag/v3.3.2). |
| 5 | O repositório não rastreia banco, cache nem `dist` | Conferido com `git ls-files`: `techbairro.db`, `__pycache__`, `.pyc` e `dist/` não estão rastreados. |
| 6 | Histórico com mensagens claras | Histórico de commits publicado: [abrir histórico](https://github.com/danihenri1310-ops/TechBairro/commits/main) |
| 7 | README, manual e requirements estão no repositório | Arquivos confirmados no repositório: `README.md`, `docs/manual_de_uso.md` e `requirements.txt`. |
| 8 | A Issue “Teste do README” está fechada | Issue #1: https://github.com/danihenri1310-ops/TechBairro/issues/1 |
| 9 | O vídeo de até 3 minutos está publicado e abre sem login | **Pendente:** gravar, publicar como Não listado no YouTube ou “Qualquer pessoa com o link” no Drive e colar aqui o link. |

## Roteiro do vídeo

Usar `docs/roteiro_video.md`. Duração máxima: 3 minutos. O roteiro tem problema/solução, demonstração do CRUD e de uma validação, explicação da construção e aprendizado.

## Perguntas por escrito

**1. Por que o arquivo `techbairro.db` não está no GitHub?**  
Porque o banco pode guardar dados pessoais dos clientes. Para evitar publicar esses dados, o banco é ignorado pelo `.gitignore` e não entra no histórico do Git.

**2. Qual caso de teste pegou um defeito de verdade? Qual era o defeito?**  
Em uma versão anterior, a validação percorria só os três primeiros campos e deixava o Endereço vazio passar. O código foi corrigido para verificar os quatro campos. O teste de campos vazios é uma forma de conferir essa correção.

**3. Se o voluntário tiver só o link do repositório, como instala e executa a TechBairro?**  
Ele pode baixar o repositório em ZIP ou cloná-lo, instalar uma versão do Python 3 com Tkinter, extrair/abrir a pasta no terminal e executar `python techbairro.py`. O arquivo SQLite `techbairro.db` é criado automaticamente na pasta do programa; não é preciso instalar uma biblioteca externa para o SQLite.

## Autoavaliação — preencher depois de gravar

- O que ficou bom no meu vídeo: **PREENCHER DEPOIS DE ASSISTIR AO VÍDEO**.
- O que eu mudaria: **PREENCHER DEPOIS DE ASSISTIR AO VÍDEO**.
- O que aprendi de mais importante: **PREENCHER COM SUA EXPERIÊNCIA**.

## Links finais

- Repositório: https://github.com/danihenri1310-ops/TechBairro
- Release 3.3.2: - Release 3.3.2: https://github.com/danihenri1310-ops/TechBairro/releases/tag/v3.3.2
- Vídeo: **PREENCHER DEPOIS DE PUBLICAR**.
