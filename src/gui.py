import tkinter as tk
from tkinter import ttk,messagebox
from database import ShopDatabase

class App:
 def __init__(self,r):
  self.r=r; r.title("Shopkeeper Management System 2.0"); r.geometry("1100x650"); self.db=ShopDatabase(); self.sel=None
  self.vars=[tk.StringVar() for _ in range(7)]; self.search=tk.StringVar()
  ttk.Label(r,text="Shopkeeper Management System 2.0",font=("Arial",22,"bold")).pack(pady=15)
  f=ttk.LabelFrame(r,text="Product Details",padding=10); f.pack(fill="x",padx=15)
  names=["Product ID","Product Name","Price","Discount %","Quantity","In Stock","Sold Out"]
  for i,n in enumerate(names):
   ttk.Label(f,text=n).grid(row=i//4*2,column=i%4*2,padx=5,pady=4,sticky="w")
   ttk.Entry(f,textvariable=self.vars[i],width=22).grid(row=i//4*2+1,column=i%4*2,padx=5,pady=4)
  b=ttk.Frame(r); b.pack(fill="x",padx=15,pady=10)
  for t,fn in [("Add",self.add),("Update",self.update),("Delete",self.delete),("Clear",self.clear),("Refresh",self.load)]:
   ttk.Button(b,text=t,command=fn).pack(side="left",padx=4)
  ttk.Label(b,text="Search").pack(side="left",padx=(30,5)); e=ttk.Entry(b,textvariable=self.search,width=25); e.pack(side="left"); e.bind("<KeyRelease>",self.find)
  cols=["pid","name","price","discount","quantity","instock","soldout"]; self.tree=ttk.Treeview(r,columns=cols,show="headings")
  heads=["Product ID","Product Name","Price","Discount %","Quantity","In Stock","Sold Out"]
  for c,h in zip(cols,heads): self.tree.heading(c,text=h); self.tree.column(c,width=140)
  self.tree.pack(fill="both",expand=True,padx=15); self.tree.bind("<<TreeviewSelect>>",self.select)
  self.status=ttk.Label(r,text="Connecting..."); self.status.pack(fill="x")
  try:self.db.connect(); self.load()
  except Exception as ex: messagebox.showerror("Database Error",str(ex))
 def values(self):
  try:
   x=[int(self.vars[0].get()),self.vars[1].get().strip(),float(self.vars[2].get()),float(self.vars[3].get() or 0),int(self.vars[4].get()),int(self.vars[5].get()),int(self.vars[6].get())]
   if not x[1] or min(x[2:])<0 or x[3]>100 or x[4]!=x[5]+x[6]: raise ValueError("Check product values; Quantity must equal In Stock + Sold Out.")
   return tuple(x)
  except ValueError as e: raise ValueError(str(e))
 def add(self):
  try:self.db.add_product(self.values()); self.load(); self.clear()
  except Exception as e:messagebox.showerror("Error",str(e))
 def update(self):
  try:
   v=self.values(); n=self.db.update_product((v[1],v[2],v[3],v[4],v[5],v[6],v[0])); self.load()
   if not n: messagebox.showwarning("Not found","Product ID not found.")
  except Exception as e:messagebox.showerror("Error",str(e))
 def delete(self):
  try:
   n=self.db.delete_product(int(self.vars[0].get())); self.load(); self.clear()
   if not n: messagebox.showwarning("Not found","Product ID not found.")
  except Exception as e:messagebox.showerror("Error",str(e))
 def load(self):
  self.fill(self.db.get_products()); self.status.config(text="Connected to MySQL")
 def find(self,e=None): self.fill(self.db.search_products(self.search.get())) if self.search.get() else self.load()
 def fill(self,rows):
  self.tree.delete(*self.tree.get_children())
  for row in rows:self.tree.insert("", "end",values=row)
 def select(self,e=None):
  s=self.tree.selection()
  if s:
   for v,x in zip(self.vars,self.tree.item(s[0])["values"]):v.set(x)
 def clear(self):
  for v in self.vars:v.set("")
  self.search.set("")
 def close(self):self.db.close();self.r.destroy()

def run_app():
 r=tk.Tk(); a=App(r); r.protocol("WM_DELETE_WINDOW",a.close); r.mainloop()
