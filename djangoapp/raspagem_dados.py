import requests as rs
import pandas as pd
from io import BytesIO

import os
import django

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE para apontar para as configurações do seu projeto Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Carregue as configurações do Django.
django.setup()

from medicamentos.models import Medicamentos

# URL da planilha a ser raspada
url = "https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos/arquivos/xls_conformidade_gov_20230714_135416984.xls/@@download/file"

print('Running!')

def convert_to_float(value):
    if isinstance(value, str):
        try:
            return float(value.replace(',', '.'))
        except ValueError:
            return value
    return value

# try:
response = rs.get(url)

if response.status_code == 200:
    # Carrega a planilha em BytesIO
    content = BytesIO(response.content)

    # Carrega os dados em um DataFrame
    df = pd.read_excel(content, sheet_name='Planilha1')

    # Formatando a planilha para receber somente os dados
    response_df = df.iloc[59:]
    columns_df = [
        str(c_name).upper() for c_name in list(response_df.iloc[0])
    ]
    data_df = response_df[1:]

    # Dataframe com os dados formatados e organizados
    medicamentos_df = pd.DataFrame(data=data_df.values, columns=columns_df)

    columns_to_convert = [
        'PF SEM IMPOSTOS', 'PF 0%', 'PF 12%', 'PF 17%', 'PF 17% ALC', 'PF 17,5%',
        'PF 17,5% ALC', 'PF 18%', 'PF 18% ALC', 'PF 19%', 'PF 20%', 'PF 21%',
        'PF 22%', 'PMVG SEM IMPOSTOS', 'PMVG 0%', 'PMVG 12%', 'PMVG 17%',
        'PMVG 17% ALC', 'PMVG 17,5%', 'PMVG 17,5% ALC', 'PMVG 18%', 'PMVG 18% ALC',
        'PMVG 19%', 'PMVG 20%', 'PMVG 21%', 'PMVG 22%'
    ]

    medicamentos_df[columns_to_convert] = medicamentos_df[columns_to_convert].applymap(convert_to_float)


    # Percorre cada linha do Dataframe e salva no banco de dados
    for index, row in medicamentos_df.iterrows():
        medicamento = Medicamentos(
            MedicamentoRegistro=row['REGISTRO'],
            MedicamentoPrincipioAtivo=str(row['PRINCÍPIO ATIVO']),
            MedicamentoCnpj=row['CNPJ'],
            MedicamentoLaboratorio=row['LABORATÓRIO'],
            MedicamentoCodGgrem=int(row['CÓDIGO GGREM']),
            MedicamentoEan1=row['EAN 1'],
            MedicamentoEan2=row['EAN 2'],
            MedicamentoEan3=row['EAN 3'],
            MedicamentoProduto=row['PRODUTO'],
            MedicamentoApresentacao=row['APRESENTAÇÃO'],
            MedicamentoClasseTerapeutica=row['CLASSE TERAPÊUTICA'],
            MedicamentoTipoProduto=row['TIPO DE PRODUTO (STATUS DO PRODUTO)'],
            MedicamentoRegimePreco=row['REGIME DE PREÇO'],
            MedicamentoPfSemImposto=float(row['PF SEM IMPOSTOS']),
            MedicamentoPf0=float(row['PF 0%']),
            MedicamentoPf12=float(row['PF 12%']),
            MedicamentoPf17=float(row['PF 17%']),
            MedicamentoPf17Alc=float(row['PF 17% ALC']),
            MedicamentoPf17Meio=float(row['PF 17,5%']),
            MedicamentoPf17MeioAlc=float(row['PF 17,5% ALC']),
            MedicamentoPf18=float(row['PF 18%']),
            MedicamentoPf18Alc=float(row['PF 18% ALC']),
            MedicamentoPf19=float(row['PF 19%']),
            MedicamentoPf20=float(row['PF 20%']),
            MedicamentoPf21=float(row['PF 21%']),
            MedicamentoPf22=float(row['PF 22%']),
            MedicamentoPmvgSemImposto=float(row['PMVG SEM IMPOSTOS']),
            MedicamentoPmvg0=float(row['PMVG 0%']),
            MedicamentoPmvg12=float(row['PMVG 12%']),
            MedicamentoPfPmvg17=float(row['PMVG 17%']),
            MedicamentoPmvg17Alc=float(row['PMVG 17% ALC']),
            MedicamentoPmvg17Meio=float(row['PMVG 17,5%']),
            MedicamentoPmvg17MeioAlc=float(row['PMVG 17,5% ALC']),
            MedicamentoPmvg18=float(row['PMVG 18%']),
            MedicamentoPmvg18Alc=float(row['PMVG 18% ALC']),
            MedicamentoPmvg19=float(row['PMVG 19%']),
            MedicamentoPmvg20=float(row['PMVG 20%']),
            MedicamentoPmvg21=float(row['PMVG 21%']),
            MedicamentoPmvg22=float(row['PMVG 22%']),
            MedicamentoRestricaoHospitalar=row['RESTRIÇÃO HOSPITALAR'],
            MedicamentoCap=row['CAP'],
            MedicamentoComfaz87=row['CONFAZ 87'],
            MedicamentoIcms0=row['ICMS 0%'],
            MedicamentoAnaliseRecursal=row['ANÁLISE RECURSAL'],
            MedicamentoPisConfins=row['LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'],
            MedicamentoComercializacao2022=row['COMERCIALIZAÇÃO 2022'],
            MedicamentoTarja=row['TARJA'],
        )
        medicamento.save()
        print(f'Row {index}: save!')
# except Exception as e:
#     print(str(e))