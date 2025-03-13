import streamlit as st
import controller.UserController as ct
import models.userCRUD as md

col1, col2, col3 = st.columns([0.6, 3, 0.6])

col2.title("Atualizar Cadastros :material/update:")
st.subheader("")

st.write("A funcionalidade de atualização permite modificar os dados dos usuários já cadastrados no sistema. Para isso, basta selecionar o usuário desejado e editar as informações que precisam ser alteradas, como nome, formação, data de nascimento ou e-mail. O sistema garante que as alterações sejam consistentes, verificando se os novos valores não entram em conflito com registros existentes. Após a confirmação, os dados atualizados são armazenados no banco de dados, refletindo imediatamente as mudanças na interface.")

st.divider()

st.selectbox(
    "Teste",
    md.User.labelId()
)