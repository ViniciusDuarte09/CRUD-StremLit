import database.getConection as db
import pandas as pd
import streamlit as st

class User:
    @staticmethod
    def createUser(nome, data_nasc, profissao, email):

        con = db.connect()
        cursor = con.cursor()

        comando = 'INSERT INTO users(nome, data_nasc, profissao, email) VALUES (\"{}\", \"{}\", \"{}\", \"{}\");'.format(nome, data_nasc, profissao, email)

        cursor.execute(comando)
        con.commit()

        cursor.close()
        con.close()

    @staticmethod
    def allUsersData():

        try:
            con = db.connect()
            cursor = con.cursor()

            comando = 'SELECT * FROM users'

            cursor.execute(comando)
            result = cursor.fetchall()

            cursor.close()
            con.close()

            return result
        
        except:
            print("Problema All")
            return []
        
    @staticmethod
    def searchUserData(view):

        search = str(view)

        con = db.connect()
        cursor = con.cursor()

        if search.isnumeric() == True:

            try:
                comando = 'SELECT * FROM users WHERE id = {}'.format(search)

                cursor.execute(comando)
                result = cursor.fetchall()

                cursor.close()
                con.close()

                return result
            
            except:
                print("Problema Num")
                return []
            
        else:
            
            try:
                comando = 'SELECT * FROM users WHERE nome LIKE \'{}\''.format(search + '%')
                cursor.execute(comando)

                result = cursor.fetchall()

                cursor.close()
                con.close()

                return result
            
            except:
                print("Problema alpha")
                return []
                
    @staticmethod
    def labelId():

        try:
            con = db.connect()
            cursor = con.cursor()

            comando = "SELECT id FROM users ORDER BY id ASC;"

            cursor.execute(comando)
            labelId = cursor.fetchall()

            cursor.close()
            con.close()
            ids = []

            for id in labelId:
                ids.append(id[0])

            print(ids)
            return ids

        except Exception as e:
            print(e)
            return []