#instalando pandas no terminal VsCode
pip intall pandas

#importando bibliotecas
import pandas as pd
# import numpy as np

#criando um dicionario
dicionario_cientistas = {
    'NOME' : ['Albert Ainstein', 'Isaac Neetown', 'Marie Curie', 'Richard Feynman', 'Maria Goeppert-Mayer'],
    'DATA_NASCIMENTO' : ['14/03/1879', '04/01/1643', '07/11/1867', '11/05/1918', '28/06/1906'],
    'SEXO': ['Masculino', 'Masculino', 'Feminino', 'Masculino', 'Feminino']
}

#imprimindo na tela o tipo de variavel DICIONARIO_CIENTISTAS
print(f'IMPORTANTE! Vejam o nosso dicionário_cientistas, realmente é um {type(dicionario_cientistas)}\n')

#convertendo nosso dicionário em um DataFrame
df_cientistas = pd.DataFrame(dicionario_cientistas)

#mostrando o resultado
print(df_cientistas)
