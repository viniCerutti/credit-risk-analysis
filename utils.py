import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_hist_box_plot(dados,y,x=None,figsize=(10,5)):
	"""
	Metodo que constroi um grafico de boxplot, histograma e 
	analise descritiva sobre aquelas variaveis
	Parametros
	----------
	dados : {pandas dataframe}
		conjunto de dados
	y : {pandas series}
		valores para eixo Y

	x : {pandas series}
		valores para eixo x e que fará a divisão dos dados

	figsize : {Tupla}, optional
	  Tamanho da figura a ser exibida
	"""
	fig, axs = plt.subplots(ncols=2,figsize=figsize)
	g1 = sns.boxplot(x=x, y=y, data=dados, ax=axs[0])
	sns.histplot(x=y, hue=x, data=dados, kde=True, ax=axs[1])
	sns.despine(bottom = True, left = True)
	# verifica se ha um dado de agrupamento
	if x is not None:
	 print(dados.groupby(x)[y].describe())
	else:
	 print(dados[y].describe())

def tabela_frequencia(dados,x,y):
	"""
	Metodo que constroi uma tabela de frequencia em porcentagens
	Parametros
	----------
	dados : {pandas dataframe}
	conjunto de dados
	y : {pandas series}
	valores para serem utilizados nas linhas

	x : {pandas series}
	valores para serem utilizados nas colunas
	"""
	print(dados[x].value_counts(normalize=True))
	print('\n\nPorcentagem por Linha\n\n')    
	print(pd.crosstab(dados[x],dados[y],normalize='index'))
	print('\n\nPorcentagem por Coluna\n\n')
	print(pd.crosstab(dados[x],dados[y],normalize='columns'))
