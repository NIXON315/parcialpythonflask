from src.conexion_bd.basedb import mysql
from flask import request, redirect, flash
class DatabaseModel():
    def lists(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SHOW DATABASES") 
        data = cursor.fetchall()
        cursor.close()
        return data
    def create(self, databases):
        cursor = mysql.get_db().cursor()
        cursor.execute("CREATE DATABASE `%s`" %databases,)
        mysql.get_db().commit()
        cursor.close()    
    def listTables(self, datab):
        cursor = mysql.get_db().cursor()
        cursor.execute("SHOW TABLES FROM `%s`" %datab)
        data = cursor.fetchall()
        cursor.close()
        return data