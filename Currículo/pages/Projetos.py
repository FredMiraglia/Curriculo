import streamlit as st
import pandas as pd




st.title("Projetos")


col1, col2 = st.columns(2)
with col1:
    data_df = pd.DataFrame(
        {
            "Projetos análise de dados": [
                "Fraude (Classifição)",
                "Séries Temporais",
                "Floresta aleatória (Classifição)",
                "Câncer (Classifição)",
                'Doenças cardíacas (Classifição)',
                'Mercado Financeiro',
                'Modelo de recomendação baseado em item',
                'Diabetes (Classifição)',
                'KNN',
                'Kmeans (Cluster)',
                'SVM (Classifição)',
                'Regreção Linear',

            ],
            "creator": [
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Analise_de_fraude.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Analise_series_Temporais.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Arvore_decisao__Floresta_aleat%C3%B3ria.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Cancer_otimos.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Doen%C3%A7as_Card%C3%ADacas.ipynb',            
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Mercado_financeiro.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/ModeloRecomenda%C3%A7%C3%A3o_baseado_item.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Pimma_diabets.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Projeto_KNN.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Projeto_Kmeans.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Projeto_svm.ipynb',
                'https://github.com/FredMiraglia/projeto_analise_dados/blob/main/Regress%C3%A3o_linear.ipynb',
            ],
        }
    )
    st.data_editor(
        data_df,
        column_config={
            "apps": st.column_config.LinkColumn(
                "Trending apps",
                help="The top trending Streamlit apps",
                validate=r"^https://[a-z]+\.streamlit\.app$",
                max_chars=500,
                display_text=r"https://(.*?)\.streamlit\.app"
            ),
            "creator": st.column_config.LinkColumn(
                "Abrir Projetos", display_text="Open profile"
            ),
        },
        hide_index=True,
    )

    