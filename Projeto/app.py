import pandas as pd
import numpy as np
import streamlit as st

# 1. Configuração da página (DEVE ser a primeira linha de comando Streamlit)
st.set_page_config(page_title="Currículo | Frederico Miraglia", page_icon="📊", layout="wide")

# --- CABEÇALHO ---
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Frederico Matheus Miraglia")
    st.write("**Analista de Dados Jr. | Data Science | Estatística Aplicada**")
    st.markdown("""
    📍 Belém, PA | 📱 (91) 9 99833-9441 | 📧 [fredericomiraglia@gmail.com](mailto:fredericomiraglia@gmail.com)
    
    🔗 [LinkedIn](https://www.linkedin.com/in/frederico-miraglia-ab8963120/) | 💻 [GitHub](https://github.com/FredMiraglia)
    """)

with col2:
    # Foto de perfil vinda do GitHub
    st.image("https://avatars.githubusercontent.com/u/68394837?v=4", width=160)

st.divider()

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("📌 Navegação")
    secao = st.radio("Ir para:", ["Resumo Profissional", "Formação Acadêmica", "Experiência", "Habilidades & Cursos"])
    
    st.divider()
    st.subheader("📥 Exportar")
    st.title("📄 Currículo PDF")
    url_curriculo = "https://drive.google.com/file/d/1Z2Zv6-tnvuJ8aotihF-UbhhJHOPKL37B/view?usp=drive_link"
    st.link_button("Abrir arquivo no Drive", url_curriculo)

# --- SEÇÕES DINÂMICAS ---

if secao == "Resumo Profissional":
    st.markdown("### 📊 Perfil Profissional")
    st.write("""
    Analista de Dados com trajetória acadêmica robusta, unindo a base técnica de **Análise e Desenvolvimento de Sistemas** e **Ciência de Dados** à especialização analítica em **Data Science** e **Estatística Aplicada**. 

    Sou apaixonado por decifrar padrões complexos e transformá-los em decisões estratégicas. Utilizo rigor técnico e atenção minuciosa aos detalhes para gerar insights que impulsionam o crescimento e a eficiência operacional das empresas.

    **Principais Competências e Ferramentas:**
    * **Linguagens & Dados:** Conhecimento em Python, SQL e implementação de modelos de Machine Learning.
    * **Análise Estatística:** Aplicação prática de métodos estatísticos para modelagem preditiva e validação de dados.
    * **Visualização:** Desenvolvimento de dashboards avançados em Power BI para suporte crítico à tomada de decisão.
    """)
    
elif secao == "Formação Acadêmica":
    st.markdown("### 🎓 Formação Acadêmica")
    col_form1, col_form2, col_form3 = st.columns(3)
    
    with col_form1:
        st.markdown("**Pós-Graduação em Estatística Aplicada**")
        st.caption("Anhanguera | 07/2025 - 04/2026 (Concluído)")
        st.markdown("**Pós-Graduação em Data Science**")
        st.caption("Descomplica | 04/2023 - 04/2024 (Concluído)")

    with col_form2:
        st.markdown("**Tecnólogo em Ciência de Dados**")
        st.caption("Universidade Cruzeiro do Sul | 09/2020 - 09/2022 (Concluído)")
        st.markdown("**Tecnólogo em Análise e Desenvolvimento de Sistemas**")
        st.caption("Universidade Cruzeiro do Sul | 03/2017 - 03/2019 (Concluído)")

    with col_form3:
        st.markdown("**Técnico em Logística**")
        st.caption("Universidade Cruzeiro do Sul | 01/2019 - 01/2020 (Concluído)")

elif secao == "Experiência":
    st.markdown("### 💼 Experiência Profissional")
    st.markdown("**Vigia Noturno (Segurança Patrimonial)**")
    st.caption("Centro Educacional Interativo Sociedade Simples LTDA | Março de 2016 – Atual")
    st.write("""
    * Vigilância e Monitoramento: Responsável pela integridade física e patrimonial da instituição por mais de 9 anos, demonstrando alto grau de confiança, lealdade e estabilidade profissional.
    * Gestão de Riscos: Atuação preventiva em ambiente de alta responsabilidade, com foco em atenção minuciosa aos detalhes e tomada de decisão sob pressão.
    * Relatórios de Ocorrências: Manutenção de registros precisos de monitoramento, garantindo a organização de dados operacionais para a diretoria.
    * Resiliência e Adaptabilidade: Capacidade comprovada de manter a performance em regimes de trabalho exigentes e horários diferenciados.
    * *Nota: Atualmente em transição de carreira para a área de Dados, aplicando conhecimentos técnicos em projetos práticos.*
    """)
    st.markdown("**PORTEIRO (HOTEL)**")
    st.caption("E MAUES LAVAREDA | 01/10/2013 - 29/05/2015")
    st.write("""* Controle de acesso de visitantes, priorizando a segurança e o atendimento ao cliente com excelência.""")

    st.markdown("**OPERADOR DE MAQUINA**")
    st.caption("MAHLE METAL LEVE S.A. | 16/11/2010 - 15/10/2012")
    st.write("""
    * Operação de maquinário industrial seguindo rigorosos padrões de qualidade e segurança (normas técnicas).
    * Foco em produtividade e redução de erros no processo fabril.""")


elif secao == "Habilidades & Cursos":
    st.markdown("### 🛠️ Habilidades Técnicas")
    habilidades = {
        "Categoria": ["Linguagens", "Banco de Dados", "BI & Visualização", "Ciência de Dados", "Estatística"],
        "Ferramentas": ["Python (Pandas, Numpy, Scikit-learn)", "SQL (MySQL)", "Power BI, Streamlit", "Machine Learning, Modelagem de Dados", "Testes de Hipótese, Regressão"]
    }
    st.table(pd.DataFrame(habilidades))

    st.markdown("### 📚 Educação Complementar (Cursos)")
    cursos = [
        "**Séries Temporais com Redes Neurais Artificiais em Python** - Udemy (14,5h)",
        "**Curso Básico de MySQL** (40h)",
        "**Python para Data Science e Machine Learning** - Udemy (17,5h)",
        "**Ciência de Dados para Empresas e Negócios** - Udemy (14,5h)",
        "**Power BI Avançado** - Udemy (10h)",
        "**Análise de Dados com Python e Machine Learning** - Udemy (5h)"
    ]
    for curso in cursos:
        st.markdown(f"- {curso}")

# --- RODAPÉ ---
st.divider()
st.caption("© 2026 Frederico Miraglia | Currículo desenvolvido com Streamlit")






