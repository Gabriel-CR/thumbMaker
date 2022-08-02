from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys

def escreverImagem(img):
    (largura, altura) = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./Kanit/Kanit-ExtraBold.ttf", 30)
    draw.text((largura / 2, altura / 2), "Hello World", fill=(255, 255, 255), align="center", font=font)
    img.save("./img/thumb.png")

if __name__ == "__main__":
    if sys.argv[1] == "--help":
        print("""
        Uso:
        python main.py <operacao> <nome_imagem> <nome_saida>
        """)
    elif sys.argv[1] == "-w":
        imagem = Image.open(sys.argv[2])
        escreverImagem(imagem)
    else:
        print("""Opção inválida
        Uso:
        python main.py <operacao> <nome_imagem> <nome_saida>
        """)