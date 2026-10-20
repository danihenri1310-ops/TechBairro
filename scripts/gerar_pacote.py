# Gera o pacote de entrega da TechBairro.
from pathlib import Path
import zipfile

PASTA_PROJETO = Path(__file__).resolve().parents[1]
PASTA_DIST = PASTA_PROJETO / "dist"
VERSAO = "3.3.1"
ARQUIVO_ZIP = PASTA_DIST / f"TechBairro-{VERSAO}.zip"

# Arquivos necessários para usar e verificar o projeto.
ARQUIVOS = [
    "techbairro.py",
    "cliente.py",
    "banco.py",
    "validacao.py",
    "testar_validacao.py",
    "CHANGELOG.md",
    "COMO_EXECUTAR.txt",
    "scripts/gerar_pacote.py",
]

PASTA_DIST.mkdir(exist_ok=True)
if ARQUIVO_ZIP.exists():
    ARQUIVO_ZIP.unlink()

with zipfile.ZipFile(ARQUIVO_ZIP, "w", zipfile.ZIP_DEFLATED) as pacote:
    for nome in ARQUIVOS:
        caminho = PASTA_PROJETO / nome
        if caminho.exists():
            pacote.write(caminho, arcname=nome)
        else:
            print(f"AVISO: arquivo não encontrado: {nome}")

print(f"Pacote criado: {ARQUIVO_ZIP}")
print("Conteúdo:")
with zipfile.ZipFile(ARQUIVO_ZIP, "r") as pacote:
    for nome in pacote.namelist():
        print("-", nome)
    proibidos = [nome for nome in pacote.namelist()
                 if "__pycache__" in nome or nome.endswith(".db")]
    if proibidos:
        print("ERRO: arquivos que não deveriam estar no pacote:", proibidos)
    else:
        print("Conferência: __pycache__ e banco de dados ficaram de fora.")
