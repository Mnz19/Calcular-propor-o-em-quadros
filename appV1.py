def calcularQuadrado(larguraImagem, alturaImagem ,larguraQuadro, alturaQradro ):
    larguraQuadrado = float(larguraQuadro)/float(larguraImagem)
    alturaQuadrado = float(alturaQradro)/float(alturaImagem)
    return print("{:.2f} x {:.2f}".format(larguraQuadrado, alturaQuadrado))

tamanhoQuadro = input("Digite o tamanho do quadro no formato indicado:[Largura X Altura]\n").replace(" ", "").lower()
tamanhoImagem = input("Digite o tamanho da imagem no formato indicado:[Largura X Altura]\n").replace(" ", "").lower()
#larguraImagem, alturaImagem ,larguraQuadro, alturaQradro (Respectivamente)
posicao_x_imagem = tamanhoImagem.find("x")
posicao_x_quadro = tamanhoQuadro.find("x")  

while posicao_x_imagem == -1 or posicao_x_quadro == -1:
    print("Formato inválido. Certifique-se de usar 'Largura X Altura'.")
    if posicao_x_imagem == -1:
        tamanhoImagem = input("Digite o tamanho da imagem no formato indicado:[Largura X Altura]\n").replace(" ", "").lower()
        posicao_x_imagem = tamanhoImagem.find("x")
    else:
        tamanhoQuadro = input("Digite o tamanho do quadro no formato indicado:[Largura X Altura]\n").replace(" ", "").lower()
        posicao_x_quadro = tamanhoQuadro.find("x")  

else:
    li = tamanhoImagem[:posicao_x_imagem:]
    ai = tamanhoImagem[posicao_x_imagem + 1::]
    lq = tamanhoQuadro[:posicao_x_quadro:]
    aq = tamanhoQuadro[posicao_x_quadro + 1::]
    print(calcularQuadrado(li,ai,lq,aq))
