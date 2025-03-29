import streamlit as st
import models.userCRUD as md
from controller.UserController import UserController
import datetime

col1, col2, col3 = st.columns([0.6, 3, 0.6])

col2.title("Adicionar Cadastro :material/person_add:")
st.title("")

st.write("Nesta seção, você pode adicionar novos usuários ao sistema. Basta preencher os campos obrigatórios, como **nome, e-mail, data de nascimento e cargo**, e clicar no botão de cadastro. O sistema verificará se o e-mail já está cadastrado para evitar duplicações. Após a criação, o novo usuário será salvo no banco de dados e poderá ser visualizado na tabela principal.")

st.divider()
st.write("")

with st.form("createR", clear_on_submit= True):

    nome = st.text_input("Nome: :material/badge:", max_chars= 40, placeholder= "Digite o nome:")
    email = st.text_input("E-Mail: :material/mail:", max_chars= 50, placeholder= "Digite o e-mail, ele deve ser único")
    prof = st.text_input("Profissão: :material/engineering:", max_chars= 30, placeholder= "Digite a profissão:")
    dataNasc = st.date_input("Data de Nascimento :material/calendar_month:", None, min_value= "1900-01-01", max_value= "today")

    sb = st.form_submit_button("Criar Registro", use_container_width= True, icon= ":material/person_add:")

    if sb:
        checkN = UserController.checkName(nome)
        checkE = UserController.checkEmail(email)

        if checkN == True or checkE == True:
            st.warning("Nome ou E-mail Já Existentes")

        else:
            if nome != "" and email != "":
                if UserController.emailValidation(email) == True:
                    try:
                        md.User.createUser(nome, dataNasc, prof, email)

                    except Exception as e:
                        st.error("Erro ao Criar o Registro")
                        print(e)

                    else:
                        st.success("Úsuario criado com sucesso")

                else:
                    st.warning("Email não válido")

            else:
                st.warning("Nome ou E-mail não inseridos")

