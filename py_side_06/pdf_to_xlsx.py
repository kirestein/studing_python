import tabula as tb
import pandas as pd

pdf_01 = '/run/media/erik_proenca/Elements/projetos/Nubank_2023-05-11.pdf'
pdf_02 = '/run/media/erik_proenca/Elements/projetos/Nubank_2023-06-11.pdf'

csv_01 = '/run/media/erik_proenca/Elements/projetos/Nubank_2023-05-11.xlsx'
csv_02 = '/run/media/erik_proenca/Elements/projetos/Nubank_2023-06-11.xlsx'

tb.convert_into(pdf_01, csv_01, output_format='csv', pages='all')
tb.convert_into(pdf_02, csv_02, output_format='csv', pages='all')

df_01 = pd.read_csv(csv_01)
df_02 = pd.read_csv(csv_02)
df_01.to_excel('Nubank_2023-05-11.xlsx', index=False)
df_02.to_excel('Nubank_2023-06-11.xlsx', index=False)
