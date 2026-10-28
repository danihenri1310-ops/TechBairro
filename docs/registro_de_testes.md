# Registro de testes da TechBairro

Versão testada: **3.3.2** · Data do teste: **28/10/2026** · Responsável: **Daniel Henrique**  
Ambiente desta conferência: **Linux de teste com tela virtual (Xvfb), Python 3.13.5 e Tkinter 8.6**.

> Os seis casos abaixo foram executados na interface em um ambiente de teste isolado, usando dados fictícios e um banco temporário. Antes da entrega, repita os casos no seu Windows para conferir o comportamento no computador que será usado na gravação. Se as mensagens forem diferentes, atualize a coluna “Obtido” com o texto que apareceu de verdade.

| ID | Requisito | Passos e dados | Esperado | Obtido nesta conferência | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar `Ana Souza`, telefone `61999990001`, e-mail `ana@email.com` e endereço `Rua 1 Casa 2`. | `Cliente 'Ana Souza' salvo com sucesso!` | `Cliente 'Ana Souza' salvo com sucesso!` | PASSOU |
| CT02 | RF01 | Deixar Nome e Endereço vazios; preencher Telefone e E-mail. | `Preencha o(s) campo(s): Nome, Endereço` | `Preencha o(s) campo(s): Nome, Endereço` | PASSOU |
| CT03 | RF02 | Informar o telefone `61 9999 0000`, com espaços. | `Telefone inválido: use somente números.` | `Telefone inválido: use somente números.` | PASSOU |
| CT04 | RF03 | Informar o e-mail `ana@email`, sem ponto no domínio. | `E-mail inválido: use o formato nome@dominio.com` | `E-mail inválido: use o formato nome@dominio.com` | PASSOU |
| CT05 | RF05 | Consultar Ana, editar o telefone para `61988880002` e salvar. | `Cliente 'Ana Souza' atualizado com sucesso!` e o telefone atualizado no banco. | `Cliente 'Ana Souza' atualizado com sucesso!`; o telefone ficou `61988880002`. | PASSOU |
| CT06 | RF06 | Consultar Ana, tentar excluir e responder Não; repetir e responder Sim. | Com Não, mantém o cadastro. Com Sim, exclui e confirma na tela. | Com Não, total ficou em 1. Com Sim, apareceu `Cliente 'Ana Souza' excluído com sucesso!` e o total ficou em 0. | PASSOU |

## Testes automáticos

Comando executado: `python testar_validacao.py`

```text
OK teste_cliente_valido
OK teste_endereco_vazio
OK teste_telefone_com_letras
OK teste_email_sem_ponto
OK teste_nome_telefone_vazios
OK teste_email_sem_nome
Todos os testes passaram.
```

Também foi executado `python -m py_compile techbairro.py cliente.py banco.py validacao.py testar_validacao.py scripts/gerar_pacote.py`, sem erros de sintaxe.

## Defeitos encontrados

Nenhum defeito nos seis casos executados nesta conferência. A execução da interface foi feita em tela virtual no ambiente de teste; repita os mesmos casos no Windows antes de gravar o vídeo. Não use dados reais de clientes.
