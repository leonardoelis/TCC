# Gustavo Oliveira Melo - 20969508
# Jair Angeluci Neto - 20935137
# Leonardo Elis da Silva - 20960821
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Leitura do arquivo CSV
dados = pd.read_csv("Perfil Usuario.csv")
print(dados)

# Exclusão da primeira coluna que contém apenas a data/hora que a pessoa preencheu o questionário
dados = dados.iloc[:,1:20]
print(dados)

# Renomeação das colunas
dados.rename(columns={'Qual sua idade?': 'Idade', 'Qual o seu grau de escolaridade?': 'Escolaridade',
                      'Qual seu estado civil?': 'Estado Civil',
                      'O quanto te incomoda andar ao lado de pessoas fumando?': 'Fumar',
                      'Você gosta de conversar com pessoas que conhece há pouco tempo?': 'Conversar',
                      'Você gosta de andar acompanhado(a) de pessoas com animais de estimação?': 'Pets',
                      'Para você, o quão importante é o custo da viagem (considerando os gastos com meios de transporte)?': 'Custo',
                      'Para você, o quão importante é o tempo gasto na viagem (considerando caminhada e meios de transporte)?': 'Tempo',
                      'Para você, o quão importante é o conforto da viagem?': 'Conforto',
                      'Para você, o quão importante é a segurança da viagem?': 'Segurança',
                      'Para você, o quão importante é a qualidade visual da viagem?': 'Qualidade Visual',
                      'Com que frequência você utiliza os seguintes meios de transporte? [Trem]': 'Trem',
                      'Com que frequência você utiliza os seguintes meios de transporte? [Metrô]': 'Metrô',
                      'Com que frequência você utiliza os seguintes meios de transporte? [Ônibus]': 'Ônibus',
                      'Com que frequência você utiliza os seguintes meios de transporte? [Caminhada]': 'Caminhada',
                      'Com que frequência você utiliza os seguintes meios de transporte? [Bicicleta]': 'Bicicleta',
                      'Com que frequência você sai nos períodos indicados abaixo? [Manhã]': 'Manhã',
                      'Com que frequência você sai nos períodos indicados abaixo? [Tarde]': 'Tarde',
                      'Com que frequência você sai nos períodos indicados abaixo? [Noite]': 'Noite'}, inplace=True)

# Transformação de atributos qualitativos em quantitativos
dados['Idade'] = dados['Idade'].replace(['Até 17 anos'], 1)
dados['Idade'] = dados['Idade'].replace(['De 18 a 24 anos'], 2)
dados['Idade'] = dados['Idade'].replace(['De 25 a 35 anos'], 3)
dados['Idade'] = dados['Idade'].replace(['De 36 a 50 anos'], 4)
dados['Idade'] = dados['Idade'].replace(['A partir de 51 anos'], 5)

dados['Escolaridade'] = dados['Escolaridade'].replace(['Ensino Fundamental ou menos'], 1)
dados['Escolaridade'] = dados['Escolaridade'].replace(['Ensino Médio incompleto'], 2)
dados['Escolaridade'] = dados['Escolaridade'].replace(['Ensino Médio completo'], 3)
dados['Escolaridade'] = dados['Escolaridade'].replace(['Ensino Superior incompleto'], 4)
dados['Escolaridade'] = dados['Escolaridade'].replace(['Ensino Superior completo'], 5)
dados['Escolaridade'] = dados['Escolaridade'].replace(['Pós-graduação'], 6)

dados['Estado Civil'] = dados['Estado Civil'].replace(['Solteiro(a)'], 1)
dados['Estado Civil'] = dados['Estado Civil'].replace(['Casado(a)'], 2)
dados['Estado Civil'] = dados['Estado Civil'].replace(['Divorciado(a)'], 3)
dados['Estado Civil'] = dados['Estado Civil'].replace(['Viúvo(a)'], 4)

dados['Trem'] = dados['Trem'].replace(['Raramente'], 1)
dados['Trem'] = dados['Trem'].replace(['1x por mês'], 2)
dados['Trem'] = dados['Trem'].replace(['1x por semana'], 3)
dados['Trem'] = dados['Trem'].replace(['2-3x por semana'], 4)
dados['Trem'] = dados['Trem'].replace(['4x por semana ou mais'], 5)

dados['Metrô'] = dados['Metrô'].replace(['Raramente'], 1)
dados['Metrô'] = dados['Metrô'].replace(['1x por mês'], 2)
dados['Metrô'] = dados['Metrô'].replace(['1x por semana'], 3)
dados['Metrô'] = dados['Metrô'].replace(['2-3x por semana'], 4)
dados['Metrô'] = dados['Metrô'].replace(['4x por semana ou mais'], 5)

dados['Ônibus'] = dados['Ônibus'].replace(['Raramente'], 1)
dados['Ônibus'] = dados['Ônibus'].replace(['1x por mês'], 2)
dados['Ônibus'] = dados['Ônibus'].replace(['1x por semana'], 3)
dados['Ônibus'] = dados['Ônibus'].replace(['2-3x por semana'], 4)
dados['Ônibus'] = dados['Ônibus'].replace(['4x por semana ou mais'], 5)

dados['Caminhada'] = dados['Caminhada'].replace(['Raramente'], 1)
dados['Caminhada'] = dados['Caminhada'].replace(['1x por mês'], 2)
dados['Caminhada'] = dados['Caminhada'].replace(['1x por semana'], 3)
dados['Caminhada'] = dados['Caminhada'].replace(['2-3x por semana'], 4)
dados['Caminhada'] = dados['Caminhada'].replace(['4x por semana ou mais'], 5)

dados['Bicicleta'] = dados['Bicicleta'].replace(['Raramente'], 1)
dados['Bicicleta'] = dados['Bicicleta'].replace(['1x por mês'], 2)
dados['Bicicleta'] = dados['Bicicleta'].replace(['1x por semana'], 3)
dados['Bicicleta'] = dados['Bicicleta'].replace(['2-3x por semana'], 4)
dados['Bicicleta'] = dados['Bicicleta'].replace(['4x por semana ou mais'], 5)

dados['Manhã'] = dados['Manhã'].replace(['Raramente'], 1)
dados['Manhã'] = dados['Manhã'].replace(['1x por mês'], 2)
dados['Manhã'] = dados['Manhã'].replace(['1x por semana'], 3)
dados['Manhã'] = dados['Manhã'].replace(['2-3x por semana'], 4)
dados['Manhã'] = dados['Manhã'].replace(['4x por semana ou mais'], 5)

dados['Tarde'] = dados['Tarde'].replace(['Raramente'], 1)
dados['Tarde'] = dados['Tarde'].replace(['1x por mês'], 2)
dados['Tarde'] = dados['Tarde'].replace(['1x por semana'], 3)
dados['Tarde'] = dados['Tarde'].replace(['2-3x por semana'], 4)
dados['Tarde'] = dados['Tarde'].replace(['4x por semana ou mais'], 5)

dados['Noite'] = dados['Noite'].replace(['Raramente'], 1)
dados['Noite'] = dados['Noite'].replace(['1x por mês'], 2)
dados['Noite'] = dados['Noite'].replace(['1x por semana'], 3)
dados['Noite'] = dados['Noite'].replace(['2-3x por semana'], 4)
dados['Noite'] = dados['Noite'].replace(['4x por semana ou mais'], 5)
print(dados.info())
print(dados.describe().transpose())

# Dispersão de todos os dados
pca = PCA(n_components=2)
pca.fit(dados)
x = pca.transform(dados)
plt.scatter(x[:, 0], x[:, 1])
plt.title('Dispersão de todos os dados')
plt.show()

# Seleção dos atributos mais relevantes para o agrupamento
dados = dados.loc[:,['Estado Civil', 'Segurança', 'Conforto', 'Trem', 'Metrô']]

# Análise de Componentes Principais (PCA)
pca = PCA(n_components=2)
pca.fit(dados)
x = pca.transform(dados)

# Variância explicada da PCA
print("Variância explicada:")
print(pca.explained_variance_ratio_)

# Dispersão dos dados considerando apenas os atributos selecionados
plt.scatter(x[:,0], x[:,1])
plt.title('Dispersão dos dados com seleção de atributos')
plt.show()

# Execução do K-means com k = 5, 20, 35, 50 e 65
k = 5
while k <= 65:
    kmeans_model = KMeans(n_clusters=k, random_state=1).fit(x)
    labels = kmeans_model.labels_

    print("K:", k)
    print("Silhouette Score:")
    print(metrics.silhouette_score(x, labels, metric='euclidean'))

    plt.scatter(x[:, 0], x[:, 1], s=10, c=kmeans_model.labels_)
    plt.scatter(kmeans_model.cluster_centers_[:, 0], kmeans_model.cluster_centers_[:, 1], s=20, c='red',
                label='Centroids')
    plt.title('Agrupamento')
    plt.show()
    k += 15

# Código para determinar os melhores atributos
# x = dados['Bicicleta'].values
# print(x)
# print(x.reshape(-1,1))
# k = 2
# while k <= 20:
#     kmeans_model = KMeans(n_clusters=k, random_state=1).fit(x.reshape(-1,1))
#     labels = kmeans_model.labels_
#     print(labels)
#
#     print("K:", k)
#     print("Silhouette Score:")
#     print(metrics.silhouette_score(x.reshape(-1,1), labels, metric='euclidean'))
#     k += 1
