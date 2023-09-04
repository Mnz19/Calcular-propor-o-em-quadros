import tkinter as tk

def obterTamanho(mensagem):
    while True:
        tamanho = mensagem.replace(" ", "").lower()
        posicao_x = tamanho.find("x")
        if posicao_x != -1:
            return tamanho[:posicao_x], tamanho[posicao_x + 1:]
        else:
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, "Formato inválido. Certifique-se de usar 'Largura X Altura'.")
            return
    
def calcularQuadrado():
    tamanho_quadro = obterTamanho(entrada_quadro.get())
    tamanho_imagem = obterTamanho(entrada_imagem.get())

    largura_quadrado = float(tamanho_quadro[0]) / float(tamanho_imagem[0])
    altura_quadrado = float(tamanho_quadro[1]) / float(tamanho_imagem[1])
    return  (resultado_text.delete(1.0, tk.END),
    resultado_text.insert(tk.END, "Cada quadrado da tela será de {:.2f} x {:.2f}, sendo {} desse quadrados na horizontal e {} na vertical".format(largura_quadrado, altura_quadrado, tamanho_imagem[0], tamanho_imagem[1])))


    
root = tk.Tk()
root.title("Calculadora de Quadrados")
root.geometry("600x400")

root.grid_rowconfigure(8, weight=1)
root.columnconfigure(0, weight=1)    

label_quadro = tk.Label(root, text="Tamanho do Quadro:")
label_quadro.grid(row=1, column=0, pady=(20, 5))  

entrada_quadro = tk.Entry(root)
entrada_quadro.grid(row=2, column=0, pady=5)

label_imagem = tk.Label(root, text="Tamanho da Imagem:")
label_imagem.grid(row=3, column=0, pady=5)

entrada_imagem = tk.Entry(root)
entrada_imagem.grid(row=4, column=0, pady=5)

calcular_button = tk.Button(root, text="Calcular", command=calcularQuadrado)
calcular_button.grid(row=5, column=0, pady=(5, 20))

resultado_text = tk.Text(root, height=5, width=35)
resultado_text.grid(row=6, column=0, pady=5)

root.mainloop()
