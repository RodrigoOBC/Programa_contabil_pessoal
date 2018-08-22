#conding: utf-8
from kivy.uix.listview import ListView
from  kivy.app import App
from kivy.uix.label import  Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from Intera_dados import insert, select
import Lista_pesquisa
from kivy.uix.selectableview import SelectableView


LABEL_X = 10
TEXT_X = 130
TAMANHO_ALTURA = 50
janela2 = App()
janela = App()

def salvar():
    Valor = float(Valor_Text.text)
    aviso = insert(Valor,Tipo_text.text,Data_text.text)
    print(aviso)

def get_data():
    return Data_text.text

def lista_dados2():
    tela = FloatLayout()
    data = get_data()
    print(data)
    valores = select(data)
    lista_composta = [[1, 2, 3], [1, 2, 3]]
    list_view = ListView(item_strings=[str(linha).strip('[]') for linha in valores])
    tela.add_widget(list_view)

    Botao_voltar = Button(text='Voltar', font_size=30)
    Botao_voltar.size_hint = None, None
    Botao_voltar.background_color = [0, 0.5, 0.9, 1]
    Botao_voltar.height, Botao_voltar.width, Botao_voltar.x, Botao_voltar.y = 50, 100, 650, 350
    Botao_voltar.on_press = voltar
    tela.add_widget(Botao_voltar)
    return tela


def nova_tela():
    Window.clearcolor = [0, 0, 0, 0]
    Window.size = 800, 600
    janela2.title, janela2.build = 'Tabela', lista_dados2
    janela.stop()
    janela2.run()


def build():

    tela = FloatLayout()

    global Data_text
    Data_text = TextInput(font_size=30)
    Data_text.size_hint = None, None
    Data_text.height, Data_text.width, Data_text.x, Data_text.y = TAMANHO_ALTURA, 500, TEXT_X, 500
    tela.add_widget(Data_text)

    Data_lb = Label(text='Data', font_size=30)
    Data_lb.size_hint = None, None
    Data_lb.height,  Data_lb.width, Data_lb.x, Data_lb.y = TAMANHO_ALTURA, 100, LABEL_X, 500
    tela.add_widget(Data_lb)

    global Tipo_text
    Tipo_text = TextInput(font_size=30)
    Tipo_text.size_hint = None, None
    Tipo_text.height, Tipo_text.width, Tipo_text.x, Tipo_text.y = TAMANHO_ALTURA, 500, TEXT_X, 400
    tela.add_widget(Tipo_text)

    Tipo_lb = Label(text='Tipo', font_size=30)
    Tipo_lb.size_hint = None, None
    Tipo_lb.height, Tipo_lb.width, Tipo_lb.x, Tipo_lb.y = 50, 100, LABEL_X, 400
    tela.add_widget(Tipo_lb)

    global Valor_Text
    Valor_Text = TextInput(font_size=30)
    Valor_Text.size_hint = None, None
    Valor_Text.height, Valor_Text.width, Valor_Text.x, Valor_Text.y = 50, 500, TEXT_X, 300
    tela.add_widget(Valor_Text)

    Valor_lb = Label(text='Valor', font_size=30)
    Valor_lb.size_hint = None, None
    Valor_lb.width, Valor_lb.height, Valor_lb.x, Valor_lb.y = 50, 100, 30, 280
    tela.add_widget(Valor_lb)

    Botao_salva = Button(text='Salvar', font_size=30)
    Botao_salva.size_hint = None,None
    Botao_salva.background_color = [0, 0.5, 0.9, 1]
    Botao_salva.height, Botao_salva.width, Botao_salva.x, Botao_salva.y = 50, 100, 650, 450
    Botao_salva.on_press = salvar
    tela.add_widget(Botao_salva)

    Botao_Fechar = Button(text='Fechar', font_size=30)
    Botao_Fechar.size_hint = None, None
    Botao_Fechar.background_color = [0, 0.5, 0.9, 1]
    Botao_Fechar.height, Botao_Fechar.width, Botao_Fechar.x, Botao_Fechar.y = 50, 100, 650, 350
    Botao_Fechar.on_press = janela.stop
    tela.add_widget(Botao_Fechar)

    Botao_buscar = Button(text='buscar', font_size=30)
    Botao_buscar.size_hint = None, None
    Botao_buscar.background_color = [0, 0.5, 0.9, 1]
    Botao_buscar.height, Botao_buscar.width, Botao_buscar.x, Botao_buscar.y = 50, 100, 650, 250
    Botao_buscar.on_press = nova_tela
    tela.add_widget(Botao_buscar)


    return tela

def voltar():
    janela = App()
    Window.clearcolor = [0, 0, 0, 0]
    Window.size = 800, 600
    janela.title, janela.build = 'Contabilidade Cabral', build
    janela2.stop()
    janela.run()


if __name__ == '__main__':
    janela = App()
    Window.clearcolor = [0, 0, 0, 0]
    Window.size = 800,600
    janela.title,janela.build = 'Contabilidade Cabral',build
    janela.run()

