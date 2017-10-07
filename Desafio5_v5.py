# Python lendo folhas de calculo do google drive
# Testes para o Desafio 5 - Manuel Robalinho

# Import das bibliotecas necessárias
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds']
# File de credenciais (JSON)
creds = ServiceAccountCredentials.from_json_keyfile_name('upt-mrobalinho.json', scope)
client = gspread.authorize(creds)

# Spreadsheet a ler
xsheet = "Alunos"
# Open da Spreadsheet 
sheet = client.open(xsheet).sheet1
# Leitura da Spreadsheet de todos os registos
# alunos = sheet.get_all_records()


	
def ler_linha(number_1):
	# Ler uma linha
	# alunos = sheet.row_values(number_1)
	if (number_1 > 1):
  
		pp = pprint.PrettyPrinter()
		# Ler e imprimir cabeçalho ( Row 1)
		xnum      = sheet.cell(1,1).value
		xnome     = sheet.cell(1,2).value
		xendereco = sheet.cell(1,3).value
		xemail    = sheet.cell(1,4).value
		xdata     = sheet.cell(1,5).value
		pp.pprint("---------------------------------------------------------------------")
		pp.pprint(xnum + " | " + xnome + "           | " + xendereco + " | " + xemail + " | " + xdata)
		pp.pprint("---------------------------------------------------------------------")

		# Ler Celula a célula
		xnum      = sheet.cell(number_1,1).value
		xnome     = sheet.cell(number_1,2).value
		xendereco = sheet.cell(number_1,3).value
		xemail    = sheet.cell(number_1,4).value
		xdata     = sheet.cell(number_1,5).value

		# Impressao do resultado
		pp.pprint(xnum + "   | " + xnome + " | " + xendereco + " | " + xemail + " | " + xdata)
	else:	
	  print(" ")
	  print("Erro - Linha deve ser superior a 1")
	return	  
#-----------------------------	


def insere_linha(index):	
    # Inserir registo
	print('----  Informe os dados do Aluno para a Sheet : '+xsheet)
	xnum      = input('Numero         :')
	xnome     = input('Nome           :')
	xendereco = input('Endereço       :')
	xemail    = input('Email          :')
	xdata     = input('Data Nascimento:')	
	row = [xnum, xnome, xendereco, xemail, xdata ]
	sheet.insert_row(row, index)
	print("Inserção executada na linha "+str(index))
	return		
#---------------------------------------

def elimina_linha(number_1):
    # Eliminar registo
	if (number_1 > 1):
		sheet.delete_row(number_1)
		print("Eliminação executada na linha "+str(number_1))
	else:	
		print(" ")
		print("Erro - Linha deve ser superior a 1")
	return		
#---------------------------------------


# Informar a operação a executar
xoper = input('''
----  Informe a operação a executar
       I - Inserir uma linha
       E - Eliminar uma linha
       L - Ler uma linha	   
	   Opção : ''')
	
if (xoper == "L"):
  	# Ler um registo especifico
	print('----  Informe o numero da linha a ler da Sheet : '+xsheet)
	number_1 = int(input('Insira um numero da linha :'))
	ler_linha(number_1)

elif (xoper == "I"):
	# Inserir registo
	index = 2
	insere_linha(index)
	
elif (xoper == "E"):  
	# Eliminar registo  
	print('----  Informe o numero da linha a eliminar da Sheet : '+xsheet)
	number_1 = int(input('Insira um numero da linha :'))
	ler_linha(number_1)
	elimina_linha(number_1)
else:
  print('ERRO - Operação errada ') 
  