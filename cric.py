from tkinter import *
import time
import requests
import json

root=Tk()

root.geometry("720x250")

match_data=requests.get('http://cricapi.com/api/cricketScore?unique_id=1216501&apikey=TInANu8EmdfIVlKU88biKMmQTMO2')
json_data=match_data.json()

background_image = PhotoImage(file='C:\\Users\\VAIBHAV_2\\Desktop\\bg.png')
background_label = Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

def times():
	current_score=json_data['stat']
	cs1=json_data['team-1']
	cs2=json_data['team-2']
	sc=json_data['score']
	s.configure(text=cs1+" Vs "+cs2)
	t.configure(text=sc)
	score.configure(text="Status :  "+current_score)
	score.after(200,times)

# frame = Frame(root,bg='#b3b3ff')
# frame.place(relx=0.5,rely=0.02,relwidth=0.85, relheight=0.55,anchor='n')

score=Label(root,font=("time",15,"bold"),bg="#b3b3ff")
score.grid(row=2,column=0,pady=10,padx=75)

s=Label(root,font=("time",15,"bold"),bg="#b3b3ff")
s.grid(row=0,column=0,pady=10,padx=75)

t=Label(root,font=("time",15,"bold"),bg="#b3b3ff")
t.grid(row=1,column=0,pady=10,padx=75)

times()

root.mainloop()
