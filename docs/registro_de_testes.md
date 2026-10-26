# Registro de testes da TechBairro

Versão testada: **3.3.2** · Data: **26/10/2026** · Responsável: **Daniel Henrique**  
Ambiente usado nesta conferência: Linux de teste com tela virtual (Xvfb), Python **3.13.5** e Tkinter **8.6**. Como o computador da apresentação pode ser diferente, repita os casos nesse computador antes da aula.

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar `Ana Souza`, `61999990001`, `ana@email.com`, `Rua 1 Casa 2`. | `Cliente 'Ana Souza' salvo com sucesso!` | `Cliente 'Ana Souza' salvo com sucesso!` | PASSOU |
| CT02 | RF01 | Deixar Nome e Endereço vazios; preencher Telefone e E-mail. | `Preencha o(s) campo(s): Nome, Endereço` | `Preencha o(s) campo(s): Nome, Endereço` | PASSOU |
| CT03 | RF02 | Informar telefone `61 9999 0000`, com espaços. | `Telefone inválido: use somente números.` | `Telefone inválido: use somente números.` | PASSOU |
| CT04 | RF03 | Informar e-mail `ana@email`, sem ponto no domínio. | `E-mail inválido: use o formato nome@dominio.com` | `E-mail inválido: use o formato nome@dominio.com` | PASSOU |
| CT05 | RF05 | Consultar Ana, editar o telefone para `61988880002` e salvar. | `Cliente 'Ana Souza' atualizado com sucesso!` e telefone atualizado no banco. | `Cliente 'Ana Souza' atualizado com sucesso!`; o telefone consultado no banco foi `61988880002`. | PASSOU |
| CT06 | RF06 | Consultar Ana; na exclusão, responder Não e depois repetir e responder Sim. | Ao responder Não, o registro continua. Ao responder Sim, o cadastro é removido e aparece a mensagem de sucesso. | Com Não, o total continuou em 1. Com Sim, apareceu `Cliente 'Ana Souza' excluído com sucesso!` e o total ficou em 0. | PASSOU |

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

Nenhum defeito nos seis casos executados nessa conferência. Os testes da interface foram automatizados numa tela virtual e usaram um banco temporário com dados fictícios; repita a conferência no computador da apresentação.
