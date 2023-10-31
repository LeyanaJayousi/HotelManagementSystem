from tkinter import *
from PIL import Image, ImageTk
from istanbul import IstanbulClass
from antalya import AntalyaClass
from fethiye import FethiyeClass
from marmaris import marmarisClass
from izmir import IzmirClass


class IMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Hotel Management system")
        self.root.config(bg="white")

        ######### TITLE #############
        self.icon_title=PhotoImage(file= "photos.png")
        title=Label(self.root, text ="Hotel Management system",image=self.icon_title,compound=LEFT, font =("times new roman", 40, "bold"), bg="pink", fg="black", anchor="w", padx=20).place(x=0, y=0, relwidth=1,height=70)

        ##############log out button#############
        ##logout =Button(self.root,text="Logout", font=("times new roman",15,"bold"), bg="#EE1289", cursor="hand2").place(x=1100,y=10, height=50,width=150)
        
        ###############left part##############
        self.MenuLogo=Image.open("hotel.png")
        self.MenuLogo=self.MenuLogo.resize((200,200), Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE)
        LeftMenu.place(x=0,y=70,width=200,height=623)
        
        lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)
    
        lbl_menu =Label(LeftMenu,text="Hotels", font=("times new roman",20), bg="#33A1C9").pack(side=TOP, fill=X)
        btn_ist=Button(LeftMenu,text="Istanbul",command=self.istanbul, font=("times new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_ayt=Button(LeftMenu,text="Antalya",command=self.antalya, font=("times new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_fth=Button(LeftMenu,text="Fethiye",command=self.fethiye , font=("times new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_mrm=Button(LeftMenu,text="Marmaris",command=self.marmaris, font=("times new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_izm=Button(LeftMenu,text="Izmir", command=self.izmir,font=("times new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit", command=exit,font=("times new roman",20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        

       
        # Create a label with title and text
        title_text1 = "Istanbul"
        description_text1 = "formerly known as Constantinople is the largest city in Turkey, serving as the country's economic, cultural and historic hub. The city straddles the Bosphorus strait, lying in both Europe and Asia, and has a population of over 15 million residents,comprising 19% of the population of Turkey. Istanbul is the most populous European city and the world's 15th-largest city."

        title_text2="Antalya"
        description_text2="It is seen as the capital of tourism in Turkey. Located on Anatolia's southwest coast bordered by the Taurus Mountains, Antalya is the largest Turkish city on the Mediterranean coast outside the Aegean region with over 2.6 million people in its metropolitan area. The city that is now Antalya was first settled around 200 BC by the Attalid dynasty of Pergamon, which was soon conquered by the Romans."
        title_text3="Fethiye"
        description_text3="a city and district of Muğla Province in the Mediterranean Region of Turkey. It is one of the prominent tourist destinations in the Turkish Riviera. In 2019 its population was 162,686.Fethiye was formerly known as Makri (Greek: Μάκρη).[5][6] Modern Fethiye is located on the site of the ancient city of Telmessos, the ruins of which can be seen in the city, e.g. the Hellenistic theatre by the main quay."

        title_text4="Marmaris"
        description_text4=" a port city and tourist resort on the Mediterranean coast, located in Muğla Province, southwest Turkey, along the shoreline of the Turkish Riviera.Although Marmaris is known for its honey, its main source of income is international tourism. It is located between two intersecting sets of mountains by the sea, though following a construction boom in the 1980s."

        title_text5="Izmir"
        description_text5="a metropolitan city on the west coast of Anatolia, and capital of İzmir Province. It is the third most populous city in Turkey, after Istanbul and Ankara, and the largest urban agglomeration on the Aegean Sea.In 2019, the city of İzmir had a population of 2,965,900, while İzmir Province had a total population of 4,367,251"
        ############body#############
        
        #Istanbul hotels
        self.lbl_ist=Label(self.root, text=f"{title_text1}\n\n{description_text1}",bd=4,relief=RIDGE,bg="#FF82AB", wraplength=200,fg="white", font=("goudy old style",16 , "bold"))
        self.lbl_ist.place(x=200,y=70,heigh=600,width=230)
        
        #Antalya hotels
        self.lbl_ayt=Label(self.root, text=f"{title_text2}\n\n{description_text2}",bd=5,relief=RIDGE,bg="#FF82AB", wraplength=200,fg="white", font=("goudy old style",16 , "bold"))
        self.lbl_ayt.place(x=430,y=70,heigh=600,width=230)


        #Fethiye hotels
        self.lbl_fth=Label(self.root,text=f"{title_text3}\n{description_text3}",bd=5,relief=RIDGE,bg="#FF82AB", wraplength=200,fg="white", font=("goudy old style",16 , "bold"))
        self.lbl_fth.place(x=660,y=70,heigh=600,width=230)

        #Marmaris hotels
        self.lbl_mrm=Label(self.root, text=f"{title_text4}\n{description_text4}",bd=5,relief=RIDGE,bg="#FF82AB", wraplength=200,fg="white", font=("goudy old style",16 , "bold"))
        self.lbl_mrm.place(x=890,y=70,heigh=600,width=230)

        #Izmir hotels
        self.lbl_izm=Label(self.root, text=f"{title_text5}\n{description_text5}",bd=5,relief=RIDGE,bg="#FF82AB", wraplength=200,fg="white", font=("goudy old style",16 , "bold"))
        self.lbl_izm.place(x=1120,y=70,heigh=600,width=230)

        ################FOOTER#################
        lbl_footer=Label(self.root, text="Hotel Management System\nFor any technical issue contact +90 (531) 454 98 74", font=("times new roman", 15), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)

    def istanbul(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=IstanbulClass(self.new_win)
    
    def antalya(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AntalyaClass(self.new_win)

    def fethiye(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=FethiyeClass(self.new_win)

    def marmaris(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=marmarisClass(self.new_win)

    def izmir(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=IzmirClass(self.new_win)

    

if __name__ =="__main__":
    root = Tk()
    obj=IMS(root)
    root.mainloop()    