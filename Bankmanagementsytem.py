import mysql.connector as sqlt
conn=sqlt.connect(host="localhost",user="root",passwd="kartik",database="bank")
if conn.is_connected():
    print("Connection success")
                  

while True: 
    print('''
        1: Add customer to the bank.
        2: Delete customer from the bank.
        3: Search for a particular customer in the bank.
        4: Modify the customer details.
        5: For exit. 
        ''')
    ch=int(input("Enter your choice"))

    #adding customer in the bank
    if ch==1:
        a=int(input("Enter the accout number of the customer="))
        b=input("Enter the name of the customer=")
        c=input("Enter the account type=")
        d=int(input("Enter the balance for the account="))
        query="insert into customer(accno,name,acctype,balance) values('{}','{}','{}','{}')".format(a,b,c,d)
        curr=conn.cursor()
        curr.execute(query)
        conn.commit()



    #deleting customer from the database
    elif ch==2:
        curr=conn.cursor()
        curr.execute("select * from customer")
        data=curr.fetchall()
        a=int(input("Enter the account number you want to delete="))
        for x in data:
            if(x[0]==a):
                query="delete from customer where accno='{}'".format(a)
                curr.execute(query)
                conn.commit()
                break
        else:
            print("NO such record is there")



    #searching for a customer record in database
    elif ch==3:
        curr=conn.cursor()
        curr.execute("select * from customer")
        data=curr.fetchall()
        a=int(input("Enter the account number you want to search="))
        for x in data:
            if(x[0]==a):
                print(x[0],x[1],x[2],x[3])
                
                break
        else:
            print("No record found, do you want to add this record yes/no")
            choice=input("Enter your choice=")
            if choice=='yes':
                a=int(input("Enter the accout number of the customer="))
                b=input("Enter the name of the customer=")
                c=input("Enter the account type=")
                d=int(input("Enter the balance for the account="))
                query="insert into customer(accno,name,acctype,balance) values('{}','{}','{}','{}')".format(a,b,c,d)
                curr=conn.cursor()
                curr.execute(query)
                conn.commit()
                
            elif choice=='no':
                print("Ok! You can choose other options")
                


    #modifying customer details
    elif ch==4:
        curr=conn.cursor()
        curr.execute("select * from customer")
        data=curr.fetchall()
        a=int(input("Enter the account number for which you want to modify="))
        for x in data:
            if(x[0]==a):
                print(''' What you want to modify
                            1) Name
                            2) Account Type
                            3) Balance
                        ''')
                ch=int(input("enter your choice"))
                if ch==1:
                    b=input("Enter new name=")
                    curr=conn.cursor()
                    query="update customer set name='{}' where accno='{}'".format(b,a)
                    curr.execute(query)
                    conn.commit()
                    break
                elif ch==2:
                    b=input("Enter new account type=")
                    curr=conn.cursor()
                    query="update customer set acctype='{}' where accno='{}'".format(b,a)
                    curr.execute(query)
                    conn.commit()
                    break
                elif ch==3:
                    b=int(input("Enter new balance="))
                    curr=conn.cursor()
                    query="update customer set balance='{}' where accno='{}'".format(b,a)
                    curr.execute(query)
                    conn.commit()
                    break
            
            


    elif ch==5:
        break
conn.close()
