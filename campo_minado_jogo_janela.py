from functools import partial
from tkinter import *
from ast import literal_eval
from campo_minado_negocio import *

class CampoMinadoJogoJanela:

    __x0 = 25
    __x1 = 69
    __x2 = 113
    __x3 = 157
    __x4 = 201
    __x5 = 245
    __x6 = 289
    __x7 = 333

    __y0 = 25
    __y1 = 65
    __y2 = 105
    __y3 = 145
    __y4 = 185
    __y5 = 225 

    def __init__(self, master):
        self.label = StringVar()
        self.negocio = CampoMinadoNegocio()
        master.title("Campo Minado")
        master.geometry("400x290+500+350")
        master["background"] = "#343434"

        self.__button_0_0 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1, textvariable=self.label)
        self.__button_0_0["command"] = partial(self.__button_onclick, self.__button_0_0)
        self.__button_0_0.place(x=self.__x0, y=self.__y0)
        self.__button_0_1 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_0_1["command"] = partial(self.__button_onclick, self.__button_0_1)
        self.__button_0_1.place(x=self.__x1, y=self.__y0)
        self.__button_0_2 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_0_2["command"] = partial(self.__button_onclick, self.__button_0_2)
        self.__button_0_2.place(x=self.__x2, y=self.__y0)
        self.__button_0_3 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_0_3["command"] = partial(self.__button_onclick, self.__button_0_3)
        self.__button_0_3.place(x=self.__x3, y=self.__y0)
        self.__button_0_4 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_0_4["command"] = partial(self.__button_onclick, self.__button_0_4)
        self.__button_0_4.place(x=self.__x4, y=self.__y0)
        self.__button_0_5 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_0_5["command"] = partial(self.__button_onclick, self.__button_0_5)
        self.__button_0_5.place(x=self.__x5, y=self.__y0)
        self.__button_0_6 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_0_6["command"] = partial(self.__button_onclick, self.__button_0_6)
        self.__button_0_6.place(x=self.__x6, y=self.__y0)
        self.__button_0_7 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_0_7["command"] = partial(self.__button_onclick, self.__button_0_7)
        self.__button_0_7.place(x=self.__x7, y=self.__y0)

        self.__button_1_0 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_1_0["command"] = partial(self.__button_onclick, self.__button_1_0)
        self.__button_1_0.place(x=self.__x0, y=self.__y1)
        self.__button_1_1 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_1_1["command"] = partial(self.__button_onclick, self.__button_1_1)
        self.__button_1_1.place(x=self.__x1, y=self.__y1)
        self.__button_1_2 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_1_2["command"] = partial(self.__button_onclick, self.__button_1_2)
        self.__button_1_2.place(x=self.__x2, y=self.__y1)
        self.__button_1_3 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_1_3["command"] = partial(self.__button_onclick, self.__button_1_3)
        self.__button_1_3.place(x=self.__x3, y=self.__y1)
        self.__button_1_4 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_1_4["command"] = partial(self.__button_onclick, self.__button_1_4)
        self.__button_1_4.place(x=self.__x4, y=self.__y1)
        self.__button_1_5 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_1_5["command"] = partial(self.__button_onclick, self.__button_1_5)
        self.__button_1_5.place(x=self.__x5, y=self.__y1)
        self.__button_1_6 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_1_6["command"] = partial(self.__button_onclick, self.__button_1_6)
        self.__button_1_6.place(x=self.__x6, y=self.__y1)
        self.__button_1_7 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_1_7["command"] = partial(self.__button_onclick, self.__button_1_7)
        self.__button_1_7.place(x=self.__x7, y=self.__y1)

        self.__button_2_0 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_2_0["command"] = partial(self.__button_onclick, self.__button_2_0)
        self.__button_2_0.place(x=self.__x0, y=self.__y2)
        self.__button_2_1 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_2_1["command"] = partial(self.__button_onclick, self.__button_2_1)
        self.__button_2_1.place(x=self.__x1, y=self.__y2)
        self.__button_2_2 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_2_2["command"] = partial(self.__button_onclick, self.__button_2_2)
        self.__button_2_2.place(x=self.__x2, y=self.__y2)
        self.__button_2_3 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_2_3["command"] = partial(self.__button_onclick, self.__button_2_3)
        self.__button_2_3.place(x=self.__x3, y=self.__y2)
        self.__button_2_4 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_2_4["command"] = partial(self.__button_onclick, self.__button_2_4)
        self.__button_2_4.place(x=self.__x4, y=self.__y2)
        self.__button_2_5 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_2_5["command"] = partial(self.__button_onclick, self.__button_2_5)
        self.__button_2_5.place(x=self.__x5, y=self.__y2)
        self.__button_2_6 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_2_6["command"] = partial(self.__button_onclick, self.__button_2_6)
        self.__button_2_6.place(x=self.__x6, y=self.__y2)
        self.__button_2_7 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_2_7["command"] = partial(self.__button_onclick, self.__button_2_7)
        self.__button_2_7.place(x=self.__x7, y=self.__y2)

        self.__button_3_0 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_3_0["command"] = partial(self.__button_onclick, self.__button_3_0)
        self.__button_3_0.place(x=self.__x0, y=self.__y3)
        self.__button_3_1 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_3_1["command"] = partial(self.__button_onclick, self.__button_3_1)
        self.__button_3_1.place(x=self.__x1, y=self.__y3)
        self.__button_3_2 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_3_2["command"] = partial(self.__button_onclick, self.__button_3_2)
        self.__button_3_2.place(x=self.__x2, y=self.__y3)
        self.__button_3_3 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_3_3["command"] = partial(self.__button_onclick, self.__button_3_3)
        self.__button_3_3.place(x=self.__x3, y=self.__y3)
        self.__button_3_4 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_3_4["command"] = partial(self.__button_onclick, self.__button_3_4)
        self.__button_3_4.place(x=self.__x4, y=self.__y3)
        self.__button_3_5 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_3_5["command"] = partial(self.__button_onclick, self.__button_3_5)
        self.__button_3_5.place(x=self.__x5, y=self.__y3)
        self.__button_3_6 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_3_6["command"] = partial(self.__button_onclick, self.__button_3_6)
        self.__button_3_6.place(x=self.__x6, y=self.__y3)
        self.__button_3_7 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_3_7["command"] = partial(self.__button_onclick, self.__button_3_7)
        self.__button_3_7.place(x=self.__x7, y=self.__y3)

        self.__button_4_0 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_4_0["command"] = partial(self.__button_onclick, self.__button_4_0)
        self.__button_4_0.place(x=self.__x0, y=self.__y4)
        self.__button_4_1 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_4_1["command"] = partial(self.__button_onclick, self.__button_4_1)
        self.__button_4_1.place(x=self.__x1, y=self.__y4)
        self.__button_4_2 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_4_2["command"] = partial(self.__button_onclick, self.__button_4_2)
        self.__button_4_2.place(x=self.__x2, y=self.__y4)
        self.__button_4_3 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_4_3["command"] = partial(self.__button_onclick, self.__button_4_3)
        self.__button_4_3.place(x=self.__x3, y=self.__y4)
        self.__button_4_4 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_4_4["command"] = partial(self.__button_onclick, self.__button_4_4)
        self.__button_4_4.place(x=self.__x4, y=self.__y4)
        self.__button_4_5 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_4_5["command"] = partial(self.__button_onclick, self.__button_4_5)
        self.__button_4_5.place(x=self.__x5, y=self.__y4)
        self.__button_4_6 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_4_6["command"] = partial(self.__button_onclick, self.__button_4_6)
        self.__button_4_6.place(x=self.__x6, y=self.__y4)
        self.__button_4_7 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_4_7["command"] = partial(self.__button_onclick, self.__button_4_7)
        self.__button_4_7.place(x=self.__x7, y=self.__y4)

        self.__button_5_0 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_5_0["command"] = partial(self.__button_onclick, self.__button_5_0)
        self.__button_5_0.place(x=self.__x0, y=self.__y5)
        self.__button_5_1 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_5_1["command"] = partial(self.__button_onclick, self.__button_5_1)
        self.__button_5_1.place(x=self.__x1, y=self.__y5)
        self.__button_5_2 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_5_2["command"] = partial(self.__button_onclick, self.__button_5_2)
        self.__button_5_2.place(x=self.__x2, y=self.__y5)
        self.__button_5_3 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_5_3["command"] = partial(self.__button_onclick, self.__button_5_3)
        self.__button_5_3.place(x=self.__x3, y=self.__y5)
        self.__button_5_4 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_5_4["command"] = partial(self.__button_onclick, self.__button_5_4)
        self.__button_5_4.place(x=self.__x4, y=self.__y5)
        self.__button_5_5 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_5_5["command"] = partial(self.__button_onclick, self.__button_5_5)
        self.__button_5_5.place(x=self.__x5, y=self.__y5)
        self.__button_5_6 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_5_6["command"] = partial(self.__button_onclick, self.__button_5_6)
        self.__button_5_6.place(x=self.__x6, y=self.__y5)
        self.__button_5_7 = Button(master, width=5, height=2, text="", background="#EFEFEF", borderwidth=1)
        self.__button_5_7["command"] = partial(self.__button_onclick, self.__button_5_7)
        self.__button_5_7.place(x=self.__x7, y=self.__y5)
    
    def __button_onclick(self, button):
        button["state"] = DISABLED
        button["background"] = "#999999"
        button["borderwidth"] = 2
        button["relief"] = FLAT
        #print(self.__tem_bomba(button))
        self.label.set("0")

    
    def __tem_bomba(self, button):
        #text_var = button["textvariable"]
        #text_str = str(text_var)
        #dicionario = literal_eval(text_str)
        tupla = (0,0)
        valor = self.negocio.tem_bomba(tupla)
        return valor    

if __name__ == "__main__":
    janela = Tk()
    CampoMinadoJogoJanela(janela)
    janela.mainloop()