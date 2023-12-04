from tkinter import *
from tkinter import messagebox as msb
from tkinter import ttk
from threading import Thread
from services import news_search
import smtplib, ssl
import webbrowser


# Email Constants
SENDER = "fake.poulstar@gmail.com"
PASSWORD = "ftgtgsssfukhiyik"
SMTP_SERVER = "smtp.gmail.com"
PORT = 465  # For SSL


# Color Constants
BG = "#333333"
BG2 = "#444444"
FG = "orange"
FG2 = "yellow"

def search(event=None):
    search_item = e_search.get().strip()
    if len(search_item)==0:
        msb.showerror("Error!", "Search box should have at least one character!")
        return    
    list_data = news_search(search_item)
    if not list_data:
        msb.showinfo("No data!", "There is no data about the item you searched.")
        return
    treev.delete(*treev.get_children())
    for data in list_data:
        info = []
        for key, value in data.items():
            info.append(value)
            print(info)
        treev.insert(parent='', index=0, iid=info[0], text=info[0], values=info[1:])
            # _id <class 'str'>
            # title <class 'str'>
            # description <class 'str'>
            # link <class 'str'>
            # creator <class 'str'>
            # pubDate <class 'str'>


def send_email_2(email_address):
    try:
        links = []
        for child in treev.get_children():
            link = treev.item(child)["values"][2]
            if link.startswith('http'):
                links.append(link)
            else: # نمیدونم چرا بعضی از جاها تو اندیس شماره ۱ میومد. به خاطر همین این کد رو این شکلی نوشتم.
                link = treev.item(child)["values"][1]
                if link.startswith('http'):
                    links.append(link)
        message = "Hi there!\nYou have requested to get this email which contains "
        message += "some links about your favorite title. Hope you enjoy it! Here you are:\n"
        for link in links:
            message+=f"{link}\n"
        print(message)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, email_address, message)
            msb.showinfo("Success", "Email sent successfully!")
    except:
        msb.showwarning("Warning", "Check if the email address really exists!")
    finally:
        btn_email.config(state='normal', relief='raised')

def send_email(event=None):
    email_address = e_email.get().strip()
    if len(email_address)==0:
        msb.showerror("Error!", "Email address can't be empty!")
        return
    elif email_address.count('@') == 0:
        msb.showerror("Error!", "Email address should have at least one '@' character!")
        return
    elif email_address.count('.') == 0:
        msb.showerror("Error!", "Email address should have at least one '.' character!")
        return
    email_address = email_address.split(',')
    Thread(target=send_email_2, args=(email_address,), daemon=True).start()
    btn_email.config(state='disabled', relief='flat')


def on_click(event):
    try:
        item = treev.selection()[0]
        values = treev.item(item)
        link = values['values'][2]
        if link.startswith('http'):
            webbrowser.open(link)
        else:
            link = values['values'][1]
            if link.startswith('http'):
                webbrowser.open(link)
            else:
                msb.showinfo('!', 'No link!')

    except IndexError:
        msb.showwarning("!", "Click on an Item Please!")
    # print("you clicked on", event, treev.item(item))

    

root = Tk()
root.geometry('1200x500+50+50')
root.config(bg=BG)


# frames
frame_top = Frame(root, bg=BG)
frame_middle = Frame(root, bg=BG)
frame_middle2 = Frame(root, bg=BG)
frame_bottom = Frame(root, bg=BG)
frame_top.pack(pady=10)
frame_middle.pack()
frame_middle2.pack()
frame_bottom.pack(side='bottom')
# end frames


# frame top
l_welcome = Label(frame_top, text='Welcome to New York times'.upper(), bg=BG, fg=FG, font=('Times', 24))
l_welcome.pack()
# end frame top


# frame middle
l_search= Label(frame_middle, text='What are you looking for?', bg=BG, fg=FG, font=('Times', 22))
e_search = Entry(frame_middle, bg=BG2, fg=FG, insertbackground=FG, font=('Times', 22), bd=4)
e_search.bind('<Return>', search)
btn_search = Button(frame_middle, bg=BG, fg=FG, font=('', 18), relief='raised', bd=4, text='Search', padx=24, command=search)
l_dbl_click= Label(frame_middle, text='Double click on a row to open the link in browser', bg=BG, fg=FG, font=('Times', 14))
l_search.grid(row=1, column=1, columnspan=2)
e_search.grid(row=2, column=1)
btn_search.grid(row=2, column=2, padx=10)
l_dbl_click.grid(row=3, column=1, columnspan=2)
# end frame middle


# frame middle2
treev = ttk.Treeview(frame_middle2, columns=(1, 2, 3, 4, 5), show='headings', height=8)
treev.bind("<Double-1>", on_click)
treev.heading(1, text='title')
treev.column(1, width=200, anchor='c')
treev.heading(2, text='description')
treev.column(2, width=200, anchor='c')
treev.heading(3, text='link')
treev.column(3, width=200, anchor='c')
treev.heading(4, text='creator')
treev.column(4, width=200, anchor='c')
treev.heading(5, text='pubDate')
treev.column(5, width=200, anchor='c')
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
treev.grid(row=10, column=1, columnspan=10)
vertical_scroll_bar = Scrollbar(frame_middle2, orient='vertical', command=treev.yview)
treev.config(yscrollcommand=vertical_scroll_bar.set)
vertical_scroll_bar.grid(row=10, column=11, sticky='ns')
# end frame middle2


# frame bottom
l_email= Label(frame_bottom, text='Enter your email address if you want to get email of above links?\nYou can separate multiple emails by \',\'', bg=BG, fg=FG2, font=('Times', 18))
e_email = Entry(frame_bottom, bg=BG2, fg=FG2, insertbackground=FG, font=('Times', 18), bd=3, width=26)
e_email.bind("<Return>", send_email)
btn_email = Button(frame_bottom, bg=BG, fg=FG2, font=('', 18), relief='raised', bd=4, text='Send', padx=28, command=send_email)
l_email.grid(row=1, column=1, columnspan=2)
e_email.grid(row=2, column=1)
btn_email.grid(row=2, column=2)
# end frame bottom


root.mainloop()