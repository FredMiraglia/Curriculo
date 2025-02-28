import streamlit as st 
container = st.container(border=True)
superior1 = "2020-2021 | Tecnólogo em Ciência de dados"
superior2 = "2017-2018 | Tecnólogo em Análise e Desenvolvimento de Sistemas"
pos='2023- 2024| Pós-Graduação em Data Science Descomplica'

st.header("FORMAÇÃO: ")

academica = st.container(border=True)
academica.write(f"Pós-graduação: {pos}")
academica.write(f'Curso superior: {superior1}')
academica.write(f'Curso superior: {superior2}')


curso1 ='Curso Básico de MySQL Carga horária: 40 horas.'
curso2 = 'Curso de Algoritmo Carga horária: 40 horas.'
curso3 ='Curso de Algoritmo Carga horária: 40 horas.'
curso4 = 'Python para Data Science e Machine learning – Udemy Carga horária 17,5 horas.'
curso5 = 'Ciência de dados para Empresa e negócios – Udemy Carga horária 14,5 horas.'
curso6 = 'Power BI - Avançado - Udemy Carga horária 10 horas.'

hab1= "Python: experiência em programação com Python, incluindo bibliotecas como pandas, NumPy e scikit-learn."
hab2="Análise de dados: habilidades em manipulação, limpeza e visualização de dados. Machine Learning: conhecimento básico em algoritmos de aprendizado de máquina e sua implementação em Python."
hab3="SQL: familiaridade com consultas e manipulação de bancos de dados."
hab4='Visualização de dados: habilidades em criação de gráficos e visualizações usando bibliotecas como Matplotlib e Seaborn.'

st.header('H A B I L I D A D E S')
habilidades = st.container(border=True)
habilidades.write(f'{hab1}')
habilidades.write(f'{hab2}')
habilidades.write(f'{hab3}')
habilidades.write(f'{hab4}')


st.header('E D U C A Ç Ã O   C O M P L E M E N T A R: ')
qualificacao = st.container(border=True)
qualificacao.write(f'{curso1}')
qualificacao.write(f'{curso2}')
qualificacao.write(f'{curso3}')
qualificacao.write(f'{curso4}')
qualificacao.write(f'{curso5}')
qualificacao.write(f'{curso6}')


