import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
 
# tema  
sns.set_style("darkgrid") 
 
# pgando os dados do iris direto da web 
url = "https://raw.githubusercontent.com/mwaskom/seaborn
data/master/iris.csv" 
iris = pd.read_csv(url) 
 
# mostrando as 5 primeiras linhas 
print("Visualizando os dados:") 
print(iris.head(5)) 
 
# dispersão 
plt.figure(figsize=(8, 6)) 
sns.scatterplot(data=iris, x='petal_length', y='petal_width', 
hue='species') 
plt.title("Pétalas - Tamanho vs Largura") 
plt.xlabel("Tamanho da pétala") 
plt.ylabel("Largura da pétala") 
plt.show() 
 
# boxplots comparando sépalas 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4)) 
 
sns.boxplot(data=iris, x='species', y='sepal_length', ax=ax1, 
palette='Set2') 
ax1.set_title("Sepal Length") 
 
sns.boxplot(data=iris, x='species', y='sepal_width', ax=ax2, 
palette='Set2') 
ax2.set_title("Sepal Width") 
 
plt.suptitle("Comparação das sépalas por espécie") 
plt.show() 
 
# Mapa de calor com correlação 
corr = iris.drop('species', axis=1).corr() 
plt.figure(figsize=(7, 5)) 
sns.heatmap(corr, annot=True, cmap='Blues') 
plt.title("Matriz de Correlação") 
plt.show()