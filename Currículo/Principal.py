import streamlit as st


st.title('currículo')
st.header('Frederico Matheus de Oliveira Miraglia')
st.subheader("Analista de dados Jr.")

col1, col2  = st.columns(2)
with col1:
    st.image(image='https://media.licdn.com/dms/image/v2/D4D03AQEHCnj_sz3DpQ/profile-displayphoto-shrink_800_800/B4DZSt8xR2HAAc-/0/1738085176914?e=1746057600&v=beta&t=K__pfWAifAhbw9q3d1R92o9HcdN6VEkiOipwZpasgos',width=250, caption="Frederico Miraglia")

with col2:
    st.write('Nacionalidade: Brasileiro.')
    st.write('Data de nascimento: 22/02/1983.')
    st.write("Estado civil: Casado.")
    st.write('Filhos: Três filhas.')
    st.write('Natural: Rio de janeiro.')
    curriculo = st.container(border=True)
    curriculo.download_button( "Baixar Currículo", 'arquivos/Currículo Frederico Miraglia 2025.pdf'
   , key='download-pdf')


rua = 'Passagem Julio de Menezes'
bairro = 'Paracuri'
ciadade ='Belém'
estado = 'PA'
pais = "Brasil"

cel = "91 99833-9441"
email = "fredericomiraglia@gmail.com"
linkedin = 'https://www.linkedin.com/in/frederico-matheus-miraglia-ab8963120/'

st.header('Endereço: 📪')
st.write(f'Rua: 🪧 {rua}')
st.write(f"Bairro:🏘️ {bairro}")
st.write(f'Cidade: 🏙️ {ciadade}')
st.write(f'Estado: 🏴󠁢󠁲󠁰󠁡󠁿 {estado}')
st.write(f'País: 🇧🇷 {pais}')


st.header('Contatos: ☎️')
st.write(f'Cel:📱 {cel}')
st.write(f'Whatsapp:📱 {cel}')
st.write(f'Email:📧 {email}')
st.write(f'Linkedin: 💼 {linkedin}')
