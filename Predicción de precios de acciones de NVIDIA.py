"""
NVIDIA Corporation ofrece soluciones gráficas, informáticas y de redes en Estados Unidos, Taiwán, China e internacionalmente. El segmento de 
gráficos de la compañía ofrece GPU GeForce para juegos y PC, el servicio de transmisión de juegos GeForce NOW e infraestructura relacionada, y 
soluciones para plataformas de juegos; GPU Quadro/NVIDIA RTX para gráficos de estaciones de trabajo empresariales; Software vGPU para computación 
visual y virtual basada en la nube.

Descripción general
Este análisis se centra en el rendimiento de las acciones de NVIDIA Corporation (NVDA) desde el 1 de enero de 2015 hasta el 1 de julio de 2024. Al 
analizar los datos históricos de las acciones, nuestro objetivo es proporcionar información sobre las tendencias financieras de NVIDIA, la 
volatilidad del mercado y los factores que influyen en el precio de sus acciones durante este período.

Descripciones de columnas
date:La fecha de los datos de stock.

open:El precio de apertura de las acciones de NVIDIA en la fecha indicada.

high:El precio más alto de las acciones de NVIDIA durante el día de negociación.

low:El precio más bajo de las acciones de NVIDIA durante el día de negociación.

close:El precio de cierre de las acciones de NVIDIA en la fecha indicada.

adjclose:El precio de cierre ajustado de las acciones de NVIDIA, teniendo en cuenta cualquier acción corporativa como dividendos o divisiones de 
acciones.

volume:El volumen de negociación de acciones de NVIDIA en la fecha indicada."""


import numpy as np 
import pandas as pd 
from plotly import express
import os


DATA = 'nvidia_stock_2015_to_2024.csv'

df = pd.read_csv(filepath_or_buffer=DATA, parse_dates=['date'])
df['year'] = df['date'].dt.year
print(df.head())

#"Veamos primero el historial de precios; como se trata de una empresa exitosa y tenemos una serie larga, probablemente necesitemos mirar los datos 
#en una escala logarítmica".

express.line(data_frame=df, x='date', y=['open', 'high', 'low', 'close'], log_y=True, template = "plotly_dark").show()
express.line(data_frame=df, x='date', y=['close', 'adjclose'], log_y=True, template = "plotly_dark").show()
express.line(data_frame=df, x='date', y='volume', log_y=True, template = "plotly_dark").show()

#Lowess (o loess)
#Suavizado de diagrama de dispersión ponderado localmente

#"Loess significa suavizado de diagrama de dispersión estimado localmente (lowess significa suavizado de diagrama de dispersión ponderado 
# localmente) y es una de las muchas técnicas de regresión no paramétrica, pero posiblemente la más flexible". https://www.epa.gov/sites/default/files/2016-07/documents/loess-lowess.pdf

express.scatter(data_frame=df, x='date', y='volume', trendline='lowess', log_y=True, color='year', template = "plotly_dark").show()

#Arriba:
#"Nuestros datos de volumen parecen bastante sólidos, pero tenemos algunos días con un volumen anormalmente bajo"

#"Nuestra línea de tendencia de precios es muy suave incluso cuando utilizamos valores de cierre ajustados diariamente"

express.scatter(data_frame=df, x='date', y='adjclose', trendline='lowess', color='year', log_y=True, template = "plotly_dark").show()

#Nuestra línea de tendencia de precios es muy suave incluso cuando utilizamos valores de cierre ajustados diariamente.

#express.scatter(data_frame=df[['date', 'adjclose']].set_index(keys=['date']).resample('ME').mean().reset_index(), x='date', y='adjclose', trendline='lowess', log_y=True, tempalte = template).show()

#"Aquí hemos filtrado los valores atípicos de volumen y obtenemos casi una capa anual de precios de cierre por año, ya que el precio de las acciones 
# de Zynex ha subido cada vez más incluso cuando el volumen de operaciones ha disminuido".

#Original era 2000000 Reduje los ceros para trazar algo

express.scatter(data_frame=df[df['volume'] > 20000], x='volume', y='adjclose', color='year', log_x=True, log_y=True, template = "plotly_dark").show()

