# Roteiro do vídeo da TechBairro

**Duração máxima:** 3 minutos  
**Versão:** 3.3.2  
**Importante:** use apenas dados fictícios. Não deixe e-mail, mensagens pessoais ou outras informações privadas aparecendo na tela.

## Antes de gravar

1. Abra a pasta `TechBairro` no VS Code e execute `python testar_validacao.py`.
2. Execute `python techbairro.py` e confira se a janela mostra `v3.3.2`.
3. Cadastre antes da gravação um ou dois clientes fictícios, por exemplo Ana Souza (`61999990001`, `ana@email.com`, `Rua 1 Casa 2`) e Bruno Lima (`61988887777`, `bruno@email.com`, `Rua 2 Casa 3`). Assim a Consulta já estará preenchida.
4. Feche notificações e janelas pessoais. Deixe o programa aberto e teste se o microfone grava sua voz.
5. Deixe preparado o link do repositório no navegador. Não precisa mostrar o código inteiro: mostre a tela do programa e explique de maneira simples.

> O arquivo `scripts/importar_planilha_antiga.py` não veio no projeto recebido. Por isso, esta orientação usa o cadastro pela própria interface para preparar os clientes de demonstração.

## Roteiro de até 3 minutos

| Tempo | O que mostrar | O que dizer |
|---|---|---|
| 0:00–0:30 | Janela principal da TechBairro mostrando `v3.3.2`. | “Esta é a TechBairro, um sistema de cadastro de clientes feito em Python. Ele permite cadastrar, consultar, editar e excluir clientes e guarda os dados no SQLite.” |
| 0:30–2:00 | Salvar um cliente fictício; abrir Consulta; editar o telefone; tentar salvar um telefone com espaços; voltar e excluir um cliente. Responda Não primeiro e depois Sim. | “Vou mostrar as funções principais. Primeiro cadastro um cliente. Na Consulta consigo editar seus dados. Se eu colocar espaços no telefone, a validação não deixa salvar. Na exclusão, responder Não mantém o cadastro; responder Sim exclui.” |
| 2:00–2:30 | Mostre rapidamente o terminal com `python testar_validacao.py` e, se couber, a página do GitHub. | “A tela usa Tkinter, o SQLite guarda os dados e o código foi separado em arquivos. Os testes verificam as regras de validação e o Git guarda o histórico das mudanças.” |
| 2:30–3:00 | Mostre README/Release no GitHub se a Release já estiver publicada. | “O README explica como executar o programa. A versão 3.3.2 foi preparada como pacote ZIP para baixar e usar. Aprendi a organizar melhor o código e a registrar testes e versões.” |

Fale num ritmo calmo. Se passar de três minutos, corte explicações repetidas; não acelere tanto que fique difícil de entender.

## Gravar no Windows

### Opção simples: Xbox Game Bar

1. Deixe a janela do programa em foco.
2. Pressione `Windows + Alt + R` para começar a gravar.
3. Confira se o microfone está ligado. `Windows + Alt + M` liga ou desliga o microfone.
4. Faça a demonstração e pressione `Windows + Alt + R` de novo para parar.
5. O vídeo costuma ficar em `Vídeos\Capturas` como arquivo MP4. Esta opção é mais adequada se for gravar principalmente uma janela.

### Para mostrar também o GitHub: OBS Studio

1. Instale o OBS Studio pelo site oficial: https://obsproject.com/.
2. Abra o OBS e adicione uma fonte `Captura de tela` (para mostrar o programa e o navegador) ou `Captura de janela` (para gravar apenas uma janela).
3. Confira no Mixer de áudio se o microfone responde quando você fala.
4. Faça uma gravação de teste de 10 segundos e assista para conferir som e imagem.
5. Clique em `Iniciar gravação`, faça o roteiro, e clique em `Parar gravação`.
6. Abra o vídeo salvo, confira se tem no máximo 3 minutos e se nenhum dado pessoal aparece.

## Publicar o vídeo

Escolha uma opção indicada na atividade:

- **YouTube:** envie o vídeo e escolha a visibilidade **Não listado**.
- **Google Drive:** envie o vídeo e, em Compartilhar, configure o acesso para **Qualquer pessoa com o link**.

Abra o link numa janela anônima para conferir que ele abre sem pedir login. Copie o link final para `docs/entrega_final.md` e para a plataforma da turma.

## Plano B

Se o programa não abrir na hora da gravação, tente executar `python techbairro.py` no terminal e verifique a mensagem de erro. Como apoio visual, há capturas em `docs/img/`, mas a entrega pede um vídeo com a sua voz explicando; as imagens sozinhas não substituem o vídeo.
