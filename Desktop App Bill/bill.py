from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
        def __init__(self,root):
            self.root = root
            self.root.geometry("1350x750+0+0")
            self.root.title("Billing System Software")
            bg_color = "pink"
            title = Label(self.root,text='*** Billing System Software ***',bd=9,relief=GROOVE,bg=bg_color,fg='red',font=("times new roman",30,'bold'),pady=2).pack(fill=X)
            
            #======= Variables ===========

            #======= Cosmetics ========
            self.soap = IntVar()
            self.cream = IntVar()
            self.wash = IntVar()
            self.spray = IntVar()
            self.gell = IntVar()
            self.loshan = IntVar()

            #======= Grocery ========

            self.rice = IntVar()
            self.oil = IntVar()
            self.daal = IntVar()
            self.wheat = IntVar()
            self.sugar = IntVar()
            self.tea = IntVar()
   
   
            #======= Cold Drinks ========

            self.maza = IntVar()
            self.cocka= IntVar()
            self.frooti = IntVar()
            self.thumbsup = IntVar()
            self.limca = IntVar()
            self.sprite = IntVar()

            
            #======= Total Products and Tax Variabels ========

            self.cosmetic = StringVar()
            self.grocery = StringVar()
            self.cold_drink = StringVar()
           
           
            self.cosmetic_tax = StringVar()
            self.grocery_tax = StringVar()
            self.cold_drink_tax = StringVar()

             
            #======= Customer ========

            self.cname = StringVar()
            self.cphone = StringVar()
            self.bill_no = StringVar()
            sano = random.randint(1000,9999)
            self.bill_no.set(str(sano))
            self.search = StringVar()
           
           
            #========== Customer detail frame ==========
            F1 = LabelFrame(self.root,bd=7,text="Customer Details",font=("times new roman",15,'bold'),fg='blue',bg=bg_color)
            F1.place(x=0,y=80,relwidth=1)

            cname_lbl = Label(F1,text="Customer Name",bg=bg_color,fg='green',font=("times new roman",18,'bold')).grid(row=0,column=0,padx=20,pady=5)
            cname_txt = Entry(F1,textvariable=self.cname,width=13,font=("arial",15,'italic'),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)


            cphn_lbl = Label(F1,text="Mobile Number",bg=bg_color,fg='green',font=("times new roman",18,'bold')).grid(row=0,column=2,padx=20,pady=5)
            cphn_txt = Entry(F1,textvariable=self.cphone,width=13,font=("arial",15,'italic'),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)


            cbill_lbl = Label(F1,text="Bill Number",bg=bg_color,fg='green',font=("times new roman",18,'bold')).grid(row=0,column=4,padx=20,pady=5)
            cbill_txt = Entry(F1,textvariable=self.search,width=13,font=("arial",15,'italic'),bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

       
            bill_btn = Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font='arial 12 bold').grid(row=0,column=6,padx=10,pady=10)

            #========= Cosmetics Frame ======

            F2 = LabelFrame(self.root,bd=7,relief=GROOVE,text="Cosmetics",font=("times new roman",15,'bold'),fg='blue',bg=bg_color)
            F2.place(x=5,y=180,width=305,height=362)

            
            Bath_lbl = Label(F2,text='Bath Soap',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky='w')
            Bath_txt = Entry(F2,textvariable=self.soap,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)


            Face_cream_lbl = Label(F2,text='Face Cream',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky='w')
            Face_cream_txt = Entry(F2,textvariable=self.cream,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)


            Face_wash_lbl = Label(F2,text='Face Wash',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky='w')
            Face_wash_txt = Entry(F2,textvariable=self.wash,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
            
            Hair_s_lbl = Label(F2,text='Hair Spray',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky='w')
            Hair_s_txt = Entry(F2,textvariable=self.spray,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

            Hair_g_lbl = Label(F2,text='Hair Gell',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky='w')
            Hair_g_txt = Entry(F2,textvariable=self.gell,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

            Body_lbl = Label(F2,text='Body Loshan',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky='w')
            Body_txt = Entry(F2,textvariable=self.loshan,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

            #========= Grocery Frame ======

            F3 = LabelFrame(self.root,bd=7,relief=GROOVE,text="Grocery",font=("times new roman",15,'bold'),fg='blue',bg=bg_color)
            F3.place(x=310,y=180,width=305,height=362)

            
            g1_lbl = Label(F3,text='Rice',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky='w')
            g1_txt = Entry(F3,textvariable=self.rice,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)


            g2_lbl = Label(F3,text='Food Oil',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky='w')
            g2_txt = Entry(F3,textvariable=self.oil,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

            
            g3_lbl = Label(F3,text='Daal',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky='w')
            g3_txt = Entry(F3,textvariable=self.daal,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

            g4_lbl = Label(F3,text='Wheat',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky='w')
            g4_txt = Entry(F3,textvariable=self.wheat,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

            g5_lbl = Label(F3,text='Sugar',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky='w')
            g5_txt = Entry(F3,textvariable=self.sugar,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)


            g6_lbl = Label(F3,text='Tea',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky='w')
            g6_txt = Entry(F3,textvariable=self.tea,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

            #========= Cold Drink Frame ======

            F4 = LabelFrame(self.root,bd=7,relief=GROOVE,text="Cold Drink",font=("times new roman",15,'bold'),fg='blue',bg=bg_color)
            F4.place(x=615,y=180,width=305,height=362)

            
            c1_lbl = Label(F4,text='Limca',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky='w')
            c1_txt = Entry(F4,textvariable=self.limca,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)


            c2_lbl = Label(F4,text='Maza',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky='w')
            c2_txt = Entry(F4,textvariable=self.maza,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

            
            c3_lbl = Label(F4,text='Cocka Cola',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky='w')
            c3_txt = Entry(F4,textvariable=self.cocka,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

            c4_lbl = Label(F4,text='Frooti',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky='w')
            c4_txt = Entry(F4,textvariable=self.frooti,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

            c5_lbl = Label(F4,text='Thumbs-Up',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky='w')
            c5_txt = Entry(F4,textvariable=self.thumbsup,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

            c6_lbl = Label(F4,text='Sprite',font=("times new roman",15,'bold'),fg='chocolate',bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky='w')
            c6_txt = Entry(F4,textvariable=self.sprite,width=10,font=("times new roman",16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

            #====== Bill Area ======
            F5 = Frame(self.root,bd=10,relief=GROOVE)
            F5.place(x=923,y=180,width=352,height=362)
            bill_title = Label(F5,text='-- Bill Area --',font=('arial 15 italic'),bg='indigo',fg='white',bd=7,relief=GROOVE).pack(fill=X)
            scrol_y = Scrollbar(F5,orient=VERTICAL)
            self.txtarea = Text(F5,yscrollcommand = scrol_y.set,bg='lightgreen',fg='Black')     
            scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=self.txtarea.yview)
            self.txtarea.pack(fill=BOTH,expand=1)

            #====== Bill Menu ================
             
              
            F6 = LabelFrame(self.root,bd=7,relief=GROOVE,text="Bill Menu",font=("times new roman",15,'bold'),fg='blue',bg=bg_color)
            F6.place(x=0,y=538,relwidth=1,height=125)

            m1_lbl = Label(F6,text='Total Cosmetics Price',font=("times new roman",14,'bold'),fg='chocolate',bg=bg_color).grid(row=0,column=0,padx=20,pady=1,sticky='w')
            m1_txt = Entry(F6,textvariable=self.cosmetic,width=10,font=("times new roman",13,'bold'),bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

            m2_lbl = Label(F6,text='Total Grocery Price',font=("times new roman",14,'bold'),fg='chocolate',bg=bg_color).grid(row=1,column=0,padx=20,pady=1,sticky='w')
            m2_txt = Entry(F6,textvariable=self.grocery,width=10,font=("times new roman",13,'bold'),bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

            m3_lbl = Label(F6,text='Total Cold Drink Price',font=("times new roman",14,'bold'),fg='chocolate',bg=bg_color).grid(row=2,column=0,padx=20,pady=1,sticky='w')
            m3_txt = Entry(F6,textvariable=self.cold_drink,width=10,font=("times new roman",13,'bold'),bd=2,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
 
            t1_lbl = Label(F6,text='Cosmetics Tax',font=("times new roman",14,'bold'),fg='chocolate',bg=bg_color).grid(row=0,column=2,padx=20,pady=1,sticky='w')
            t1_txt = Entry(F6,textvariable=self.cosmetic_tax,width=10,font=("times new roman",13,'bold'),bd=2,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

            t2_lbl = Label(F6,text='Grocery Tax',font=("times new roman",14,'bold'),fg='chocolate',bg=bg_color).grid(row=1,column=2,padx=20,pady=1,sticky='w')
            t2_txt = Entry(F6,textvariable=self.grocery_tax,width=10,font=("times new roman",13,'bold'),bd=2,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

            t3_lbl = Label(F6,text='Cold Drink Tax',font=("times new roman",14,'bold'),fg='chocolate',bg=bg_color).grid(row=2,column=2,padx=20,pady=1,sticky='w')
            t3_txt = Entry(F6,textvariable=self.cold_drink_tax,width=10,font=("times new roman",13,'bold'),bd=2,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

            #=== Button frame = ====

            btn_f = Frame(F6,bd=7,relief=GROOVE)
            btn_f.place(x=640,width=620,height=95)

            total_btn = Button(btn_f,command=self.total,text='Total',bg='cadetblue',width=11,bd=5,fg='white',pady=15,font=("times new roman",13,'bold')).grid(row=0,column=0,padx=25,pady=5)
            gbill_btn = Button(btn_f,command=self.bill_area,text='Generate Bill',bg='cadetblue',width=11,bd=5,fg='white',pady=15,font=("times new roman",13,'bold')).grid(row=0,column=1,padx=5,pady=5)
            clear_btn = Button(btn_f,command=self.clear_data,text='Clear',bg='cadetblue',width=11,bd=5,fg='white',pady=15,font=("times new roman",13,'bold')).grid(row=0,column=2,padx=5,pady=5)
            exit_btn = Button(btn_f,command=self.exit_app,text='Exit',bg='cadetblue',width=11,bd=5,fg='white',pady=15,font=("times new roman",13,'bold')).grid(row=0,column=3,padx=5,pady=5)

        def total(self):
            self.cs = (self.soap.get()*40)
            self.cc = (self.cream.get()*120)
            self.cw = (self.wash.get()*60)
            self.csp = (self.spray.get()*180) 
            self.cg = (self.gell.get()*140) 
            self.cl = (self.loshan.get()*160) 
            self.total_cosmetic = float(
                                        self.cs +
                                        self.cc +
                                        self.cw +
                                        self.csp +
                                        self.cg +
                                        self.cl
                                  )
            self.cosmetic.set(str(self.total_cosmetic) + "  Rs.")
            self.ctax = round((self.total_cosmetic*0.05),2)
            self.cosmetic_tax.set("Tax=" + str(self.ctax)+ "Rs.")


            self.gr = (self.rice.get()*40)
            self.go = (self.oil.get()*120)
            self.gd = (self.daal.get()*60)
            self.gw = (self.wheat.get()*180)
            self.gs = (self.sugar.get()*140)
            self.gt = (self.tea.get()*160) 
            self.total_grocery = float(
                                        self.gr +
                                        self.go +
                                        self.gd +
                                        self.gw +
                                        self.gs +
                                        self.gt
                                  )
            self.grocery.set(str(self.total_grocery) + "  Rs.")
            self.gtax = round((self.total_grocery*0.1),2)
            self.grocery_tax.set("Tax=" + str(self.gtax)+ "Rs.")



            self.cdm = (self.maza.get()*40)
            self.cdc = (self.cocka.get()*120)
            self.cdf = (self.frooti.get()*60)
            self.cdt = (self.thumbsup.get()*180)
            self.cdl = (self.limca.get()*140)
            self.cds = (self.sprite.get()*160)
            self.total_cold_drink = float(
                                        self.cdm +
                                        self.cdc +
                                        self.cdf +
                                        self.cdt +
                                        self.cdl +
                                        self.cds 
                                  )
            self.cold_drink.set(str(self.total_cold_drink) + "  Rs.")
            self.cdtax = round((self.total_cold_drink*0.04),2)
            self.cold_drink_tax.set("Tax=" + str(self.cdtax)+ "Rs.")

            self.Total_bill = float (
                                        self.total_cosmetic +
                                        self.total_grocery + 
                                        self.total_cold_drink +
                                        self.ctax +
                                        self.gtax +
                                        self.cdtax
                                    )

        def welcome_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,'       Welcome In Shooping Mall...\n')
            self.txtarea.insert(END,f"     _______________________________\n")
            self.txtarea.insert(END,f"\n\t Bill Number : {self.bill_no.get()}")
            self.txtarea.insert(END,f"\n\t Customer Name : {self.cname.get()}")
            self.txtarea.insert(END,f"\n\t Mobile Number : {self.cphone.get()}")
            self.txtarea.insert(END,f"\n\n *************************************\n")
            self.txtarea.insert(END,f"    Products  \t Quantity \t Price ")
            self.txtarea.insert(END,f"\n *************************************\n")
            

        
        def bill_area(self):

            if self.cname.get() =="" or self.cphone.get()=="" :
                messagebox.showerror("Problem","Customer Details Are Must...")
            
            elif self.cosmetic.get() == "0.0  Rs." and self.grocery.get() == "0.0  Rs." and self.cold_drink.get() == "0.0  Rs." :
                messagebox.showerror("Problem","There is no  Product selected..! Please select the required Products...")

            
            else :

                self.welcome_bill()

                #============ Cosmetics ========================
                if self.soap.get() !=0:
                    self.txtarea.insert(END,f"\n   Bath Soap      \t {self.soap.get()}     \t {self.cs}")
                if self.cream.get() !=0:
                    self.txtarea.insert(END,f"\n   Face Cream     \t {self.cream.get()}     \t {self.cc}")
                if self.wash.get() !=0:
                    self.txtarea.insert(END,f"\n   Face Wash      \t {self.wash.get()}     \t {self.cw}")
                if self.spray.get() !=0:
                    self.txtarea.insert(END,f"\n   Hair Spray     \t {self.spray.get()}     \t {self.csp}")
                if self.gell.get() !=0:
                    self.txtarea.insert(END,f"\n   Hair Gell      \t {self.gell.get()}     \t {self.cg}")
                if self.loshan.get() !=0:
                    self.txtarea.insert(END,f"\n   Body Loshan    \t {self.loshan.get()}     \t {self.cl}")


                #============ Grocery ========================
                if self.rice.get() !=0:
                    self.txtarea.insert(END,f"\n   Rice           \t {self.rice.get()}     \t {self.gr}")
                if self.oil.get() !=0:
                    self.txtarea.insert(END,f"\n   Food Oil       \t {self.oil.get()}     \t {self.go}")
                if self.daal.get() !=0:
                    self.txtarea.insert(END,f"\n   Daal           \t {self.daal.get()}     \t {self.gd}")
                if self.wheat.get() !=0:
                    self.txtarea.insert(END,f"\n   Wheat          \t {self.wheat.get()}     \t {self.gw}")
                if self.sugar.get() !=0:
                    self.txtarea.insert(END,f"\n   Sugar          \t {self.sugar.get()}     \t {self.gs}")
                if self.tea.get() !=0:
                    self.txtarea.insert(END,f"\n   Tea            \t {self.tea.get()}     \t {self.gt}")


                

                #============ Cold Drinks ========================
                if self.limca.get() !=0:
                    self.txtarea.insert(END,f"\n   Limca          \t {self.limca.get()}     \t {self.cdl}")
                if self.maza.get() !=0:
                    self.txtarea.insert(END,f"\n   Maza           \t {self.maza.get()}     \t {self.cdm}")
                if self.cocka.get() !=0:
                    self.txtarea.insert(END,f"\n   Cocka Cola     \t {self.cocka.get()}     \t {self.cdc}")
                if self.frooti.get() !=0:
                    self.txtarea.insert(END,f"\n   Frooti         \t {self.frooti.get()}     \t {self.cdf}")
                if self.thumbsup.get() !=0:
                    self.txtarea.insert(END,f"\n   Thumbs-Up      \t {self.thumbsup.get()}     \t {self.cdt}")
                if self.sprite.get() !=0:
                    self.txtarea.insert(END,f"\n   Sprite         \t {self.sprite.get()}     \t {self.cds}")


                #============ Taxes Setion ========================

                self.txtarea.insert(END,f"\n\n *************************************")
                
                if self.cosmetic_tax.get() !="Tax=0.0Rs.":
                    self.txtarea.insert(END,f"\n\n   Cosmetic's Tax     \t\t {self.cosmetic_tax.get()}")
                
                if self.grocery_tax.get() !="Tax=0.0Rs.":
                    self.txtarea.insert(END,f"\n   Grocery's Tax      \t\t {self.grocery_tax.get()}")
            
                if self.cold_drink_tax.get() !="Tax=0.0Rs.":
                    self.txtarea.insert(END,f"\n   Cold Drink's Tax   \t\t {self.cold_drink_tax.get()}")
                
                self.txtarea.insert(END,f"\n\n\n *************************************\n")
                self.txtarea.insert(END,f"    Total Bill = \t\t    Rs: {str(self.Total_bill)}")
                self.txtarea.insert(END,f"\n *************************************\n")

                self.save_bill()
                        
        def save_bill(self):
            shaibaz = messagebox.askyesno("Save Bill","Do you want to save bill ?")
            if shaibaz > 0:
                self.bill_data = self.txtarea.get("1.0",END)
                f1 = open("Bills/" + str(self.bill_no.get()) +"_"+self.cname.get()+ ".txt","w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved",f"Bill No : {self.bill_no.get()}_{self.cname.get()}  Saved SuccessFully...")
            else:
                return

        def find_bill(self):
            present = "no"
            for i in os.listdir("Bills/"):
                if i.split('.')[0] == self.search.get():
                    f1 = open(f"Bills/{i}","r")
                    self.txtarea.delete('1.0',END)
                    for d in f1:
                        self.txtarea.insert(END,d)
                    f1.close()
                    present = "yes"
                
            if present == "no":
                    messagebox.showerror("Problem","You Have Entered Invalid Bill Number...")
            
        def clear_data(self):
            shaibaz = messagebox.askyesno("Clear Bill","Do you want to clear bill ?")
            if shaibaz > 0:

                    #======= Cosmetics ========
                self.soap.set(0)
                self.cream.set(0)
                self.wash.set(0)
                self.spray.set(0)
                self.gell.set(0)
                self.loshan.set(0)

                #======= Grocery ========

                self.rice.set(0)
                self.oil.set(0)
                self.daal.set(0)
                self.wheat.set(0)
                self.sugar.set(0)
                self.tea.set(0)
    
    
                #======= Cold Drinks ========

                self.maza.set(0)
                self.cocka.set(0)
                self.frooti.set(0)
                self.thumbsup.set(0)
                self.limca.set(0)
                self.sprite.set(0)

                
                #======= Total Products and Tax Variabels ========

                self.cosmetic.set("")
                self.grocery.set("")
                self.cold_drink.set("")           
            
                self.cosmetic_tax.set("")
                self.grocery_tax.set("")
                self.cold_drink_tax.set("")

                
                #======= Customer ========

                self.cname.set("")
                self.cphone.set("")
                self.bill_no.set("")
                sano = random.randint(1000,9999)
                self.bill_no.set(str(sano))
                self.search.set("")


                self.welcome_bill()
        
        def exit_app(self):
            sano = messagebox.askyesno("Exit","Do you want to Exit this Application... ?")
            if sano > 0:
                self.root.destroy()

root = Tk()
sano = Bill_App(root)
root.mainloop()
