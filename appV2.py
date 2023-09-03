def calcularQuadrado(larguraImagem, alturaImagem, larguraQuadro, alturaQuadro):
    larguraQuadrado = float(larguraQuadro) / float(larguraImagem)
    alturaQuadrado = float(alturaQuadro) / float(alturaImagem)
    return "{:.2f} x {:.2f}".format(larguraQuadrado, alturaQuadrado)

def obterTamanho(mensagem):
    while True:
        tamanho = input(mensagem).replace(" ", "").lower()
        posicao_x = tamanho.find("x")
        if posicao_x != -1:
            return tamanho[:posicao_x], tamanho[posicao_x + 1:]
        else:
            print("Formato inválido. Certifique-se de usar 'Largura X Altura'.")

tamanhoQuadro = obterTamanho("Digite o tamanho do quadro no formato indicado:[Largura X Altura]\n")
tamanhoImagem = obterTamanho("Digite o tamanho da imagem no formato indicado:[Largura X Altura]\n")

resultado = calcularQuadrado(*tamanhoImagem, *tamanhoQuadro)
print(resultado)