import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# File reading
df = pd.read_csv('caida_moneda_datos.csv', sep = ',', decimal=',')
df = df['T3'].astype(float)
df = df.sort_values(ascending=True)
print(df)


# Range
rango = df.max() - df.min()
print('Este es el rango: ', rango)


# Number of clases
clases = 7


# Wide of each class
ancho = rango / clases
print('Este es el ancho: ', ancho)


# Different classes creation
for clases in df:
	clase1 = df.loc[0] + ancho
	print('Esta es la clase 1: ', clase1)
	clase2 = clase1 + ancho
	print('Esta es la clase 2: ', clase2)
	clase3 = clase2 + ancho
	print('Esta es la clase 3: ', clase3)
	clase4 = clase3 + ancho
	print('Esta es la clase 4: ', clase4)
	clase5 = clase4 + ancho
	print('Esta es la clase 5: ', clase5)
	clase6 = clase5 + ancho
	print('Esta es la clase 6: ', clase6)
	clase7 = clase6 + ancho
	print('Esta es la clase 7: ', clase7)
	break

# Standard Deviation
def stand_deviation:
	std_deviation = numpy.std(df)
	print('Este es el valor de la desviacion estandar: ', std_deviation)

stand_deviation()

# Average Value
def mean_caida_moneda():
	mean_caida = df.mean()
	print('Este es el valor medio del tiempo de caida de la moneda considerando los datos del cronometro 3: ', mean_caida)

mean_caida_moneda()	

# Median
def median_caida_moneda():
	median_caida = df.median()
	print('Esta es la mediana del tiempo de caida de la moneda considerando los datos del cronometro 3: ', median_caida)

median_caida_moneda()

# Mode
def mode_caida_moneda():
	mode_caida = df.mode()
	print('Esta es la moda del tiempo de caida de la moneda considerando los datos del cronometro 3: ', mode_caida)

mode_caida_moneda()


# Histogram
def histograma():
	
	fig = sns.histplot(df, bins=7)
	plt.axvline(x=df.mean(),
            color='red')
	
	fig.figure.savefig('histograma.png')
	return fig

histograma()