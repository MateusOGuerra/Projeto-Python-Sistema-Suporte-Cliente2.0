import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- BANCO ----------------
conexao = sqlite3.connect("cadastro.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    status TEXT
)
""")
conexao.commit()

# ---------------- FUNÇÃO DE SAÍDA ----------------
def mostrar(texto):
    saida.delete("1.0", tk.END)
    saida.insert(tk.END, texto)

# ---------------- FUNÇÕES ----------------

def produtos_entrega():
    texto = (
        "📦 PRODUTOS DISPONÍVEIS PARA ENTREGA\n\n"

        "💻 TECNOLOGIA\n"
        "• Notebook Dell Inspiron 15\n"
        "• Notebook Lenovo IdeaPad\n"
        "• Monitor LG 24\"\n"
        "• Monitor Samsung 27\"\n"
        "• Mouse Logitech M170\n"
        "• Teclado Mecânico Redragon\n"
        "• Headset HyperX Cloud\n"
        "• Webcam Full HD Logitech\n"
        "• SSD Kingston 1TB\n"
        "• HD Externo 1TB\n\n"

        "🪑 GAMER / ESCRITÓRIO\n"
        "• Cadeira Gamer RGB\n"
        "• Mesa Gamer com LED\n"
        "• Suporte para monitor ajustável\n"
        "• Mousepad gamer grande\n"
        "• Kit LED para setup\n\n"

        "📱 ACESSÓRIOS\n"
        "• Carregador turbo USB-C\n"
        "• Cabo HDMI 2.0\n"
        "• Adaptador Bluetooth USB\n"
        "• Power Bank 10.000mAh\n"
        "• Suporte para celular\n\n"

        "🏠 UTILIDADES\n"
        "• Estabilizador de energia\n"
        "• Filtro de linha com proteção\n"
        "• Ventilador portátil USB\n"
        "• Luminária LED de mesa\n"
    )

    mostrar(texto)


def endereco():
    mostrar("📍 Rua Ladeira Porto Geral, 123 - São Paulo")


def horario_de_funcionamento():
    mostrar("🕒 Segunda a Sexta: 08h às 20h")


def abrir_atendente():
    mostrar("🤖 Olá! No que posso te ajudar?")


def enviar_chat():
    msg = entrada_chat.get()

    if msg.strip() == "":
        messagebox.showwarning("Atenção", "Digite uma mensagem!")
        return

    mostrar("📞 Deixe seu número aqui e entraremos em contato o mais rápido possível.")
    entrada_chat.delete(0, tk.END)


def cadastrar_cliente():
    nome = entrada_nome.get()
    telefone = entrada_tel.get()
    status = tipo_cliente.get()

    if nome == "" or telefone == "":
        messagebox.showwarning("Erro", "Preencha nome e telefone!")
        return

    cursor.execute(
        "INSERT INTO clientes (nome, telefone, status) VALUES (?, ?, ?)",
        (nome, telefone, status)
    )
    conexao.commit()

    mostrar("⏳ Aguarde alguns instantes, entraremos em contato já.")
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

    entrada_nome.delete(0, tk.END)
    entrada_tel.delete(0, tk.END)

# ---------------- INTERFACE ----------------

janela = tk.Tk()
janela.title("Sistema de Atendimento - Loja de Informática v2.0")
janela.geometry("700x600")

# ---------------- ÁREA COM SCROLL ----------------
frame_saida = tk.Frame(janela)
frame_saida.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(frame_saida)
scrollbar.pack(side="right", fill="y")

saida = tk.Text(
    frame_saida,
    wrap="word",
    yscrollcommand=scrollbar.set,
    height=15
)

saida.pack(side="left", fill="both", expand=True)
scrollbar.config(command=saida.yview)

# ---------------- TÍTULO ----------------
tk.Label(
    janela,
    text="SISTEMA DE ATENDIMENTO AO CLIENTE",
    font=("Arial", 14, "bold")
).pack(pady=5)

# ---------------- BOTÕES ----------------
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

tk.Button(frame_botoes, text="Produtos disponíveis", command=produtos_entrega).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botoes, text="Endereço", command=endereco).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="Horário", command=horario_de_funcionamento).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="Atendente", command=abrir_atendente).grid(row=0, column=3, padx=5)

# ---------------- CHAT ----------------
tk.Label(janela, text="\n💬 Fale com o atendente").pack()

entrada_chat = tk.Entry(janela, width=50)
entrada_chat.pack()

tk.Button(janela, text="Enviar", command=enviar_chat).pack(pady=5)

# ---------------- CADASTRO ----------------
tk.Label(janela, text="\n🧾 Cadastro de Cliente", font=("Arial", 12, "bold")).pack()

tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela, width=50)
entrada_nome.pack()

tk.Label(janela, text="Telefone:").pack()
entrada_tel = tk.Entry(janela, width=50)
entrada_tel.pack()

tipo_cliente = tk.StringVar(value="sem cadastro")

tk.Radiobutton(janela, text="Cliente cadastrado", variable=tipo_cliente, value="cadastrado").pack()
tk.Radiobutton(janela, text="Cliente sem cadastro", variable=tipo_cliente, value="sem cadastro").pack()

tk.Button(janela, text="Realizar Cadastro", command=cadastrar_cliente).pack(pady=10)

janela.mainloop()