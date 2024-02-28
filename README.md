# Gerador-de-qr-code-em-massa-por-meio-de-um-arquivo-CSV
Descrição da Aplicação: Gerador de Códigos QR com Moldura de Texto

** Gerador de Códigos QR com Moldura de Texto**

Esta aplicação em Python é um gerador de códigos QR que recebe dados de um arquivo CSV e cria códigos QR personalizados com moldura de texto. A funcionalidade principal inclui a geração de códigos QR , onde parte dos dados é utilizada para formar uma moldura de texto ao redor do código.

**Principais Características:**

1. **Entrada de Dados por CSV:** A aplicação lê dados de um arquivo CSV, garantindo que os dados estejam estruturados corretamente para a geração de códigos QR.

2. **Personalização da Moldura de Texto:** A moldura de texto é criada a partir dos dados fornecidos, excluindo uma parte inicial (no exemplo, "MV|"). A moldura é exibida ao redor do código QR, adicionando um elemento personalizado à imagem.

3. **Saída de Imagem Personalizada:** Os códigos QR gerados são salvos como imagens JPEG, com nomes de arquivo limpos para garantir compatibilidade com sistemas de arquivos.

**Como Usar:**

- **Preparação do CSV:** Prepare um arquivo CSV contendo os dados desejados para cada código QR.

- **Execução do Script:** Execute o script Python fornecendo o caminho para o arquivo CSV como argumento. O script processará os dados e gerará códigos QR personalizados.

- **Saída Personalizada:** As imagens geradas serão salvas com nomes correspondentes aos dados do CSV, prontas para uso.

**Requisitos:**

- Python
- Bibliotecas: PIL (Pillow), qrcode
