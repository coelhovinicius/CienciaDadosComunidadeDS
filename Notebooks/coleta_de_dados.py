# -*- coding: utf-8 -*-
"""Coleta_de_Dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vgsG6ZMYFZaSsiO16BeV-nNsL_ym9UXu

##Importando Dados
"""

# Importando os Dados

import sqlite3
import pandas as pd
conn = sqlite3.connect( "database.db" )

# Consulta dos Dados no BD
consulta_atividade = """

  SELECT
    fa.loyalty_number,
    fa.year,
    fa.month,
    fa.flights_booked,
    fa.total_flights,
    fa.distance,
    fa.points_accumulated
  FROM
    flight_activity fa

"""
df_atividade = pd.read_sql_query( consulta_atividade, conn )

df_atividade.head(10)

"""#Exercícios Aula 1 - SQL

"""

# 1. Selecione as colunas: loyalty_number, country, city, gender, loyalty_card e salary da tabela "flight_loyalty_history"

consulta_atividade = """

  SELECT
    flh.loyalty_number,
    flh.country,
    flh.city,
    flh.gender,
    flh.loyalty_card,
    flh.salary
  FROM
    flight_loyalty_history flh

"""

df_atividade = pd.read_sql_query( consulta_atividade, conn )

df_atividade.head()

# 2. Selecione as mesmas colunas, porém, recupere somente as linhas cuja coluna gender é igual a Female da tabela flighy_loyalty_history

consulta_atividade = """

  SELECT
    flh.loyalty_number,
    flh.country,
    flh.city,
    flh.gender,
    flh.loyalty_card,
    flh.salary
  FROM
    flight_loyalty_history flh
  WHERE
    flh.gender = 'Female'

  """

df_atividade = pd.read_sql_query( consulta_atividade, conn )

df_atividade.head(12)

# 3. Selecione as colunas: loyalty_number, month, year, distance, flights_booked e total_flights da tabela flight_activity
# e recupere somente as linhas cuja coluna flights_booked é maior que 10 e menor que 12.

consulta_atividade = """

  SELECT
    fa.loyalty_number,
    fa.month,
    fa.year,
    fa.distance,
    fa.flights_booked,
    fa.total_flights
  FROM
    flight_activity fa
  WHERE
    fa.flights_booked > 10
  AND
    fa.flights_booked < 12

"""

df_atividade = pd.read_sql_query( consulta_atividade, conn )

df_atividade.head(12)

"""#Inspeção dos Dados"""

# Importando os Dados com Python
import sqlite3 as sl3
import pandas as pd

# Estabelece a conexão com a base de dados e atribui á variavel "conn"
conn = sl3.connect( "database.db" )

# Juntando as tabelas flight_activity e flight_loyalty_history
consulta_atividade = """
  SELECT
    *
  FROM flight_activity fa LEFT JOIN flight_loyalty_history flh ON (fa.loyalty_number = flh.loyalty_number)

"""

# Executando uma consulta SQL no banco de dados SQLite ao qual conn está conectado,
# e armazenando o resultado em um DataFrame do pandas chamado df_atividade.
# Isso permite que você trabalhe com os dados da consulta SQL usando as funcionalidades do pandas.
df_atividade = pd.read_sql_query( consulta_atividade, conn )

# Verifica se está funcionando
df_atividade.head(10)

# Verificar o número de linhas do Data Frame
df_atividade.shape[0]

# Verificar o número de colunas do Data Frame
df_atividade.shape[1]

# Obtendo informações da base de dados
df_atividade.info()

# Exibe as informações de todas as linhas da coluna "distance"
df_atividade.loc[:, "distance"]

# Comandos aritméticos
soma_distancia = df_atividade.loc[:, "distance"].sum()
maior_distancia = df_atividade.loc[:, "distance"].max()
media_distancia = df_atividade.loc[:, "distance"].mean()
minima_distancia = df_atividade.loc[:, "distance"].min()

print('Soma das Distâncias: {}'.format(soma_distancia))
print(maior_distancia)
print(media_distancia)
print(minima_distancia)

# Verificar valores nulos
df_atividade.isna()

df_atividade.head()

"""#Tratamento dos Dados"""

# Importando os Dados
import sqlite3 as sl3
import pandas as pd

# Estabelecendo a Conexão
conn = sqlite3.connect( "database.db" )

consulta_atividade = """

SELECT
  *
  FROM flight_activity fa Left Join flight_loyalty_history flh ON (fa.loyalty_number = flh.loyalty_number)

"""

df_atividade = pd.read_sql_query( consulta_atividade, conn )
df_atividade.head()

# Numero de dados faltantes
df_atividade.isna().sum()

# selecionando somente as colunas numéricas
colunas = ["year", "month", "flights_booked", "flights_with_companions", "total_flights",
"distance", "points_accumulated", "salary", "clv", "loyalty_card"]

df_colunas_numericas = df_atividade.loc[:, colunas]
df_colunas_numericas

# removendo linhas com alguma coluna vazia
df_dados_completos = df_colunas_numericas.dropna()

# verificando o numero de linhas vazias
df_dados_completos.isna().sum()

df_dados_completos.shape[0]

"""#Machine Learning"""

df_dados_completos.head()

#Importação da biblioteca "tree", que está dentro da biblioteca "sklearn"
from sklearn import tree as tr

X_atributos = df_dados_completos.drop(columns="loyalty_card")
y_rotulos = df_dados_completos.loc[:, "loyalty_card"]

#Definição do algoritmo
modelo = tr.DecisionTreeClassifier(max_depth=5)

#Treinamento do algoritmo - modelo.fit(X_atributos, Y_rotulo)
modelo_treinado = modelo.fit(X_atributos, y_rotulos)

X_atributos.head()

y_rotulos.head()

tr.plot_tree(modelo_treinado, filled=True);

"""#Apresentando os Resultados"""

#Exibe os dados aleatoreamente
X_novo = X_atributos.sample()

#Probabilidades
previsao = modelo_treinado.predict_proba(X_novo)

print("Prob - Aurora: {:.2%} - Nova: {:.2%} - Star {:.2%}".format(previsao[0][0], previsao[0][1], previsao[0][2]))

"""#Painel de Visualização"""

#Instalação do Gradio
!pip install gradio

#Importando a biblioteca Gradio
import gradio as gr
import numpy as np

# Função de previsão
def predict(*args):
  X_novo = np.array([args]).reshape(1, -1)
  previsao = modelo_treinado.predict_proba(X_novo)

  return{"Aurora":previsao[0][0], "Nova":previsao[0][1], "Star":previsao[0][2]}

print("Prob - Aurora: {:.2%} - Nova: {:.2%} - Star {:.2%}".format(previsao[0][0], previsao[0][1], previsao[0][2]))

#Comando para criar blocos
with gr.Blocks() as painel_previsoes:
  #Título do painel
  gr.Markdown(""" # Propensão de Compra """)

  with gr.Row():
    with gr.Column():
      gr.Markdown(""" # Atributos do Cliente """)
      year                    = gr.Slider(label="year", minimum=2017, maximum=2018, step=1, randomize=True)
      month                   = gr.Slider(label="month", minimum=1, maximum=12, step=1, randomize=True)
      flights_booked          = gr.Slider(label="flights_booked", minimum=0, maximum=21, step=1, randomize=True)
      flights_with_companions = gr.Slider(label="flights_with_companion", minimum=0, maximum=11, step=1, randomize=True)
      total_flights           = gr.Slider(label="total_flights", minimum=0, maximum=32, step=1, randomize=True)
      distance                = gr.Slider(label="distance", minimum=0, maximum=6293, step=1, randomize=True)
      points_accumulated      = gr.Slider(label="points_accumulated", minimum=0.00, maximum=676.50, step=0.1, randomize=True)
      salary                  = gr.Slider(label="salary", minimum=58486.00, maximum=407228.00, step=0.1, randomize=True)
      clv                     = gr.Slider(label="clv", minimum=2119.89, maximum=83325.38, step=0.1, randomize=True)

      with gr.Row():

        with gr.Row():
          gr.Markdown(""" # Botão de Previsão """)
          predict_btn = gr.Button(value="Previsao")

    with gr.Column():
      gr.Markdown(""" # Propensão de Compra do Cliente """)
      label = gr.Label()

#Botão Predict
  predict_btn.click(
    fn=predict,
    inputs=[
        year,
        month,
        flights_booked,
        flights_with_companions,
        total_flights,
        distance,
        points_accumulated,
        salary,
        clv
        ],
    outputs=[label])

painel_previsoes.launch(debug=True, share=False)#share=True)

"""#Exercícios Aula 2 - SQL e Python"""

# Importando os Dados

import sqlite3
import pandas as pd
conn = sqlite3.connect( "database.db" )

df_atividade = pd.read_sql_query( consulta_atividade, conn )
df_atividade.info()

'''1. Selecionar os números do cartão de fidelidade, a cidade e o gênero, dos passageiros que tem o
cartão Star de fidelidade, mas nunca realizaram nenhuma viagem de avião ( Dica: “loyalty_card” = “Star” e
“distance” = 0 )'''

consulta_atividade1 = """

  SELECT
    flh.loyalty_number,
    flh.gender,
    flh.city,
    flh.loyalty_card

  FROM flight_activity fa LEFT JOIN flight_loyalty_history flh ON (fa.loyalty_number = flh.loyalty_number)

  WHERE
    flh.loyalty_card = 'Star' AND fa.distance = 0

"""

df_atividade1 = pd.read_sql_query( consulta_atividade1, conn )

df_atividade1.head(12)

'''2. Selecionar os números do cartão de fidelidade, o gênero e a cidade de todos os passageiros do sexo feminino que
moram na cidade de Toronto, fizeram mais de 30 viagens no total e tem o cartão de fidelidade do tipo Aurora.'''

consulta_atividade2 = """

  SELECT
    flh.loyalty_number,
    flh.gender,
    flh.city,
    flh.loyalty_card

  FROM flight_activity fa LEFT JOIN flight_loyalty_history flh ON (fa.loyalty_number = flh.loyalty_number)

  WHERE
    flh.gender = 'Female' AND flh.city = 'Toronto' AND fa.total_flights > 30 AND flh.loyalty_card = 'Aurora'

"""

df_atividade2 = pd.read_sql_query( consulta_atividade2, conn )

df_atividade2.head(12)

'''3. Selecionar os números do cartão de fidelidade, o tipo do cartão, o genero e os pontos acumulados, dos passageiros
com salário acima de 13200, estado civil como casado e nível acadêmico como mestrado e número de voos
agendados igual ao número total de voos.'''

consulta_atividade3 = """

  SELECT
    flh.loyalty_number,
    flh.gender,
    fa.points_accumulated,
    flh.salary,
    flh.marital_status,
    flh.education,
    fa.flights_booked,
    fa.total_flights,
    flh.loyalty_card

  FROM flight_activity fa LEFT JOIN flight_loyalty_history flh ON (fa.loyalty_number = flh.loyalty_number)

  WHERE
    salary > 13200 AND marital_status = 'Married' AND education = 'Master' AND flights_booked = total_flights

"""

df_atividade3 = pd.read_sql_query( consulta_atividade3, conn )

df_atividade3.head(12)

'''4. Selecionar os números do cartão de fidelidade, o tipo do cartão, o genero e os pontos acumulados, dos passageiros
com salário acima de 13200, estado civil como casado e nível acadêmico como mestrado e número de voos
agendados menor ao número total de voos.'''

consulta_atividade4 = """

SELECT
    flh.loyalty_number,
    flh.gender,
    fa.points_accumulated,
    flh.salary,
    flh.marital_status,
    flh.education,
    fa.flights_booked,
    fa.total_flights,
    flh.loyalty_card

  FROM flight_activity fa LEFT JOIN flight_loyalty_history flh ON (fa.loyalty_number = flh.loyalty_number)

  WHERE
    flh.salary > 13200 AND flh.marital_status = 'Married' AND flh.education = 'Master' AND fa.flights_booked < fa.total_flights

"""

df_atividade4 = pd.read_sql_query( consulta_atividade4, conn )

df_atividade4.head(12)

'''5. Qual o valor da soma total da distância percorrida pelos voos registrados na planilha de dados?'''

soma_distancia = df_atividade.loc[:, "distance"].sum()
print(soma_distancia)

'''6. Qual o salário médio dos passageiros?'''

media_salario = df_atividade.loc[:, "salary"].mean()
print("Média salarial: {:.2f}".format(media_salario))

'''7. Qual o valor total de pontos acumulados?'''

total_pontos = df_atividade.loc[:, "points_accumulated"].sum()
print("Total de pontos acumulados: {:.2f}".format(total_pontos))

"""#Fechando a Conexão"""

# Fecha a conexão com o banco de dados
#conn.close()