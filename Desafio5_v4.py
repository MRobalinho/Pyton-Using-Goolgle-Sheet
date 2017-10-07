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

# Ler um registo especifico
print('----  Informe o numero da linha a ler da Sheet : '+xsheet)
number_1 = int(input('Insira um numero da linha :'))

def lerlinha(number_1):
	# Ler uma linha
	# alunos = sheet.row_values(number_1)

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

#-----------------------------	
	
if ( number_1 > 1 ):
  lerlinha(number_1)
else:	
  print(" ")
  print("Erro - Linha deve ser superior a 1")

  