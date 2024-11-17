#Essse programa serve para mover os arquivos mais recentes da pasta Downloads para a pasta 'recentes'
import os

#indo para a pasta Downloads
if os.getcwd() != "C:/Users/User/Downloads":
	os.chdir("C:/Users/User/Downloads")
pasta_downloads = os.getcwd()
	
#criando pasta 'recentes se não existir
if not os.path.exists(pasta_downloads + '/' + 'recentes'):
	os.mkdir(pasta_downloads + '/' + 'recentes')

#variaveis
#lista de tuplas com 'periodo de modificação' e arquivo, respectivamente.
lista_arquivos = [x for x in os.listdir(pasta_downloads) if '.pdf' in x or '.jpg' in x] #arquivos de Downloads
lista_periodos = [os.path.getmtime(f'{pasta_downloads}/{arquivo}') for arquivo in lista_arquivos] #tempo de modificação de cada arquivo
juncao_listas = list(zip(lista_periodos, lista_arquivos )) #[(lista_arquivos, lista_periodos)]
ls_arq_recentes = os.listdir(f'{pasta_downloads}/recentes') #arquivos de 'recentes'
pasta_recentes = pasta_downloads + '/' + 'recentes' #pasta 'recentes'



#tirando da pasta recentes arquivos se estiver ocupada
if not ls_arq_recentes == []:
	for arquivo in ls_arq_recentes:
		os.rename(pasta_recentes + '/' + arquivo, pasta_downloads + '/' + arquivo)


#movendo arquivos para a pasta 'recentes'
juncao_listas.sort(reverse=True)

#movendo os arquivos para pasta 'recentes'
if len(juncao_listas) >= 4:
	for arquivo in juncao_listas[:3]:
		if '.pdf' in arquivo[1] or '.jpg' in arquivo[1]:
			os.rename(f'{pasta_downloads}/{arquivo[1]}', f'{pasta_downloads}/recentes/{arquivo[1]}')
else:
	for arquivo in juncao_listas:
		if '.pdf' in arquivo[1] or '.jpg' in arquivo[1]:
				os.rename(f'{pasta_downloads}/{arquivo[1]}', f'{pasta_downloads}/recentes/{arquivo[1]}')