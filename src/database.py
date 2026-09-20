import mysql.connector
from utils import load_config

class ShopDatabase:
    def __init__(self): self.connection=None
    def connect(self):
        c=load_config()
        self.connection=mysql.connector.connect(host=c["host"],port=int(c["port"]),user=c["user"],password=c["password"],database=c["database"])
        self.create_table()
    def close(self):
        if self.connection and self.connection.is_connected(): self.connection.close()
    def create_table(self):
        q='''CREATE TABLE IF NOT EXISTS kirana(
        pid INT PRIMARY KEY,pname VARCHAR(100) NOT NULL,price DECIMAL(10,2) NOT NULL,
        discount DECIMAL(5,2) DEFAULT 0,quantity INT NOT NULL,instock INT NOT NULL,soldout INT NOT NULL)'''
        cur=self.connection.cursor(); cur.execute(q); self.connection.commit(); cur.close()
    def add_product(self,p):
        cur=self.connection.cursor(); cur.execute("INSERT INTO kirana VALUES(%s,%s,%s,%s,%s,%s,%s)",p); self.connection.commit(); cur.close()
    def get_products(self):
        cur=self.connection.cursor(); cur.execute("SELECT * FROM kirana ORDER BY pid"); r=cur.fetchall(); cur.close(); return r
    def search_products(self,k):
        cur=self.connection.cursor(); p=f"%{k}%"; cur.execute("SELECT * FROM kirana WHERE CAST(pid AS CHAR) LIKE %s OR pname LIKE %s ORDER BY pid",(p,p)); r=cur.fetchall(); cur.close(); return r
    def update_product(self,p):
        cur=self.connection.cursor(); cur.execute("UPDATE kirana SET pname=%s,price=%s,discount=%s,quantity=%s,instock=%s,soldout=%s WHERE pid=%s",p); self.connection.commit(); n=cur.rowcount; cur.close(); return n
    def delete_product(self,pid):
        cur=self.connection.cursor(); cur.execute("DELETE FROM kirana WHERE pid=%s",(pid,)); self.connection.commit(); n=cur.rowcount; cur.close(); return n
