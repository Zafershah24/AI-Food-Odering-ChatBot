import mysql.connector
def DataUpdate1(Name,Number,vegpizza,nvegpizza,size,topping,crust_type,quantity): 
    
    sqldb = mysql.connector.connect( host="localhost", user="root",  
    passwd="root", database="CustomerOrder") 
    mycursor = sqldb.cursor() 
    sql='INSERT INTO CustomerDetails1 (name,number,vegpizza,nvegpizza,size,topping,crust_type,quantity) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}");'.format(Name,Number,vegpizza,nvegpizza,size,topping,crust_type,quantity) 
    mycursor.execute(sql) 
    sqldb.commit()


def DataUpdate2(Name,Number,side): 
    
    sqldb = mysql.connector.connect( host="localhost", user="root",  
    passwd="root", database="CustomerOrder") 
    mycursor = sqldb.cursor() 
    sql='INSERT INTO CustomerDetails1 (name,number,side) VALUES ("{0}","{1}","{2}");'.format(Name,Number,side) 
    mycursor.execute(sql) 
    sqldb.commit()