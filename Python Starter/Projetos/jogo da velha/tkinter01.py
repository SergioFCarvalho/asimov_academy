import tkinter as tk

# Instanciar janela
janela = tk.Tk()
janela.title("Primeiro App")  # titulo
janela.geometry("400x300+100+100")  # dimensões
janela.config(bg='#20EE70')  # Cor de fundo
janela.attributes('-alpha', 0.9)  # transparência da janela

# Criar e posicionar Label com uma msg
titleLabel = tk.Label(janela, text='Hello World!')
titleLabel.pack()

# Exibir -
janela.mainloop()
