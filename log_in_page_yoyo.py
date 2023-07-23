import tkinter as tk

window = tk.Tk()
window.title("log in")
window.geometry("800x600")




st_login =tk.Label(window,text="")

def log_in():
    if entry_username.get() == 'yossef' and entry_password.get() == 'password':
        st_login.config(text="success!!",fg="green")
    else:
        st_login.config(text="failed!!",fg="red")


my_frame=tk.Frame(window,padx=20,pady=10)



label_username = tk.Label(window,text="username : ")


entry_username = tk.Entry(window,width=20)


label_password = tk.Label(window,text="password : ")



entry_password = tk.Entry(window,width=20,show="*")





btn = tk.Button(my_frame,text="login",command=log_in)





label_username.pack()
entry_username.pack()
label_password.pack()
entry_password.pack()



my_frame.pack()

btn.pack()

st_login.pack()

window.mainloop()