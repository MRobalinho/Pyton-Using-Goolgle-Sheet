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
# Ler uma linha
alunos = sheet.row_values(number_1)

pp = pprint.PrettyPrinter()
# Impressao do resultado
pp.pprint(alunos)