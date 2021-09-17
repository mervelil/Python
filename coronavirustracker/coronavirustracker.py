import requests
from bs4 import BeautifulSoup
import plyer
import pandas as pd
def datacollected():
    def notification(title,message):
        plyer.notification.notify(
        title=title,
        message=message,
        app_icon='coronavirus.ico',
        timeout=15
        )
         #we keep notification for 15 sec
    url="https://www.worldometers.info/coronavirus/"
    res=requests.get(url)
    soup=BeautifulSoup(res.content,"html.parser")
    tbody=soup.find('tbody')
    abc=tbody.find_all('tr')
    countrynotification=cntdata.get()
    if(countrynotification==""):
        countrynotification="world"
    serial_number,countries,total_cases,new_cases,total_death,new_deaths,total_recovered,active_cases=[],[],[],[],[],[],[],[]
    serious_critical,total_cases_permn,total_deaths_permn,total_tests,total_test_permillion,total_pop=[],[],[],[],[],[]
    header =['serial_number','countries','total_cases','new_cases','total_death','new_deaths','total_recovered','active_cases','serious_critical','total_cases_permn','total_deaths_permn','total_tests','total_test_permillion','total_pop']
    for i in abc:
        id=i.find_all('td')
        if(id[1].text.strip().lower()==countrynotification):
            totalcases1=int(id[2].text.strip().replace(',',""))
            totaldeath=id[4].text.strip()
            newcases=id[3].text.strip()
            newdeaths=id[5].text.strip()
            notification("CORONA RECENT UPDATES of {}".format(countrynotification),"Total Cases : {}\nTotal Deaths : {}\nNew Cases : {}\nNew Deaths : {}".format(totalcases1,totaldeath,newcases,newdeaths))

        serial_number.append(id[0].text.strip())
        countries.append(id[1].text.strip())
        total_cases.append(id[2].text.strip().replace(',',""))
        new_cases.append(id[3].text.strip())
        total_death.append(id[4].text.strip())
        new_deaths.append(id[5].text.strip())
        total_recovered.append(id[6].text.strip())
        active_cases.append(id[7].text.strip())
        serious_critical.append(id[8].text.strip())
        total_cases_permn.append(id[9].text.strip())
        total_deaths_permn.append(id[10].text.strip())
        total_tests.append(id[11].text.strip())
        total_test_permillion.append(id[12].text.strip())
        total_pop.append(id[13].text.strip())
    dataframe= pd.DataFrame(list(zip(serial_number,countries,total_cases,new_cases,total_death,new_deaths,total_recovered,active_cases,serious_critical,total_cases_permn,total_deaths_permn,total_tests,total_test_permillion,total_pop)),columns=header)
    sorts=dataframe.sort_values('total_cases',ascending=False)
    for a in flist:
      if(a=='html'):
        path2='{}/coronadata.html'.format(path)
        sorts.to_html(r'{}'.format(path2)) #r to read our metioned path
      if(a=='json'):
        path2='{}/coronadata.json'.format(path)
        sorts.to_json(r'{}'.format(path2)) 
      if(a=='csv'):
        path2='{}/coronadata.csv'.format(path)
        sorts.to_csv(r'{}'.format(path2)) 
      if (len(flist) !=0):
        messagebox.showinfo("Notification","Corona Record is Saved {}".format(path2),parent=coro)
def downloaddata():
    global path
    if(len(flist) !=0):
        path=filedialog.askdirectory()
    else:
        pass
    datacollected()
    flist.clear()
    Inhtml.configure(state='normal')
    Injson.configure(state='normal')
    Inexcel.configure(state='normal')

def  inhtmldownload():
    flist.append('html')
    Inhtml.configure(state='disabled')
def  injsondownload():
    flist.append('json')
    Injson.configure(state='disabled')
def  inexceldownload():
    flist.append('csv')
    Inexcel.configure(state='disabled')

from tkinter import *
from tkinter import messagebox,filedialog
coro =Tk()
coro.title("Corona Virus Information")
coro.geometry('800x500+200+100')
coro.configure(bg='#046173')
coro.iconbitmap('coronavirus.ico')
flist=[]
path=''
mainlabel=Label(coro,text="Corona Virus Live Tracker",font=("new roman",30," italic bold"),bg ="#05897A",width=33,fg="black",bd=5)
mainlabel.place(x=0,y=0)

label1= Label(coro,text="Country Name",font=("arial",20," italic bold"),bg ="#046173")
label1.place(x=15,y=100)

label2= Label(coro,text="Download File in",font=("arial",20," italic bold"),bg ="#046173")
label2.place(x=15,y=200)

cntdata=StringVar()
entry1=Entry(coro,textvariable=cntdata,font=("arial",20,"italic bold"),relief=RIDGE,bd=2,width=32)
entry1.place(x=280,y=100)
Inhtml=Button(coro,text="Html",bg= "#2DAE9A",font=("arial",15,"italic bold"),relief=RIDGE,activebackground="#059458" ,activeforeground="white",bd=5,width=5 ,command=inhtmldownload)
Inhtml.place(x=300,y=200)
Injson=Button(coro,text="json",bg= "#2DAE9A",font=("arial",15,"italic bold"),relief=RIDGE,activebackground="#059458" ,activeforeground="white",bd=5,width=5,command=injsondownload)
Injson.place(x=300,y=260)
Inexcel=Button(coro,text="Excel",bg= "#2DAE9A",font=("arial",15,"italic bold"),relief=RIDGE,activebackground="#059458" ,activeforeground="white",bd=5,width=5, command=inexceldownload)
Inexcel.place(x=300,y=320)
Submit=Button(coro,text="Submit",bg= "#CB054A",font=("arial",15,"italic bold"),relief=RIDGE,activebackground="#7B0519" ,activeforeground="white",bd=5,width=25,command=downloaddata)
Submit.place(x=450,y=260)
coro.mainloop()
#ctrl k+ctrl u