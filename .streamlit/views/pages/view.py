import streamlit as st
import models.userCRUD as md
import controller.UserController as ct

col1, col2, col3 = st.columns([0.5, 3 , 0.5])

col2.title("Visualizar Cadastros :material/table:")
st.title("")

st.write("Nesta página, você pode *visualizar e pesquisar* os usuários cadastrados no sistema. As tabelas abaixo exibem informações como **ID, nome, formação, data de nascimento e e-mail.** Além disso, é possível utilizar filtros para buscar usuários específicos, como aqueles cujo nome começa com uma determinada letra. Os dados são exibidos de forma organizada para facilitar a leitura e compreensão. Caso seja necessário *editar ou excluir* um usuário, basta utilizar as opções disponíveis no menu de navegação. Todas as informações são atualizadas automaticamente após qualquer alteração no sistema.")
st.write("")

st.divider()

if st.button("Exibir todos os cadastros", use_container_width=True):
    
    st.write("")

    try:
        st.dataframe(ct.UserController.viewTable(md.User.allUsersData()), use_container_width= True)

    except:
            st.error("Ocorreu um erro ao gerar a tabela")

name_search = st.text_input("Digite ",placeholder="Digite o \"Nome\" do registro ou \"ID\" do Registro", label_visibility="collapsed")

if name_search:
    st.write("")
    
    register = md.User.searchUserData(name_search)

    if register == []:

        st.warning("Cadastro não encontrado, tente novamente!")

    else:

        try:
            st.table(ct.UserController.viewTable(register))

        except:
            st.error("Ocorreu um erro ao gerar a tabela")
