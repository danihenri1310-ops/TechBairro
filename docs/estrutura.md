# Estrutura da TechBairro

O projeto foi dividido por responsabilidade para facilitar a leitura e a manutenção.

- `techbairro.py`: interface Tkinter e interação com o usuário.
- `cliente.py`: representa os dados de um cliente.
- `banco.py`: cria a tabela e faz cadastro, consulta, edição e exclusão no SQLite.
- `validacao.py`: confere as regras dos dados antes de salvar.
- `testar_validacao.py`: executa os testes das regras sem abrir a janela.
- `scripts/gerar_pacote.py`: monta o ZIP para distribuição.
- `docs/`: manual, registro de testes e documentação do projeto.
