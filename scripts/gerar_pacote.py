# Gera o pacote de entrega da TechBairro.
from pathlib import Path
import zipfile

PASTA_PROJETO = Path(__file__).resolve().parents[1]
PASTA_DIST = PASTA_PROJETO / "dist"
VERSAO = "3.3.2"
ARQUIVO_ZIP = PASTA_DIST / f"TechBairro-{VERSAO}.zip"

# Arquivos necessários para usar e conferir o programa.
ARQUIVOS = [
    "techbairro.py",
    "cliente.py",
    "banco.py",
    "validacao.py",
    "testar_validacao.py",
    "README.md",
    "requirements.txt",
    "CHANGELOG.md",
    "COMO_EXECUTAR.txt",
    "docs/estrutura.md",
    "docs/manual_de_uso.md",
    "docs/registro_de_testes.md",
    "scripts/gerar_pacote.py",
]

PASTA_DIST.mkdir(exist_ok=True)
if ARQUIVO_ZIP.exists():
    ARQUIVO_ZIP.unlink()

with zipfile.ZipFile(ARQUIVO_ZIP, "w", zipfile.ZIP_DEFLATED) as pacote:
    faltando = []
    for nome in ARQUIVOS:
        caminho = PASTA_PROJETO / nome
        if caminho.is_file():
            pacote.write(caminho, arcname=nome)
        else:
            faltando.append(nome)

if faltando:
    raise SystemExit("ERRO: arquivos necessários não encontrados: " + ", ".join(faltando))

with zipfile.ZipFile(ARQUIVO_ZIP, "r") as pacote:
    nomes = pacote.namelist()
    proibidos = [nome for nome in nomes if "__pycache__" in nome or nome.endswith((".db", ".pyc")) or nome.startswith(".git/") or nome.startswith("dist/")]
    if proibidos:
        ARQUIVO_ZIP.unlink(missing_ok=True)
        raise SystemExit("ERRO: arquivos que não deveriam estar no pacote: " + ", ".join(proibidos))

print(f"Pacote criado: {ARQUIVO_ZIP}")
print("Arquivos incluídos:")
for nome in nomes:
    print("-", nome)
print("Conferência: banco, cache Python, .pyc, .git e dist ficaram de fora.")
