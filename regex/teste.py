from datetime import datetime 
import pytest
import re

def validateDatePatternYDM(date: str) -> bool:
	"""
	Função que verifica se uma string de data é válida e está no formato YY-MM-DD.

	:param date: String de data.
	:return: Retorna um boolean. True caso a string seja válida, False inválida
	"""
	pattern = r'^([0-9]{4})\-(1[0-2]|0[1-9]|[1-9])\-((3[0-1])$|([1-2][0-9]$)|(0[1-9])$|([1-9])$)'
	matches = re.match(pattern= pattern, string= date)
	return bool(matches)

def convertDateDMY(date: str)-> str:
	"""
	Função que converta data no formato YY-MM-DD para DD/MM/YY.

	:param date: String de data.
	:return: Retorna string no formato DD/MM/YY
	"""
	dateObject = datetime.strptime(date, r'%Y-%m-%d')
	return dateObject.strftime(r'%d/%m/%Y')

def validateYDMConvertDMY(date: str)-> str:
	"""
	Função que verifica se string está no formato YY-MM-DD caso sim converte para formato DD/MM/YY, caso não retorna um exceção.

	:param date: String de data.
	:return: Retorna string no formato DD/MM/YY ou Exceção
	"""
	isValid = validateDatePatternYDM(date)
	if not(isValid): raise ValueError('Date Format is Invalid') 
	return convertDateDMY(date)


def test_validateYDMConvertDMY():
	"""
	Testes unitários de validateYDMConvertDMY.
	"""

	# Teste com uma datas válidas no formato correto
	assert validateYDMConvertDMY('2024-04-01') == '01/04/2024'
	assert validateYDMConvertDMY('2024-4-01') == '01/04/2024'
	assert validateYDMConvertDMY('2024-04-1') == '01/04/2024'

	# Teste com uma data no formato inválido (dia maior que 31)
	with pytest.raises(ValueError):
		validateYDMConvertDMY('2024-04-32')
	
	# Teste com uma data no formato inválido (mês maior que 12)
	with pytest.raises(ValueError):
		validateYDMConvertDMY('2024-13-01')
	
	# Teste com uma data no formato inválido (ano com menos de 4 dígitos)
	with pytest.raises(ValueError):
		validateYDMConvertDMY('24-04-01')
	
	# Teste com uma data no formato inválido (ano com mais de 4 dígitos)
	with pytest.raises(ValueError):
		validateYDMConvertDMY('20244-04-01')
	
	# Teste com uma data no formato inválido (formato incorreto de separador)
	with pytest.raises(ValueError):
		validateYDMConvertDMY('2024/04/01')
	
	# Teste com uma data no formato inválido (data vazia)
	with pytest.raises(ValueError):
		validateYDMConvertDMY('')
	
	# Teste com uma data no formato inválido (data no formato incorreto)
	with pytest.raises(ValueError):
		validateYDMConvertDMY('2024-20-01')