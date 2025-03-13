import streamlit as st

col1, col2, col3 = st.columns([0.65,3.5,0.65])

with col2:
    st.subheader("Sistema de Gerenciamento de Dados :material/database:")

st.title("")
st.write("Este é um sistema simples de **CRUD (Criar, Ler, Atualizar e Deletar)**, onde você pode gerenciar usuários de forma prática e eficiente. **Seja bem vindo!!**")
st.divider()

st.subheader("Sinta-se a vontade para: ")
st.write('''
- ✅ Visualizar a lista de usuários cadastrados.\n
- ✅ Adicionar novos usuários ao sistema.\n
- ✅ Editar informações de usuários existentes.\n
- ✅ Remover usuários quando necessário.\n
''')

st.write("Além disso, você pode acompanhar um resumo geral dos usuários cadastrados, visualizar estatísticas e acessar rapidamente as principais funcionalidades do sistema. 🚀")
st.divider()

st.subheader("**Acesse as funcionalidade:**")
st.write("")

st.page_link(page= "views/pages/create.py", 
            label= "Adicionar Cadastro", 
            icon= "✔" 
            )

st.page_link(page= "views/pages/update.py", 
            label= "Atualizar Dados", 
            icon= "♻" 
            )

st.page_link(page= "views/pages/view.py", 
            label= "Exbir Dados", 
            icon= "👁" 
            )

st.page_link(page= "views/pages/delete.py", 
            label= "Deletar Cadastro", 
            icon= "‼" 
            )

st.divider()
