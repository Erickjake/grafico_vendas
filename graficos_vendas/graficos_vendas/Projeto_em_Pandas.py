import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Ler os dados
df = pd.read_excel("C:/Users/erick/OneDrive/Área de Trabalho/package-template-master/package_name/graficos_vendas/AdventureWorks.xlsx")


# Colunas para obter novos resultados
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])
df["Lucro"] = df["Valor Venda"] - df["Custo"]
df["Tempo Envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

# Variaveis De Resultados para Graficos
receita_total = df["Valor Venda"].sum()
plt.show()
custo_total = round(df["Custo"].sum(), 2)
lucro_total = round(df["Lucro"].sum(), 2)

# Tempo médio de envio por marca
tempo_media = df.groupby("Marca")["Tempo Envio"].mean()

# Configuração do estilo do searborn
sns.set(style="whitegrid")
plt.figure(figsize=(10,6)) # Tamanho da Figura

# Graficos para Visualização
plt.bar(df["Tempo Envio"].value_counts().index, df["Tempo Envio"].value_counts().values, color="purple")
plt.title("Tempo de Envio")
plt.xlabel("Dias")
plt.ylabel("Quantidade")
plt.show()

# Grafico de pizza para a distribuição de receita por marca
plt.figure(figsize=(8, 8))
df.groupby("Marca")["Valor Venda"].sum().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("bright"))
plt.title("Ditribuição da Receita por Marca")
plt.ylabel("")
plt.show()

# Resumo dos resultados

print(f"Receita Total: {receita_total}")
print(f"Custo Total: {custo_total}")
print(f"Lucro Total: {lucro_total}")
print("\nTempo Medio de Envio por Marca: ")
print(tempo_media)