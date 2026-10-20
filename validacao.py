# ============================================================
# VALIDAÇÃO (Aula 21)
# ============================================================
# Responsabilidade: as regras de negócio do cadastro (RF01 a RF03).
# Este arquivo não sabe nada de janela nem de banco.

class ValidadorCliente:
    # Confere todas as regras do cliente.
    # Retorna a mensagem do primeiro problema encontrado,
    # ou None se o cliente estiver válido.
    def validar(self, cliente):
        # RF01: campos vazios, na mesma ordem que aparece na tela.
        vazios = []
        if cliente.nome == "":
            vazios.append("Nome")
        if cliente.telefone == "":
            vazios.append("Telefone")
        if cliente.email == "":
            vazios.append("E-mail")
        if cliente.endereco == "":
            vazios.append("Endereço")

        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"

        # RF02: o telefone precisa ter somente números.
        if not cliente.telefone.isdigit():
            return "Telefone inválido: use somente números."

        # RF03: mantém a mensagem que já era mostrada pela versão 3.3.0.
        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido: use o formato nome@dominio.com"

        return None

    # Mantém a mesma regra da função usada na versão 3.3.0.
    def email_parece_valido(self, email):
        if "@" not in email:
            return False

        usuario, _, dominio = email.partition("@")

        if usuario == "" or "." not in dominio:
            return False

        return True
