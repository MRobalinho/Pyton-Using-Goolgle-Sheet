# Python lendo folhas de calculo do google drive
# Testes para o Desafio 5 - Manuel Robalinho

# Import das bibliotecas necessárias
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
# File de credenciais (JSON)
creds = ServiceAccountCredentials.from_json_keyfile_name('upt-mrobalinho.json', scope)
client = gspread.authorize(creds)

# Spreadsheet a ler
xsheet = "Alunos"
# Open da Spreadsheet 
sheet = client.open(xsheet).sheet1
# Leitura da Spreadsheet de todos os registos
alunos = sheet.get_all_records()

print(alunos)