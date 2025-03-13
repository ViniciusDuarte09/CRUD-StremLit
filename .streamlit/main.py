import streamlit as st

# -- Configuração das Página --
home_page = st.Page(
    page= "views/pages/home.py",
    title= "Home_Page",
    icon= ":material/home:",
    default=True
)

aboutme_page = st.Page(
    page = "views/pages/aboutMe.py",
    title="Sobre Mim 😃",
    icon=":material/person:"
)

create_page = st.Page(
    page= "views/pages/create.py",
    title= "Criar",
    icon= ":material/add_circle:"
)

delete_page = st.Page(
    page = "views/pages/delete.py",
    title = "Excluir",
    icon= ":material/cancel:"
)

update_page = st.Page(
    page = "views/pages/update.py",
    title = "Atualizar",
    icon= ":material/autorenew:"
)

view_page = st.Page(
    page = "views/pages/view.py",
    title = "Exibir",
    icon= ":material/search:"
)

# -- Navegação --
pages = st.navigation(
    {
    "CRUD" : [home_page, create_page, view_page, update_page, delete_page],
     "Sobre" : [aboutme_page]
    }
    )

pages.run()
