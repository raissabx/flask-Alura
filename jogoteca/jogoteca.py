from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/home')
def ola():
    jogo1 = Jogo('The Sims', 'Vida', 'PC')
    jogo2 = Jogo('While True()', 'Programação', 'PC')
    jogo3 = Jogo('Super Mário', 'Aventura', 'Super Nitendo')

    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()