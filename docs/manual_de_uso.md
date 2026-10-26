# Manual de uso da TechBairro

## 1. Abrir o programa

1. Abra a pasta `TechBairro` no VS Code.
2. Abra o terminal nessa pasta.
3. Execute `python techbairro.py`.

A janela Cadastro de Cliente será aberta. O banco `techbairro.db` é criado automaticamente se ainda não existir.

## 2. Cadastrar um cliente

1. Preencha Nome, Telefone, E-mail e Endereço.
2. Clique em **Salvar**.
3. Confira a mensagem que aparece abaixo do formulário.

Use dados fictícios para testes. Exemplo: Ana Souza, `61999990001`, `ana@email.com`, `Rua 1 Casa 2`.

## 3. Regras de validação

- Os quatro campos precisam ser preenchidos.
- O telefone precisa ter somente números, sem espaços ou letras.
- O e-mail precisa ter um usuário e um domínio com ponto, por exemplo `ana@email.com`.

Se algum dado estiver errado, a mensagem vermelha explica o problema.

## 4. Consultar e editar

1. Clique em **Consultar**.
2. Selecione o cliente desejado.
3. Clique em **Editar selecionado** ou dê dois cliques no cliente.
4. Altere os campos necessários e clique em **Salvar edição**.

A mensagem da janela principal informa se a alteração foi salva.

## 5. Excluir

1. Abra **Consultar** e selecione um cliente.
2. Clique em **Excluir selecionado**.
3. Confira o nome e os dados mostrados na confirmação.
4. Clique em **Não** para manter o cadastro ou em **Sim** para excluir.

## 6. Fechar e abrir novamente

Feche a janela normalmente. Ao abrir o programa de novo, os cadastros continuam no arquivo `techbairro.db`.

## 7. Executar os testes

Para testar as regras sem abrir a janela, execute `python testar_validacao.py` no terminal.
