import csv
from PIL import Image, ImageDraw, ImageFont
import qrcode
import re

def clean_filename(name):
    # Substitui caracteres inválidos por underscores
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def create_qr_code(data, output_path, font):
    # Crie um objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Adicione os dados ao QRCode
    qr.add_data(data)
    qr.make(fit=True)

    # Crie uma imagem a partir do QRCode
    img = qr.make_image(fill_color="black", back_color="white")

    # Use o texto sem "MV|" para a moldura
    text_frame = data[3:]

    # Crie um retângulo preto ao redor do QRCode (moldura)
    draw = ImageDraw.Draw(img)
    draw.rectangle(
        [(2, img.size[1] - 25), (img.size[0] - 2, img.size[1])],
        fill="black",
    )

    # Adicione o texto da moldura à imagem
    font_size = 40  # Ajuste este valor para o tamanho desejado
    font = ImageFont.load_default()
    text_bbox = draw.textbbox((0, 0), text_frame, font)
    text_position = (
        (img.size[0] - text_bbox[0]) // 2,
        img.size[1] - 12 - (text_bbox[1] // 2),
    )
    draw.text(text_position, text_frame, font=font, fill="white")

    # Salve a imagem com um nome de arquivo limpo
    img.save(clean_filename(output_path))

def main(csv_file_path):
    try:
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  # Verifica se a linha não está vazia antes de acessar o índice
                    data = row[0]
                    output_path = f'{data}.jpg'  # Pode ajustar o nome do arquivo de saída conforme necessário
                    create_qr_code(data, output_path, font=None)
    except FileNotFoundError:
        print(f"O arquivo {csv_file_path} não existe.")

# Chame a função main com o caminho do seu arquivo CSV
main("C:\\Users\\jorna\\Downloads\\create_text_qr_codes_template2.csv")
