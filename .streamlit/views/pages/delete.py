import streamlit as st
import models.userCRUD as md

col1, col2, col3 = st.columns([0.65,3,0.65])

col2.title("Deletar Cadastro :material/delete:")
st.subheader("")

st.write("Na seção de exclusão, você pode remover um usuário existente do banco de dados. Para isso, selecione o ID do usuário que deseja deletar. **Atenção: essa ação é irreversível, então certifique-se antes de prosseguir.**")
st.write("")
st.divider()
st.write("")

with st.container(border=True):
    id = st.selectbox(
        "Selecione o id do Registro :material/badge::",
        md.User.labelId()
    )

    cancel = st.button(":red[Deletar]", use_container_width=True)

    if cancel:
        st.divider()

        user = md.User.searchUserData(id)

        st.write("Tem certeza que deseja apagar o registro de: **{}**?".format(user[0][1]))
        s = st.button(":green[Sim]", use_container_width=True)
        n = st.button(":red[Cancelar]", use_container_width=True)

        if s:
            try:
                md.User.deleteUser(id=id)

            except Exception as e:
                print(e)
                st.error("Erro ao deletar Registro")

            else:
                st.success("Registro Apagado com sucesso!")

        if n:
            pass

