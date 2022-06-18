import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-T2JV7p5;"
    "DatabasePythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

id = 3
cliente = "Vitória Python"
produto = "Carro"
data = "25/08/2021"
preco = 5000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()