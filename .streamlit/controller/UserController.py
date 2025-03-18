import models.userCRUD as md
import pandas as pd

class UserController:

    @staticmethod
    def viewTable(dados):

        colunas = ["ID", "Nome", "Formação", "Data De Nascimento", "E-Mail"]
        result = pd.DataFrame(dados, columns = colunas)

        return result
    
    @staticmethod
    def checkName(name):

        df = md.User.allUsersData()

        for user in df:
            if name == user[1]:
                return True

    
        return False
    
    @staticmethod
    def checkEmail(email):

        df = md.User.allUsersData()

        for user in df:
            if email == user[4]:
                return True

    
        return False
    