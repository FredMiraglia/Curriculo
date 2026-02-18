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
    
    🔗 [LinkedIn](https://www.linkedin.com/in/frederico-matheus-miraglia-ab8963120/) | 💻 [GitHub](https://github.com/FredMiraglia)
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
    
    # BOTÃO DE DOWNLOAD (Colocado na sidebar para ficar sempre acessível)
    st.divider()
    st.title("📄 Currículo PDF")
    url_curriculo = "https://drive.google.com/file/d/1Vw8X4QpzlPibn-BS2EM7aEpo5lLIDa2g/view?usp=drive_link"
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
        st.caption("Anhanguera | 07/2024 - 05/2025 (Em andamento)")
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
    st.markdown("**Vigia Noturno**")
    st.caption("Centro Educacional Interativo Sociedade Simples LTDA | 03/2016 - Atual")
    st.write("""
    * Atuação em ambiente de alta responsabilidade, exigindo atenção minuciosa aos detalhes e resiliência.
    * Gestão de segurança patrimonial e monitoramento, demonstrando compromisso e estabilidade profissional (10 anos de casa).
    * *Nota: Atualmente em transição de carreira para a área de Dados, aplicando conhecimentos técnicos em projetos práticos.*
    """)

elif secao == "Habilidades & Cursos":
    st.markdown("### 🛠️ Habilidades Técnicas")
    habilidades = {
        "Categoria": ["Linguagens", "Banco de Dados", "BI & Visualização", "Ciência de Dados", "Estatística"],
        "Ferramentas": ["Python (Pandas, Numpy, Scikit-learn)", "SQL (MySQL)", "Power BI, Streamlit", "Machine Learning, Modelagem de Dados", "Testes de Hipótese, Regressão"]
    }
    st.table(pd.DataFrame(habilidades))

    st.markdown("### 📚 Educação Complementar (Cursos)")
    cursos = [
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

