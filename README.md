# cybersecurity-ramsonware-challenge

# Ferramenta de Criptografia de Arquivos (AES-256-CBC)

Este projeto contém duas ferramentas simples para criptografar e descriptografar arquivos usando o algoritmo AES-256 em modo CBC. Foi desenvolvido como parte de um laboratório de Cybersecurity para demonstrar conceitos básicos de criptografia simétrica.

## 📦 Instalação

### Pré-requisitos
- Python 3.6 ou superior
- Gerenciador de pacotes pip

### Instalando dependências
```
pip install pycryptodome
```
## Como Usar
Criptografar um arquivo
Use encrypt.py para criptografar um arquivo:

```
python encrypt.py <caminho-do-arquivo>
```
## Saída esperada
Arquivo criptografado salvo em: documento.txt.enc
CHAVE (guarde com segurança!): 5v3RyS3cRe7K3YbAse64Enc0d3dK3Y=

ATENÇÃO: Sem esta chave, os dados serão PERDIDOS permanentemente!

## Descriptografar um arquivo
Use decrypt.py para descriptografar um arquivo:

```
python decrypt.py <caminho-do-arquivo-criptografado> "<chave-em-base64>"
```

## Saída esperada
Arquivo descriptografado salvo em: documento.txt
Descriptografia concluída com sucesso!

