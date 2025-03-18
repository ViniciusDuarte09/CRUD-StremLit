import streamlit as st
import controller.UserController as ct
import models.userCRUD as md

col1, col2, col3 = st.columns([0.6, 3, 0.6])

col2.title("Atualizar Cadastros :material/update:")
st.subheader("")

st.write("A funcionalidade de atualização permite modificar os dados dos usuários já cadastrados no sistema. Para isso, basta selecionar o usuário desejado e editar as informações que precisam ser alteradas, como nome, formação, data de nascimento ou e-mail. O sistema garante que as alterações sejam consistentes, verificando se os novos valores não entram em conflito com registros existentes. Após a confirmação, os dados atualizados são armazenados no banco de dados, refletindo imediatamente as mudanças na interface.")

st.divider()

with st.form("updatef", clear_on_submit=True):
    
    with st.container(border= True):
        st.write("Caso deseje atualizar as informações de um usuário, selecione um ID existente na lista e preencha os campos com os novos valores. **Se não quiser alterar um campo específico, basta deixá-lo em branco, e o valor atual será mantido**. Após preencher os dados desejados, clique no botão de atualização para salvar as mudanças.")

    id = st.selectbox(
        "Id do Registro :material/badge:",
        md.User.labelId()
    )

    nome = st.text_input("Nome: :material/badge:", max_chars= 40, placeholder= "Digite o nome: ")
    email = st.text_input("E-Mail: :material/mail:", max_chars= 50, placeholder= "Digite o e-mail: ")
    prof = st.text_input("Profissão: :material/engineering:", max_chars= 30, placeholder= "Digite a profissão: ")
    dataNasc = st.date_input("Data: :material/calendar_month:", None, min_value= "1900-01-01", max_value= "today")
    
    sb = st.form_submit_button("Atualizar Dados :material/upgrade:")

    if sb:

        if nome == "":
            pass

        else:
            checkN = ct.UserController.checkName(nome)
 
            if checkN == True:
                st.warning("Nome já Existente")

            else:
                try:
                    md.User.changeValues(id, "nome", nome)

                except Exception as e:
                    print(e)
                    st.error("Erro ao Atualizar o Cadastro")

                else:
                    st.success("Nome do Registro Atualizado com sucesso!")
                    

        if email == "":
            pass

        else:
            
            checkE = ct.UserController.checkEmail(email)

            if checkE == True:
                st.warning("Email já cadastrado")

            else:
                try:
                    md.User.changeValues(id, "email", email)

                except Exception as e:
                    print(e)
                    st.error("Erro ao Atualizar o Cadastro")

                else:
                    st.success("Email do Registro Atualizado com sucesso!")
                    
        
        if prof == "":
            pass
        
        else:
                try:
                    md.User.changeValues(id, "profissao", prof)

                except Exception as e:
                    print(e)
                    st.error("Erro ao Atualizar o Cadastro")

                else:
                    st.success("Profissao Atualizada com sucesso!")

        if dataNasc is None:
            pass
        
        else:
                try:
                    md.User.changeValues(id, "data_nasc", dataNasc)

                except Exception as e:
                    print(e)
                    st.error("Erro ao Atualizar o Cadastro")

                else:
                    st.success("Data de Nascimento atualizada com sucesso!")
                    
