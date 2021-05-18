from tkinter import*
import pandas as pd
import random
import os
import time;
import csv
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox
# create the main window
root=Tk()

root.geometry("950x700+50+10")
root.title("BUSINESS_PLAN SIMULATOR BY Jackmangichui@gmail.com")
#root.resizable(width=0,height=0)
root.configure(bg="#ccffeb")
data_base="index.csv"
personal=20000
menu="content1.txt"
try:
    with open(menu,"w") as k:
        k.write("\t")
except:
    with open(menu,"a+") as k:
        k.write("\t")
def total_s(x1,x2):
    x2=x2-1
    return x2*x1
def simulation():
    global bs_name
    #
    try:
        with open(menu,"w") as k:
            k.write("\t")
    except:
        with open(menu,"a+") as k:
            k.write("\t")
        k.close()
    
    #getting all the data at a series
    income1=sum_data(data_base,bs_name,"income")
    expens1=sum_data(data_base,bs_name,"exp")
    asset1=sum_data(data_base,bs_name,"nce")
    depl_asset=sum_dep(data_base,bs_name,"nce")
    loan=sum_dep0(data_base,bs_name,"finance")
    intrest_loan=sum_dep1(data_base,bs_name,"finance")

    
    ###print(loan,intrest_loan,income1,expens1,depl_asset)
    ###print("ass",asset1,depl_asset)
    total_income=0
    total_bstax=0
    total_intax=0
    total_loan=0
    total_expens=0
    total_deple=0
    total_maintain=0
    total_tax1=0
    total_tax2=0
    total_div1=0
    total_div2=0

    
    total_ass=0
    total_retain=0
    total_div=0
    total_tax=0
    total_finance=0
    total_dep=0
    totalpp=0
    rest=0
    maintainace=0
    cash_back=0
    count1=1
    x6=depl_asset
    ###print("nnnnn",asset1/x6,x6,asset1)
    x5=asset1
    x55=x5#asset value that will change dynamically
    deep=x6
    try:
        r1=income1/(loan+intrest_loan+expens1)
        r2=1-(x5/x6)# asset depretion to asset
    except:
        r1=0
        r2=0
    ###print("the rate of profit is",r1,(loan+intrest_loan+expens1+depl_asset))
    
    #total_ff1=sum_dep2(data_base,bs_name,"finance")
    #gettin if the r1 is more than one
    if(r1<1):
        pr=("the project is operating at a loss of the rate: "+str(round(1-r1,2))+"\n")
        with open(menu,"a+") as k:
            k.write(pr)
        k.close()
    else:
        #get the values of every data required and then simulate through ie the profit dipresiation and many others
        while(cash_back<=2*x5):
            asset_now=r2*x55# the acuatul value t
            
            tt1="\n\t*****************************************PERIOD:"+str(count1)+"*********************************\n\t\t===========financial cash flow ===============================\n"
            tt2="\t\t"+"name\t\t inflow\t\t outflow\n"
            
            with open(menu,"a+") as k:
                k.write(tt1+tt2)
            k.close()
            sum_now=sum_intrest_loan(data_base,bs_name,"finance",count1)#total amount of loans and intrest
            dif=income1-sum_now-expens1 #total profit the busness generate without taxes
            dif1=cash_back *r1# the amount the generated from the profit of the bussiness x the rate of return
            ###print("the profit withou taxes",dif1)
            
            #defining the tax
            ##print(dif,round(0.01*x55,2),x55)
            if(dif<=asset_now):
                tax=.1*dif
                
                divided1=.05*dif
                maintan=.05*dif
                reinvest=.3*dif
                deple=.5*dif
                tax2=.02*dif1#tax due to investment
                #total taxes
                tot_cash=.97*dif1
                tot1=cash_back
                divided2=.01*dif1
                x55=x55-deple
                ##print("payable loan",sum_now)
                ###print("check",(divided1+maintan+reinvest+deple+tax+sum_now+expens1))
                ###print(divided1,maintan,reinvest,deple,tax,sum_now,expens1)
                
                ###print("asset now",round(x55,2),round(cash_back,2),round(tot_cash,2),round(tax2,2),str(count1))
                cash_back=reinvest+tot_cash
                
                total_income=total_income+income1
                total_bstax=total_bstax+tax
                total_intax=total_intax+tax2
                total_expens=total_expens+expens1
                total_loan=total_loan+sum_now
                total_deple=total_deple+deple
                total_maintain=total_maintain+maintan
                total_div1=total_div1+divided1
                total_div2=total_div2+divided2
                #total_loan=total_loan+sum_now
                ##print("payable loan now",total_loan-sum_now)
                
                total_retain=total_retain+reinvest
                ###print(divided1,maintan,reinvest,deple,tax,sum_now,expens1)
                ###print(total_income,total_div1,total_maintain,total_retain,total_deple,total_bstax,total_loan,total_expens)
                ###print(income1,(total_retain+total_bstax+total_expens+total_loan+total_deple+total_div1,2))
                
                
                tt1="\n\t\t===========investment cashflow for =========="+"\n"
                tt2="\t\t"+"  name\t\t inflow\t\t outflow\n"
                ttt3="\t\tre_investment\t\t"+str(round(tot1,2))+"\t\t\n"
                ttt4="\t\tbus divided\t\t\t\t"+str(round(divided1,2))+"\n"
                ttt4="\t\tinvestment divided\t\t\t\t"+str(round(divided2,2))+"\n"
                tt5="\n\t\t===========operational cashflow for period==:"+"\n"
                tt6=" \t\tname\t\t inflow\t\t outflow\n"
                ttt7="\t\tincome\t\t"+str(round(income1,2))+"\t\t\n"
                ttt8="\t\texpenses\t\t\t\t"+str(round(expens1,2))+"\n"
                ttt9="\t\tasset repayment\t\t\t\t"+str(round(deple,2))+"\n"
                ttt10="\t\tmaintainance\t\t\t\t"+str(round(maintan,2))+"\n"
                ttt11="\t\tbusness tax\t\t\t\t"+str(round(tax,2))+"\n"
                ttt12="\t\tinvestment tax\t\t\t\t"+str(round(tax2,2))+"\n"
                ppp8=str(round(total_deple+total_expens+total_maintain+total_bstax+total_div1+total_retain+total_loan,2))
                
                ##print("here",count1,"done1")
                with open(menu,"a+") as k:
                    k.write(tt1+tt2+ttt3+ttt4+tt5+tt6+ttt7+ttt8+ttt9+ttt10+ttt11+ttt12)
                k.close()
            else:
                
                ####print("here",dif)
                deple1=r2*x55
                if(deple1<dif):
                    ###print("the total deplitable is",deple,dif,x55,r2)
                    deple=dif*.1
                    tax=.2*dif
                
                
                    divided1=.2*dif
                    maintan=.2*dif
                    reinvest=.3*dif
                
                    tax2=.02*dif1#tax due to investment
                
                    tot_cash=.97*dif1
                    tot1=cash_back
                    divided2=.01*dif1
                    ###print("asset now",round(deep,2),round(cash_back,2),round(tot_cash,2),round(tax2,2))
                    cash_back=reinvest+tot_cash
                    x55=x55-deple

                    
                    total_income=total_income+income1
                    total_bstax=total_bstax+tax
                    total_intax=total_intax+tax2
                    total_expens=total_expens+expens1
                    total_loan=total_loan+sum_now
                    total_deple=total_deple+deple
                    total_maintain=total_maintain+maintan
                    total_div1=total_div1+divided1
                    total_div2=total_div2+divided2
                    

                    total_retain=total_retain+reinvest
                    ##print("payable loan now2",total_loan-sum_now)
                    
                
                    tt1="\n\t\t===========investment cashflow for==========="+"\n"
                    tt2=" \t\t name\t\t inflow\t\t outflow\n"
                    ttt3="\t\tre_investment\t\t"+str(round(tot1,2))+"\t\t\n"
                    ttt4="\t\tbus divided\t\t\t\t"+str(round(divided1,2))+"\n"
                    ttt4="\t\tinvestment divided\t\t\t\t"+str(round(divided2,2))+"\n"
                    tt5="\n\t\t===========operational cashflow for period==:"+"\n"
                    tt6="\t\t name\t\t inflow\t\t outflow\n"
                    ttt7="\t\tincome\t\t"+str(round(income1,2))+"\t\t\n"
                    ttt8="\t\texpenses\t\t\t\t"+str(round(expens1,2))+"\n"
                    ttt9="\t\tasset repayment\t\t\t\t"+str(round(deple,2))+"\n"
                    ttt10="\t\tmaintainance\t\t\t\t"+str(round(maintan,2))+"\n"
                    ttt11="\t\tbusness tax\t\t\t\t"+str(round(tax,2))+"\n"
                    ttt12="\t\tinvestment tax\t\t\t\t"+str(round(tax2,2))+"\n"
                    ##print("here",count1,"done2")
                
            
                    with open(menu,"a+") as k:
                        k.write(tt1+tt2+ttt3+ttt4+tt5+tt6+ttt7+ttt8+ttt9+ttt10+ttt11+ttt12)
                    k.close()
                else:
                    ####print("profit less than the rate of dip")
                    dif=dif-deple
                    ###print(count1,dif)
                    tax=.2*dif
                
                
                    divided1=.2*dif
                    maintan=.3*dif
                    reinvest=.3*dif
                
                    tax2=.02*dif1#tax due to investment
                
                    tot_cash=.97*dif1
                    tot1=cash_back
                    divided2=.01*dif1
                    
                    cash_back=reinvest+tot_cash
                    x55=x55-deple
                    total_income=total_income+income1
                    total_bstax=total_bstax+tax
                    total_intax=total_intax+tax2
                    total_expens=total_expens+expens1
                    total_loan=total_loan+sum_now
                    total_deple=total_deple+deple
                    total_maintain=total_maintain+maintan
                    total_div1=total_div1+divided1
                    total_div2=total_div2+divided2
                    
                
                
                    total_retain=total_retain+reinvest
                    
                    
                
                    tt1="\n\t\t===========investment cashflow for period==:"+"\n"
                    tt2=" \t\t name\t\t inflow\t\t outflow\n"
                    ttt3="\t\tre_investment\t\t"+str(round(tot1,2))+"\t\t\n"
                    ttt4="\t\tbus divided\t\t\t\t"+str(round(divided1,2))+"\n"
                    ttt4="\t\tinvestment divided\t\t\t\t"+str(round(divided2,2))+"\n"
                    tt5="\n\t\t===========operational cashflow for period==:"+"\n"
                    tt6="\t\t name\t\t inflow\t\t outflow\n"
                    ttt7="\t\tincome\t\t"+str(round(income1,2))+"\t\t\n"
                    ttt8="\t\texpenses\t\t\t\t"+str(round(expens1,2))+"\n"
                    ttt9="\t\tasset repayment\t\t\t\t"+str(round(deple,2))+"\n"
                    ttt10="\t\tmaintainance\t\t\t\t"+str(round(maintan,2))+"\n"
                    ttt11="\t\tbusness tax\t\t\t\t"+str(round(tax,2))+"\n"
                    ttt12="\t\tinvestment tax\t\t\t\t"+str(round(tax2,2))+"\n"
                    ###print("here",count1,"done3")
                
            
                    with open(menu,"a+") as k:
                        k.write(tt1+tt2+ttt3+ttt4+tt5+tt6+ttt7+ttt8+ttt9+ttt10+ttt11+ttt12)
                    k.close()
                    
            
            
        
            ###print(count1,x55,cash_back,tax,tax2)
            count1=count1+1
        total_income1=total_s(income1,count1)
        total_expens1=total_s(expens1,count1)
        
        #total_depleno=total_s(total_deplen,count1)
        
        ###print(total_income1,total_income,total_expens1,total_expens,total_deple)
        pp0="\t\t ==========BUSINESS SUMARY VIEW===\n\t\tTotal income earned:\t"+str(round(total_income,2))+"\n"
        pp1="\t\tTotal used for expenses:\t"+str(round(total_expens,2))+"\n"
        pp2="\t\tTotal saved for machine depletiation:\t"+str(round(total_deple,2))+"\t\t machinery value now\t"+str(round(x55,2))+"\n"
        pp3="\t\tTotal used for maintanance:\t"+str(round(total_maintain,2))+"\n"
        pp4="\t\tTotal paid as Firm tax:\t"+str(round(total_bstax,2))+"\n"
        pp5="\t\tTotal paid as investment tax:\t"+str(round(total_intax,2))+"\n"
        pp6="\t\tTotal paid as firm divided:\t"+str(round(total_div1,2))+"\n"
        pp7="\t\tTotal paid as investment divided:\t"+str(round(total_div2,2))+"\n"
        pp9="\t\tTotal paid for loan:\t"+str(round(total_loan,2))+"\n"
        pp10="\t\tTotal reinvested money from the firm:\t"+str(round(total_retain,2))+"\n"
        pp11="\t\tTotal cash out  money from the investment:\t"+str(round(cash_back,2))+"\n"
        ###print(income1,round(divided11+maintan1+deple1+tax1+expens11+sum_now+reinvest,2))
        pp8=str(round((total_income+total_div1+total_maintain+total_retain+total_deple+total_bstax+total_loan+total_expens)/2,2))
        ###print("here2",total_income,total_div1,total_maintain,total_retain,total_deple,total_bstax,total_loan,total_expens)
        
        with open(menu,"a+") as k:
            k.write(pp0+pp1+pp2+pp3+pp4+pp5+pp6+pp7+pp9+pp10+pp11)

        k.close()
    a1=StringVar()
    n1=StringVar()
    r1=StringVar()

    reset_frame()
    #create the two frames
    
    f1=Frame(root,width=1000,height=100,bg="#b0a94f",relief=RAISED)
    f1.pack(pady=1)
    f2=Frame(root,width=900,height=500,bg="lime",relief=RAISED)
    f2.pack(pady=1)
    #valiables
    def exit11():
        for wid in root.winfo_children():
            wid.destroy()
        bs1_name()
    def reset_frame2():
        for wid in f2.winfo_children():
            wid.destroy()
        
    def reset_fields():
        a1.set("")
        n1.set("")
        r1.set("")
    def add_data():
        #getting the data entered so we have to  check if the data is empty
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="exp")&(df["project_name"]== bs_name)]
        got=(len(frame1))
        code=got+1
        name2=name1.get()
        rate2=0
        amount2=amount1.get()
        #####print(amount2)
        try:
            
            
            amount3=float(amount2)
            #####print(name2,amount2)
        
            frame3=frame1.loc[(frame1["description"]==name2)&(frame1["amount"]==amount3)]
            if(len(frame3)<1):
                
        
                if((name2!="")&(amount3>0)):
                    with open(data_base,"a+") as k:
                        k.write(str(bs_name))
                        k.write(",")
                        k.write(str("exp"))
                        k.write(",")
                        k.write(str(code))
                        k.write(",")
                        k.write(str(name2))
                        k.write(",")
                        k.write(str(amount2))
                        k.write(",")
                        k.write(str(rate2))
                        k.write("\n")
            
                    k.close()
                reset_frame2()
                preview()
                reset_fields()
            else:
                reset_frame2()
                preview()
                reset_fields()
        except:
            messagebox.showinfo("Wrong Data formart","the data you entered in not correct  check ")
            reset_fields()
            
    def preview():
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["project_name"]== bs_name)]
        got=(len(frame1))
        
        mm="content.txt"
        #open the file to write on it
        with open(mm,"w") as m:
            
            for i in range(got):
                name1=frame1.iloc[i,0]
                type1=frame1.iloc[i,1]
                code1=frame1.iloc[i,2]
                desc1=frame1.iloc[i,3]
                amount1=frame1.iloc[i,4]
                rate1=frame1.iloc[i,5]
                m.write(str(name1))
                m.write("\t")
                m.write(str(type1))
                m.write("\t")
                m.write(str(code1))
                m.write("\t")
                m.write(str(desc1)) 
                m.write("\t\t")
                m.write(str(amount1))
                m.write("\t")
                m.write(str(rate1))
                m.write("\t")
                m.write("\n")
        m.close()
        scroll1 = Scrollbar(f2)
        scroll1.pack(side=RIGHT,fill=Y)
        text = Text(f2, font=('bold',8),height=30, width=145,fg="#000000",bg="#DCDCDC",yscrollcommand=scroll1.set)
        
    
        with open(menu) as j:
            data1=j.readlines()
            for row in data1:
                text.insert(END,row)

        j.close()
        text.pack()
        scroll1.config(command=text.yview)

    

    

    name1=StringVar()
    rate1=StringVar()
    amount1=StringVar()
    rate1.set(0)
    lab=Label(f1,font="12",text="The summary of  "+bs_name+"  business plan simulation",fg="green")
    lab.grid(row=1,column=0,columnspan=3,pady=1,padx=1,ipadx=10,ipady=11)
    b2=Button(f1,text="EXIT",bg="#8B0000",fg="white",command=exit1)
    b2.grid(row=0,column=3,columnspan=2,ipady=10,ipadx=10,pady=1,padx=20)
    b21=Button(f1,text="Home",bg="#8A2BE2",fg="white",command=exit11)
    b21.grid(row=2,column=3,columnspan=2,ipady=10,ipadx=10,pady=1,padx=20)
    #lab1=Label(f1,text="name",fg="red")
    #lab1.grid(row=2,column=0,padx=5)
    ##lab1=Label(f1,text="Rate%",fg="red")
    #lab1.grid(row=2,column=1,padx=20)
    #lab1=Label(f1,text="Amount",fg="red")
    #lab1.grid(row=2,column=2,padx=20)
    #name1=Entry(f1,textvariable=n1)
    #name1.grid(row=3,column=0,pady=10,padx=10)
    #name1.focus_set()
    #rate1=Entry(f1)
    #rate1.grid(row=3,column=1,pady=10,padx=10)
    #amount1=Entry(f1,textvariable=a1)
    #amount1.grid(row=3,column=2,pady=10,padx=10)
    b3=Button(f1,text="back",bg="black",fg="white",command=income_fn)
    b3.grid(row=4,column=0,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    #b4=Button(f1,text="send to database",bg="#8B0000",fg="white",command=add_data)
    #b4.grid(row=4,column=1,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    #b5=Button(f1,text="NEXT",bg="orange",fg="white",command=financing)
    #b5.grid(row=4,column=3,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    preview()
    
    # here we want to  get the required data to make the cashflow fot
    #operation
    #finance
    #investiment

    #******************operations**********************

def sum_intrest_loan(x,x2,x3,c):
    global bs_name
    data_base=pd.read_csv(x)
    data=data_base.loc[(data_base["project_name"]==x2)&(data_base["category"]==x3)]
    sum1=0
    l1=len(data)
    
    for i in range(l1):
        name_1=data.iloc[i,3]
        k=data.iloc[i,4]
        kk=data.iloc[i,5]
        kk3=data.iloc[i,6]
        ####print("i",i)
        if((c==1)):
            quatum=k/kk3
            
            prod=(kk*quatum)
            sum1=sum1+prod+quatum
            ###print(sum1,kk3)
            
            tr="\t\t"+str(name_1)+"\t"
            tr1="\t"+str(round(quatum,2))+"\t"
            tr3="\t"+str(round(prod+quatum,2))+"\n"
            
            
            with open(menu,"a+") as k:
                k.write(tr+tr1+tr3)
            k.close()
            #
        else:
            ####print("not over here")
            if((kk3>1)&(kk3>=c)):
                quatum=k/kk3
            
                prod=(kk*quatum)
                sum1=sum1+prod+quatum
                ###print("here on",c,name_1)
               
                tr="\t\t"+str(name_1)+"\t"
                tr1="\t"+str(round(quatum,2))+"\t"
                tr3="\t"+str(round(prod+quatum,2))+"\n"
            
            
                with open(menu,"a+") as k:
                    k.write(tr+tr1+tr3)
                k.close()
                if(kk3==c):
                    tr=str(name_1)+"\t\t"
                    tr1="\t\t"+"loan has been completed\n"
                    
                    with open(menu,"a+") as k:
                        k.write(tr+tr1)
                    k.close()
                    
                    
            elif(kk3==1):
                quatum=k/kk3
            
                prod=(kk*quatum)
                sum1=sum1+prod+quatum
                
                tr="\t\t"+str(name_1)+"\t"
                tr1="\t"+str(round(quatum,2))+"\t"
                tr3="\t"+str(round(prod+quatum,2))+"\n"
            
            
                with open(menu,"a+") as k:
                    k.write(tr+tr1+tr3)
                k.close()
            else:
                sum1=sum1
                prod=0
                quatum=0
                
                tr="\t\t"+str(name_1)+"\t"
                tr1="\t"+str(round(quatum,2))+"\t"
                tr3="\t"+str(round(prod,2))+"\n"
                
                
            
                with open(menu,"a+") as k:
                    k.write(tr+tr1+tr3)
                k.close()
                
    ###print("sum for period",c,sum1)
    c=c+1
    
    return sum1
    
    
def sum_dep1(x,x2,x3):
    global bs_name
    data_base=pd.read_csv(x)
    data=data_base.loc[(data_base["project_name"]==x2)&(data_base["category"]==x3)]
    sum1=0
    l1=len(data)
    for i in range(l1):
        k=data.iloc[i,4]
        kk=data.iloc[i,5]
        kk3=data.iloc[i,6]
        quatum=k/kk3
        k_rate=quatum*kk
        prod=(k*kk/kk3)
        sum1=sum1+prod
        
    return sum1
        
    
def sum_dep0(x,x2,x3):
    global bs_name
    data_base=pd.read_csv(x)
    data=data_base.loc[(data_base["project_name"]==x2)&(data_base["category"]==x3)]
    sum1=0
    l1=len(data)
    for i in range(l1):
        k=data.iloc[i,4]
        
        kk=data.iloc[i,5]
        kk3=data.iloc[i,6]
        prod=float(k)/float(kk3)
        sum1=sum1+prod
    return sum1  
    
    
def sum_dep(x,x2,x3):
    global bs_name
    data_base=pd.read_csv(x)
    data=data_base.loc[(data_base["project_name"]==x2)&(data_base["category"]==x3)]
    sum1=0
    l1=len(data)
    for i in range(l1):
        k=data.iloc[i,4]
        kk=data.iloc[i,5]
        prod=float(k)*float(kk)
        sum1=sum1+prod+k
    return sum1
    
def sum_data(x,x2,x3):
    global bs_name
    data_base=pd.read_csv(x)
    #geting the  condatyionsa for the data\
    data=data_base.loc[(data_base["project_name"]==x2)&(data_base["category"]==x3)]
    #getting the sum for the column
    nce_sum=data["amount"].sum()
    return nce_sum
    ####print(sum_data(data_base,bs_name,"nce"))


try:
    data=pd.read_csv("index.csv")
    data.describe()
except:
    with open(data_base,"a+") as m:
        m.write("project_name,")
        m.write("category,")
        m.write("code,")
        m.write("description,")
        m.write("amount,")
        m.write("rate,")
        m.write("period\n")
    with open("content.txt","a+") as k:
        k.write("\t")

def exit1():
    root.destroy()

def reset_frame():
    for wid in root.winfo_children():
            wid.destroy()


def current_exp():
    global bs_name
    def delete(x1,x2,x3):
        def get_name1():
            df=pd.read_csv(data_base)
            lst2=lst1.get()
            
            
            #print(lst2)
            if(lst2=="None"):
                x=1
            else:
                dat=df.loc[df[x1]!=lst2]
                pd.DataFrame(dat).to_csv("index.csv",header=True,index=None)
                
                reset_frame()
                current_exp()
                #print(dat)
                
                
                
            
        lab=Label(f1,font="9",text="select the  Entry to delete")
        lab.grid(row=1,column=4,pady=1,padx=1,ipadx=1,ipady=1)
        df=pd.read_csv(data_base)
        df=df.loc[(df["project_name"]==bs_name)&(df["category"]=="exp")]
        frame1=df["description"]
        ls=[]
        if(len(frame1)<1):
            datak=["None"]
        else:
            for i in range(len(frame1)):
                d1=frame1.iloc[i]
                dat=[d1]
                ls=ls+dat
    
            datak=np.unique(ls)
    
    
    
    
        lst1=StringVar()
        lst1.set("None")
        selectI=OptionMenu(f1,lst1,*datak)
        selectI.grid(row=2,column=4)
        b1=Button(f1,text="Delete  ",height=1,width=8,bg="#ff1a1a",fg="white",command=get_name1)
        b1.grid(row=3,column=4 ,columnspan=1,ipady=1,ipadx=1,pady=1,padx=1)
        #delete("description","reset_frame",1)
    a1=StringVar()
    n1=StringVar()
    r1=StringVar()

    reset_frame()
    def sum_tot():
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="exp")&(df["project_name"]== bs_name)]
        tot1=str(frame1["amount"].sum())
        return tot1
    #create the two frames
    
    f1=Frame(root,width=1000,height=100,bg="#b0a94f",relief=RAISED)
    f1.pack(pady=1)
    f2=Frame(root,width=900,height=500,bg="lime",relief=RAISED)
    f2.pack(pady=1)
    delete("description","reset_frame",1)
    #valiables
    def reset_frame2():
        for wid in f2.winfo_children():
            wid.destroy()
        
    def reset_fields():
        a1.set("")
        n1.set("")
        r1.set("")
    def add_data():
        #getting the data entered so we have to  check if the data is empty
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="exp")&(df["project_name"]== bs_name)]
        got=(len(frame1))
        code=got+1
        name2=name1.get()
        rate2=0
        amount2=amount1.get()
        
        #####print(amount2)
        try:
            
            
            amount3=float(amount2)
            #####print(name2,amount2)
        
            frame3=frame1.loc[(frame1["description"]==name2)&(frame1["amount"]==amount3)]
            if(len(frame3)<1):
                
        
                if((name2!="")&(amount3>0)):
                    with open(data_base,"a+") as k:
                        k.write(str(bs_name))
                        k.write(",")
                        k.write(str("exp"))
                        k.write(",")
                        k.write(str(code))
                        k.write(",")
                        k.write(str(name2))
                        k.write(",")
                        k.write(str(amount2))
                        k.write(",")
                        k.write(str(rate2))
                        k.write("\n")
            
                    k.close()
                reset_frame2()
                preview()
                reset_fields()
            else:
                reset_frame2()
                preview()
                reset_fields()
        except:
            messagebox.showinfo("Wrong Data formart","the data you entered in not correct  check ")
            reset_fields()
            
    def preview():
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="exp")&(df["project_name"]== bs_name)]
        got=(len(frame1))
        tot1=sum_tot() 
        mm="content.txt"
        #open the file to write on it
        with open(mm,"w") as m:
            kk="Total amount is  :"+tot1+"\n"
            m.write(kk)
            for i in range(got):
                name1=frame1.iloc[i,0]
                type1=frame1.iloc[i,1]
                code1=frame1.iloc[i,2]
                desc1=frame1.iloc[i,3]
                amount1=frame1.iloc[i,4]
                rate1=frame1.iloc[i,5]
                m.write(str(name1))
                m.write("\t")
                m.write(str(type1))
                m.write("\t")
                m.write(str(code1))
                m.write("\t")
                m.write(str(desc1)) 
                m.write("\t\t")
                m.write(str(amount1))
                m.write("\t")
                m.write(str(rate1))
                m.write("\t")
                m.write("\n")
        m.close()
        scroll1 = Scrollbar(f2)
        scroll1.pack(side=RIGHT,fill=Y)
        text = Text(f2, font=('bold'),height=24, width=145,fg="#000000",bg="#DCDCDC",yscrollcommand=scroll1.set)
        
    
        with open(mm) as j:
            data1=j.readlines()
            for row in data1:
                text.insert(END,row)

        j.close()
        text.pack()
        scroll1.config(command=text.yview)

    

    name1=StringVar()
    rate1=StringVar()
    amount1=StringVar()
    rate1.set(0)
    lab=Label(f1,font="12",text="Enter current expenses for "+bs_name+"  business plan")
    lab.grid(row=1,column=0,columnspan=3,pady=1,padx=1,ipadx=10,ipady=11)
    b2=Button(f1,text="EXIT",bg="#8B0000",fg="white",command=exit1)
    b2.grid(row=0,column=3,columnspan=2,ipady=10,ipadx=10,pady=1,padx=20)
    lab1=Label(f1,text="name",fg="red")
    lab1.grid(row=2,column=0,padx=5)
    #lab1=Label(f1,text="Rate%",fg="red")
    #lab1.grid(row=2,column=1,padx=20)
    lab1=Label(f1,text="Amount",fg="red")
    lab1.grid(row=2,column=2,padx=20)
    name1=Entry(f1,textvariable=n1)
    name1.grid(row=3,column=0,pady=10,padx=10)
    name1.focus_set()
    #rate1=Entry(f1)
    #rate1.grid(row=3,column=1,pady=10,padx=10)
    amount1=Entry(f1,textvariable=a1)
    amount1.grid(row=3,column=2,pady=10,padx=10)
    b3=Button(f1,text="back",bg="black",fg="white",command=non_current_asset)
    b3.grid(row=4,column=0,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    b4=Button(f1,text="send to database",bg="#8B0000",fg="white",command=add_data)
    b4.grid(row=4,column=1,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    b5=Button(f1,text="NEXT",bg="orange",fg="white",command=financing)
    b5.grid(row=4,column=3,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    preview()


def income_fn():
    global bs_name
    def delete(x1,x2,x3):
        def get_name1():
            df=pd.read_csv(data_base)
            lst2=lst1.get()
            
            
            #print(lst2)
            if(lst2=="None"):
                x=1
            else:
                dat=df.loc[df[x1]!=lst2]
                pd.DataFrame(dat).to_csv("index.csv",header=True,index=None)
                
                reset_frame()
                income_fn()
                #print(dat)
                
                
                
            
        lab=Label(f1,font="10",text="select the  Entry to delete")
        lab.grid(row=1,column=4,pady=10,padx=1,ipadx=1,ipady=1)
        df=pd.read_csv(data_base)
        df=df.loc[(df["project_name"]==bs_name)&(df["category"]=="income")]
        frame1=df["description"]
        ls=[]
        if(len(frame1)<1):
            datak=["None"]
        else:
            for i in range(len(frame1)):
                d1=frame1.iloc[i]
                dat=[d1]
                ls=ls+dat
    
            datak=np.unique(ls)
    
    
    
    
        lst1=StringVar()
        lst1.set("None")
        selectI=OptionMenu(f1,lst1,*datak)
        selectI.grid(row=2,column=4)
        b1=Button(f1,text="Delete  ",height=2,width=8,bg="#ff1a1a",fg="white",command=get_name1)
        b1.grid(row=3,column=4 ,columnspan=1,ipady=1,ipadx=1,pady=1,padx=1)
        #delete("description","reset_frame",1)

    a1=StringVar()
    n1=StringVar()
    r1=StringVar()

    reset_frame()
    def sum_tot():
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="income")&(df["project_name"]== bs_name)]
        tot1=str(frame1["amount"].sum())
        return tot1
    #create the two frames
    
    f1=Frame(root,width=1000,height=100,bg="#b0a94f",relief=RAISED)
    f1.pack(pady=1)
    f2=Frame(root,width=900,height=500,bg="lime",relief=RAISED)
    f2.pack(pady=1)
    delete("description","reset_frame",1)
    #valiables
    def reset_frame2():
        for wid in f2.winfo_children():
            wid.destroy()
        
    def reset_fields():
        a1.set("")
        n1.set("")
        r1.set("")
    
    def add_data():
        #getting the data entered so we have to  check if the data is empty
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="income")&(df["project_name"]== bs_name)]
        got=(len(frame1))
        code=got+1
        name2=name1.get()
        rate2=0
        amount2=amount1.get()
        #####print(amount2)
        try:
            
            
            amount3=float(amount2)
            #####print(name2,amount2)
            frame3=frame1.loc[(frame1["description"]==name2)&(frame1["amount"]==amount3)]
            if(len(frame3)<1):
                
        
                if((name2!="")&(amount3>0)):
                    with open(data_base,"a+") as k:
                        k.write(str(bs_name))
                        k.write(",")
                        k.write(str("income"))
                        k.write(",")
                        k.write(str(code))
                        k.write(",")
                        k.write(str(name2))
                        k.write(",")
                        k.write(str(amount2))
                        k.write(",")
                        k.write(str(rate2))
                        k.write("\n")
            
                    k.close()
                reset_frame2()
                preview()
                reset_fields()
            else:
                reset_frame2()
                preview()
                reset_fields()
        except:
            messagebox.showinfo("Wrong Data formart","the data you entered in not correct  check ")
            reset_fields()
            
    def preview():
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="income")&(df["project_name"]== bs_name)]
        got=(len(frame1))
        tot1=sum_tot() 
        mm="content.txt"
        #open the file to write on it
        with open(mm,"w") as m:
            kk="Total amount is  :"+tot1+"\n"
            m.write(kk)
            for i in range(got):
                name1=frame1.iloc[i,0]
                type1=frame1.iloc[i,1]
                code1=frame1.iloc[i,2]
                desc1=frame1.iloc[i,3]
                amount1=frame1.iloc[i,4]
                rate1=frame1.iloc[i,5]
                m.write(str(name1))
                m.write("\t")
                m.write(str(type1))
                m.write("\t")
                m.write(str(code1))
                m.write("\t")
                m.write(str(desc1))
                m.write("\t\t")
                m.write(str(amount1))
                m.write("\t")
                m.write(str(rate1))
                m.write("\t")
                m.write("\n")
        m.close()
        scroll1 = Scrollbar(f2)
        scroll1.pack(side=RIGHT,fill=Y)
        text = Text(f2, font=('bold'),height=24, width=145,fg="#000000",bg="#DCDCDC",yscrollcommand=scroll1.set)
        
    
        with open(mm) as j:
            data1=j.readlines()
            for row in data1:
                text.insert(END,row)

        j.close()
        text.pack()
        scroll1.config(command=text.yview)

    

    name1=StringVar()
    rate1=StringVar()
    amount1=StringVar()
    rate1.set(0)
    lab=Label(f1,font="12",text="Enter income for "+bs_name+" business plan")
    lab.grid(row=1,column=0,columnspan=3,pady=1,padx=1,ipadx=10,ipady=11)
    b2=Button(f1,text="EXIT",bg="#8B0000",fg="white",command=exit1)
    b2.grid(row=0,column=3,columnspan=2,ipady=10,ipadx=10,pady=1,padx=20)
    lab1=Label(f1,text="name",fg="red")
    lab1.grid(row=2,column=0,padx=5)
    #lab1=Label(f1,text="Rate%",fg="red")
    #lab1.grid(row=2,column=1,padx=20)
    lab1=Label(f1,text="Amount",fg="red")
    lab1.grid(row=2,column=2,padx=20)
    name1=Entry(f1,textvariable=n1)
    name1.grid(row=3,column=0,pady=10,padx=10)
    name1.focus_set()
    #rate1=Entry(f1)
    #rate1.grid(row=3,column=1,pady=10,padx=10)
    amount1=Entry(f1,textvariable=a1)
    amount1.grid(row=3,column=2,pady=10,padx=10)
    b3=Button(f1,text="back",bg="black",fg="white",command=financing)
    b3.grid(row=4,column=0,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    b4=Button(f1,text="send to database",bg="#8B0000",fg="white",command=add_data)
    b4.grid(row=4,column=1,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    b5=Button(f1,text="NEXT",bg="orange",fg="white",command=simulation)
    b5.grid(row=4,column=3,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    preview()


def financing():
    global bs_name
    def delete(x1,x2,x3):
        def get_name1():
            df=pd.read_csv(data_base)
            lst2=lst1.get()
            
            
            #print(lst2)
            if(lst2=="None"):
                x=1
            else:
                dat=df.loc[df[x1]!=lst2]
                pd.DataFrame(dat).to_csv("index.csv",header=True,index=None)
                
                reset_frame()
                financing()
                #print(dat)
                
                
                
            
        lab=Label(f1,font="10",text="select the  Entry to delete")
        lab.grid(row=1,column=4,pady=10,padx=1,ipadx=1,ipady=1)
        df=pd.read_csv(data_base)
        df=df.loc[(df["project_name"]==bs_name)&(df["category"]=="finance")]
        frame1=df["description"]
        ls=[]
        if(len(frame1)<1):
            datak=["None"]
        else:
            for i in range(len(frame1)):
                d1=frame1.iloc[i]
                dat=[d1]
                ls=ls+dat
    
            datak=np.unique(ls)
    
    
    
    
        lst1=StringVar()
        lst1.set("None")
        selectI=OptionMenu(f1,lst1,*datak)
        selectI.grid(row=2,column=4)
        b1=Button(f1,text="Delete  ",height=2,width=8,bg="#ff1a1a",fg="white",command=get_name1)
        b1.grid(row=3,column=4 ,columnspan=1,ipady=1,ipadx=1,pady=1,padx=1)

    a1=StringVar()
    n1=StringVar()
    r1=StringVar()

    reset_frame()
    def sum_tot():
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="finance")&(df["project_name"]== bs_name)]
        tot1=str(frame1["amount"].sum())
        return tot1
    #create the two frames
    
    f1=Frame(root,width=1000,height=100,bg="#b0a94f",relief=RAISED)
    f1.pack(pady=1)
    f2=Frame(root,width=900,height=500,bg="lime",relief=RAISED)
    f2.pack(pady=1)
    delete("description","reset_frame",1)
    #valiables
    def reset_frame2():
        for wid in f2.winfo_children():
            wid.destroy()
        
    def reset_fields():
        a1.set("")
        n1.set("")
        r1.set("")
    
    def add_data():
        #getting the data entered so we have to  check if the data is empty
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="finance")&(df["project_name"]== bs_name)]
        got=(len(frame1))
        #####print(got)
        
        
        
        code=got+1
        name2=name1.get()
        rate2=rate1.get()
        amount2=amount1.get()
        period=lst3.get()
        ###print(period)
        
        
        
        
        
        try:
            
            rate3=float(rate2)
            amount3=float(amount2)
            period3=float(period)
            #####print(name2,rate3,amount2)
            framef=frame1.loc[(frame1["description"]==name2)&(frame1["amount"]==amount3)&(frame1["rate"]==rate3)]
            #####print(len(framef))
            
            if(len(framef)<1):
                
        
                if((name2!="")&(rate3<0.99)&(rate3>0.01)&(amount3>0)):
                    with open(data_base,"a+") as k:
                        k.write(str(bs_name))
                        k.write(",")
                        k.write(str("finance"))
                        k.write(",")
                        k.write(str(code))
                        k.write(",")
                        k.write(str(name2))
                        k.write(",")
                        k.write(str(amount2))
                        k.write(",")
                        k.write(str(rate2))
                        k.write(",")
                        k.write(str(period3))
                        k.write("\n")
            
                    k.close()
                reset_frame2()
                preview()
                reset_fields()
            else:
                reset_frame2()
                preview()
                reset_fields()
        except:
            messagebox.showinfo("Wrong Data formart","the data you entered in not correct  ")
            reset_fields()
            
    def preview():
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="finance")&(df["project_name"]== bs_name)]
        got=(len(frame1))
        tot1=sum_tot() 
        mm="content.txt"
        #open the file to write on it
        with open(mm,"w") as m:
            kk="Total amount is  :"+tot1+"\n"
            m.write(kk)
            for i in range(got):
                name1=frame1.iloc[i,0]
                type1=frame1.iloc[i,1]
                code1=frame1.iloc[i,2]
                desc1=frame1.iloc[i,3]
                amount1=frame1.iloc[i,4]
                rate1=frame1.iloc[i,5]
                period1=frame1.iloc[i,6]
                m.write(str(name1))
                m.write("\t")
                m.write(str(type1))
                m.write("\t")
                m.write(str(code1))
                m.write("\t")
                m.write(str(desc1))
                m.write("\t\t")
                m.write(str(amount1))
                m.write("\t")
                m.write(str(rate1))
                m.write("\t")
                m.write(str(period1))
                m.write("\n")
        m.close()
        scroll1 = Scrollbar(f2)
        scroll1.pack(side=RIGHT,fill=Y)
        text = Text(f2, font=('bold'),height=24, width=145,fg="#000000",bg="#DCDCDC",yscrollcommand=scroll1.set)
        
    
        with open(mm) as j:
            data1=j.readlines()
            for row in data1:
                text.insert(END,row)

        j.close()
        text.pack()
        scroll1.config(command=text.yview)

    

    name1=StringVar()
    rate1=StringVar()
    amount1=StringVar()
    lst3=StringVar()
    datak=['1\n', '2\n','3\n','4\n','5\n','6\n','7\n','8\n','9\n','10\n','11\n','12\n','13\n','14\n','15\n']
    rate1.set(0)
    lab=Label(f1,font="12",text="declare the fanancing for "+bs_name)
    lab.grid(row=1,column=0,columnspan=3,pady=1,padx=1,ipadx=10,ipady=11)
    b2=Button(f1,text="EXIT",bg="#8B0000",fg="white",command=exit1)
    b2.grid(row=0,column=3,columnspan=2,ipady=10,ipadx=10,pady=1,padx=20)
    lab1=Label(f1,text="name",fg="red")
    lab1.grid(row=2,column=0,padx=5)
    lab1=Label(f1,text="Rate%",fg="red")
    lab1.grid(row=2,column=1,padx=20)
    lab1=Label(f1,text="Amount",fg="red")
    lab1.grid(row=2,column=2,padx=20)

    lab1=Label(f1,text="repayment period",fg="red")
    lab1.grid(row=2,column=3,padx=20)
    
    name1=Entry(f1,textvariable=n1)
    name1.grid(row=3,column=0,pady=10,padx=10)
    name1.focus_set()
    rate1=Entry(f1,textvariable=r1)
    rate1.grid(row=3,column=1,pady=10,padx=10)
    amount1=Entry(f1,textvariable=a1)
    amount1.grid(row=3,column=2,pady=10,padx=10)
    lst3.set(datak[0])
    selectI=OptionMenu(f1,lst3,*datak)
    selectI.grid(row=3,column=3)
    b3=Button(f1,text="back",bg="black",fg="white",command=current_exp)
    b3.grid(row=4,column=0,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    b4=Button(f1,text="send to database",bg="#8B0000",fg="white",command=add_data)
    b4.grid(row=4,column=1,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    b5=Button(f1,text="NEXT",bg="orange",fg="white",command=income_fn)
    b5.grid(row=4,column=3,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    preview()


def non_current_asset():
    global bs_name
    def delete(x1,x2,x3):
        def get_name1():
            df=pd.read_csv(data_base)
            lst2=lst1.get()
            
            
            #print(lst2)
            if(lst2=="None"):
                x=1
            else:
                dat=df.loc[df[x1]!=lst2]
                pd.DataFrame(dat).to_csv("index.csv",header=True,index=None)
                
                reset_frame()
                non_current_asset()
                #print(dat)
                
                
                
            
        lab=Label(f1,font="10",text="select the  Entry to delete")
        lab.grid(row=1,column=4,pady=10,padx=1,ipadx=1,ipady=1)
        df=pd.read_csv(data_base)
        df=df.loc[(df["project_name"]==bs_name)&(df["category"]=="nce")]
        frame1=df["description"]
        ls=[]
        if(len(frame1)<1):
            datak=["None"]
        else:
            for i in range(len(frame1)):
                d1=frame1.iloc[i]
                dat=[d1]
                ls=ls+dat
    
            datak=np.unique(ls)
    
    
    
    
        lst1=StringVar()
        lst1.set("None")
        selectI=OptionMenu(f1,lst1,*datak)
        selectI.grid(row=2,column=4)
        b1=Button(f1,text="Delete  ",height=2,width=8,bg="#ff1a1a",fg="white",command=get_name1)
        b1.grid(row=3,column=4 ,columnspan=1,ipady=1,ipadx=1,pady=1,padx=1)
    
    a1=StringVar()
    n1=StringVar()
    r1=StringVar()
    tot1=StringVar()
    df=pd.read_csv(data_base)
    def back_menu():
        reset_frame()
        bs1_name()
        
    
    def sum_tot():
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="nce")&(df["project_name"]== bs_name)]
        tot1=str(frame1["amount"].sum())
        return tot1
    
    
    reset_frame()
    
    #create the two frames
    
    f1=Frame(root,width=1000,height=100,bg="#b0a94f",relief=RAISED)
    f1.pack(pady=1)
    f2=Frame(root,width=900,height=500,bg="lime",relief=RAISED)
    f2.pack(pady=1)
    delete("description","reset_frame",1)
    #valiables
    
        
    def add_data():
        #getting the data entered so we have to  check if the data is empty
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="nce")&(df["project_name"]== bs_name)]
        got=(len(frame1))
        
        
        code=got+1
        name2=name1.get()
        rate2=rate1.get()
        amount2=amount1.get()
        try:
            
            rate3=float(rate2)
            amount3=float(amount2)
            #####print(name2,rate3,amount2)
            frame3=frame1.loc[(frame1["description"]!=name2)&(frame1["amount"]!=amount3)&(frame1["rate"]!=rate3)]
            ####print("count",len(frame3))
            if(len(frame3)<1):
                
        
                if((name2!="")&(rate3<0.99)&(rate3>0.01)&(amount3>0)):
                    with open(data_base,"a+") as k:
                        k.write(str(bs_name))
                        k.write(",")
                        k.write(str("nce"))
                        k.write(",")
                        k.write(str(code))
                        k.write(",")
                        k.write(str(name2))
                        k.write(",")
                        k.write(str(amount2))
                        k.write(",")
                        k.write(str(rate2))
                        k.write("\n")
            
                    k.close()
                reset_frame2()
                preview()
                reset_fields()
            else:
                reset_frame2()
                preview()
                reset_fields()
        except:
            messagebox.showinfo("Wrong Data formart","the data you entered in not correct  ")
            reset_fields()
            
    
        
    def reset_frame2():
        for wid in f2.winfo_children():
            wid.destroy()
        
        
    def reset_fields():
        a1.set("")
        n1.set("")
        r1.set("")
               
    def preview():
        df=pd.read_csv(data_base)
        frame1=df.loc[(df["category"]=="nce")&(df["project_name"]== bs_name)]
        got=(len(frame1))
        #create the txt of the field found under the search
        tot1=sum_tot() 
        mm="content.txt"
        #open the file to write on it
        with open(mm,"w") as m:
            kk="Total amount is  :"+tot1+"\n"
            m.write(kk)
            for i in range(got):
                name1=frame1.iloc[i,0]
                type1=frame1.iloc[i,1]
                code1=frame1.iloc[i,2]
                desc1=frame1.iloc[i,3]
                amount1=frame1.iloc[i,4]
                rate1=frame1.iloc[i,5]
                m.write(str(name1))
                m.write("\t")
                m.write(str(type1))
                m.write("\t")
                m.write(str(code1))
                m.write("\t")
                m.write(str(desc1))
                m.write("\t\t")
                m.write(str(amount1))
                m.write("\t")
                m.write(str(rate1))
                m.write("\t")
                m.write("\n")
            
        m.close()
        scroll1 = Scrollbar(f2)
        scroll1.pack(side=RIGHT,fill=Y)
        text = Text(f2, font=('bold'),height=24, width=145,fg="#000000",bg="#DCDCDC",yscrollcommand=scroll1.set)
        
    
        with open(mm) as j:
            data1=j.readlines()
            for row in data1:
                text.insert(END,row)

        j.close()
        text.pack()
        scroll1.config(command=text.yview)
        

    

    name1=StringVar()
    rate1=StringVar()
    amount1=StringVar()
    rate1.set(0)
    lab=Label(f1,font="12",text="Enter non current asset for "+bs_name)
    lab.grid(row=1,column=0,columnspan=3,pady=1,padx=1,ipadx=10,ipady=11)
    b2=Button(f1,text="EXIT",bg="#8B0000",fg="white",command=exit1)
    b2.grid(row=0,column=3,columnspan=2,ipady=10,ipadx=10,pady=1,padx=20)
    lab1=Label(f1,text="name",fg="red")
    lab1.grid(row=2,column=0,padx=5)
    lab1=Label(f1,text="Rate%",fg="red")
    lab1.grid(row=2,column=1,padx=20)
    lab1=Label(f1,text="Amount",fg="red")
    lab1.grid(row=2,column=2,padx=20)
    name1=Entry(f1,textvariable=n1)
    name1.grid(row=3,column=0,pady=10,padx=10)
    name1.focus_set()
    rate1=Entry(f1,textvariable=r1)
    rate1.grid(row=3,column=1,pady=10,padx=10)
    amount1=Entry(f1,textvariable=a1)
    amount1.grid(row=3,column=2,pady=10,padx=10)
    
    
    b4=Button(f1,text="send to database",bg="#8B0000",fg="white",command=add_data)
    b4.grid(row=4,column=1,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    b5=Button(f1,text="NEXT",bg="orange",fg="white",command=current_exp)
    b5.grid(row=4,column=3,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    b6=Button(f1,text="back to the main menu",bg="green",fg="white",command=back_menu)
    b6.grid(row=4,column=0,columnspan=2,ipady=10,ipadx=10,pady=10,padx=20)
    preview()
      
    
    

#now let create a window to get the name of business

    
            
def bs1_name():
    def delete(x1,x2,x3):
        def get_name1():
            df=pd.read_csv(data_base)
            lst2=lst1.get()
            
            
            #print(lst2)
            if(lst2=="None"):
                x=1
            else:
                dat=df.loc[df[x1]!=lst2]
                pd.DataFrame(dat).to_csv("index.csv",header=True,index=None)
                bs1_name()
                #print(dat)
                
                
                
            
        lab=Label(f1,font="10",text="select the  project to delete")
        lab.grid(row=0,column=4,pady=10,padx=1,ipadx=1,ipady=1)
        df=pd.read_csv(data_base)
        frame1=df["project_name"]
        ls=[]
        if(len(frame1)<1):
            datak=["None"]
        else:
            for i in range(len(frame1)):
                d1=frame1.iloc[i]
                dat=[d1]
                ls=ls+dat
    
            datak=np.unique(ls)
    
    
    
    
        lst1=StringVar()
        lst1.set("None")
        selectI=OptionMenu(f1,lst1,*datak)
        selectI.grid(row=1,column=4)
        b1=Button(f1,text="Delete  ",height=2,width=8,bg="#ff1a1a",fg="white",command=get_name1)
        b1.grid(row=3,column=4 ,columnspan=1,ipady=1,ipadx=1,pady=1,padx=1)
    
    bs_name2=StringVar()
    
    
    def res():
        bs_name2.set("")
    
            
    #creatining a  frame
    f1=Frame(root,width=1000,height=700,bg="#b0a94f",relief=RAISED)
    f1.pack(pady=100)
    lab=Label(f1,font="12",text="Enter Business Name")
    lab.grid(row=0,column=1,pady=50,padx=10,ipadx=10,ipady=11)
    lab=Label(f1,font="12",text="select the existing project to continue")
    lab.grid(row=0,column=2,pady=50,padx=10,ipadx=10,ipady=11)
    delete("project_name","reset_frame",1)
    
    df=pd.read_csv(data_base)
    frame1=df["project_name"]
    ls=[]
    if(len(frame1)<1):
        datak=["NONE"]
    else:
        for i in range(len(frame1)):
            d1=frame1.iloc[i]
            dat=[d1]
            ls=ls+dat
    
        datak=np.unique(ls)
    
    
    
    
    lst1=StringVar()
    lst1.set("NONE")
   
    bs_name1=Entry(f1,width=25,textvariable=bs_name2)
    bs_name1.grid(row=1,column=0,ipady=10,columnspan=2)
    bs_name1.focus_set()
    selectI=OptionMenu(f1,lst1,*datak)
    selectI.grid(row=1,column=2)
    

    def get_name():
        global bs_name,tot1
        
        bs_name3=bs_name1.get()
        lst2=lst1.get()
        #####print(lst2,bs_name3)
        if((bs_name3=="")&(lst2=="NONE")):
            bs_name=bs_name3
        elif( (bs_name3=="")&(lst2!="NONE")):
            bs_name=lst2
            #####print(bs_name)
        elif( (bs_name3!="")&(lst2!="NONE")):
            bs_name=lst2
            #####print(bs_name)
        
        elif( (bs_name3!="")&(lst2=="NONE")):
            bs_name=bs_name3
            #####print(bs_name)
        
        
        if((bs_name!="")):
            messagebox.showinfo("Business Name","Your Business Name is "+bs_name)
            non_current_asset()
            tot1=(sum_data(data_base,bs_name,"nce"))
            #####print(sum_dep(data_base,bs_name,"nce"))
            res()

    b1=Button(f1,text="Next  ",height=2,width=20,bg="#FF8C00",fg="white",command=get_name)
    b1.grid(row=5,column=2 ,columnspan=2,ipady=5,ipadx=10,pady=50,padx=100)
    
    b2=Button(f1,text="EXIT",bg="#8B0000",fg="white",command=exit1)
    b2.grid(row=5,column=0,columnspan=2,ipady=10,ipadx=40,pady=50,padx=20)
    
    

bs1_name()

root.mainloop()
