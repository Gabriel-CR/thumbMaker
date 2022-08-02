from PIL import Image, ImageDraw
import sys

def escreverImagem(img):
    imagem = Image.open(img)
    (largura, altura) = imagem.size
    draw = ImageDraw.Draw(imagem)
    draw.text((180, altura / 2), "Hello World", fill=(255, 255, 255), align='center')
    imagem.save("teste.png")

if __name__ == "__main__":
    if sys.argv[1] == "--help":
        print("""
        Uso:
        python main.py <operacao> <nome_imagem> <nome_saida>
        """)
    elif sys.argv[1] == "-r":
        escreverImagem(sys.argv[2])