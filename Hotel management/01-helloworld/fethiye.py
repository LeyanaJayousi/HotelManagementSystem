from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class FethiyeClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("")
        self.root.config(bg="white")
        self.root.focus_force()

        # Definingn variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_fthhtl_id=StringVar()
        self.var_name=StringVar()
        self.var_area=StringVar()
        self.var_Category=StringVar()
        self.var_board=StringVar()
        self.var_Website=StringVar()
        



        ########### search #########  
        SearchFrame=LabelFrame(self.root, text ="Search Hotel", font=("goudy old style",15, "bold" ), bd=2, relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #### options #####
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=("Select","Name","Area","Category"), state ='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        cmb_cat=ttk.Combobox(self.root,textvariable=self.var_Category, values=("Select","Special Category","3 Stars","4 Stars","5 Stars", "Luxury"), state ='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_cat.place(x=850,y=150,width=180)
        cmb_cat.current(0)
        #txt_htlarea=Entry (self.root, textvariable=self.var_area, font= ("goudy old style", 15), bg="white").place(x=150,y=350,width=180)
        cmb_area=ttk.Combobox(self.root,textvariable=self.var_area, values=("Select","Taksim","Fatih","Laleli","Beşiktaş", "Nişantaşı", "Asian side"), state ='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_area.place(x=150,y=250,width=180)
        cmb_area.current(0)
        #txr_htlboard=Entry (self.root, textvariable=self.var_board, font= ("goudy old style", 15), bg="white").place(x=850,y=350,width=180)
        cmb_board=ttk.Combobox(self.root,textvariable=self.var_board, values=("Select", "Room only","Bed and breakfast","Half board","All inclusive","Ultra all-inclusive"), state ='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_board.place(x=850,y=250,width=180)
        cmb_board.current(0)
        
        txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt ,font=("goudy old style",15), bg="#FFE4E1").place(x=200,y=10)
        btn_search=Button(SearchFrame, text="Search",font=("goudy old style",15), bg="#FFAEB9",fg="white",cursor="hand2").place(x=410,y=10, width=150,height=30)
        
        ###############3 Title ################
        title=Label(self.root, text="Hotel Details", font=("goudy old style",15), bg="#FFAEB9",fg="white").place(x=50,y=100, width=1000,height=30)

        ##############content###########
        #Labels
        lbl_htlid=Label (self.root, text="Hotel ID", font= ("goudy old style", 15), bg="white").place(x=50,y=150)
        lbl_htlname=Label (self.root, text="Name", font= ("goudy old style", 15), bg="white").place(x=350,y=150)
        lbl_htlcat=Label (self.root, text="Category", font= ("goudy old style", 15), bg="white").place(x=750,y=150)
        lbl_htlarea=Label (self.root, text="Area", font= ("goudy old style", 15), bg="white").place(x=50,y=250)
        lbl_htlboard=Label (self.root, text="Board basis", font= ("goudy old style", 15), bg="white").place(x=730,y=250)
        lbl_htlweb=Label (self.root, text="Website", font= ("goudy old style", 15), bg="white").place(x=350,y=250)
        
        #texts
        txt_htlid=Entry (self.root, textvariable=self.var_fthhtl_id, font= ("goudy old style", 15), bg="white").place(x=150,y=150,width=180)
        txt_htlname=Entry (self.root, textvariable=self.var_name, font= ("goudy old style", 15), bg="white").place(x=450,y=150,width=180)
        #txt_htlcat=Entry (self.root, textvariable=self.var_Category, font= ("goudy old style", 15), bg="white").place(x=850,y=150,width=180)
        
        txt_htlweb=Entry (self.root, textvariable=self.var_Website, font= ("goudy old style", 15), bg="white").place(x=450,y=250,width=180)
        

        ############## Buttons ############
        btn_add=Button(self.root, text="Save", font=("goudy old style",15), bg="#FFAEB9",fg="white",cursor="hand2").place(x=50,y=310, width=110,height=28)
        btn_update=Button(self.root, text="Update",font=("goudy old style",15), bg="#FFAEB9",fg="white",cursor="hand2").place(x=220,y=310, width=110,height=28)
        btn_delete=Button(self.root, text="Delete",font=("goudy old style",15), bg="#FFAEB9",fg="white",cursor="hand2").place(x=390,y=310, width=110,height=28)
        btn_clear=Button(self.root, text="Clear",font=("goudy old style",15), bg="#FFAEB9",fg="white",cursor="hand2").place(x=570,y=310, width=110,height=28)


        ############### Hotel Details (table) ##########
        emp_frame= Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly=Scrollbar(emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)

        self.Hoteltable= ttk.Treeview(emp_frame, columns=("HotelID", "Name", "Category", "area", "website","Board"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Hoteltable.xview)
        scrolly.config(command=self.Hoteltable.yview)
        self.Hoteltable.heading("HotelID", text="Hotel ID")
        self.Hoteltable.heading("Name", text="Hotel name")
        self.Hoteltable.heading("Category", text="Hotel Category")
        self.Hoteltable.heading("area", text="Hotel area")
        self.Hoteltable.heading("website", text="Hotel Website")
        self.Hoteltable.heading("Board", text="Board Basis")
        
        self.Hoteltable["show"]= "headings"

        self.Hoteltable.column("HotelID", width=90)
        self.Hoteltable.column("Name",  width=120)
        self.Hoteltable.column("Category",  width=120)
        self.Hoteltable.column("area",  width=120)
        self.Hoteltable.column("website",  width=120)
        self.Hoteltable.column("Board",  width=120)
        
        
        self.Hoteltable.pack(fill=BOTH, expand=1)


#################################################################
        
          


if __name__ =="__main__":
    root = Tk()
    obj=FethiyeClass(root)
    root.mainloop()    