import tkinter as tk
from tkinter import Button, Label, Menu, StringVar, Variable, ttk
from tkinter import font,filedialog,messagebox,colorchooser
import os
from tkinter.constants import BOTH, END, LEFT, UNDERLINE, X
 
main_appication = tk.Tk()
main_appication.geometry('1200x800')
main_appication.title('Tenali Text Editor')


############################################################# Main Menu #########################################################
# File Icons
file_icon = tk.PhotoImage(file='Img/new.png')
save_icon = tk.PhotoImage(file='Img/save.png')
save_as_icon = tk.PhotoImage(file='Img/save_as.png')
open_icon = tk.PhotoImage(file='Img/open.png')
exit_icon = tk.PhotoImage(file='Img/exit.png')

main_menu = tk.Menu()
# Configuration File Menu 
file = tk.Menu(main_menu,tearoff=False)

# Configuration Edit Menu 
copy_icon = tk.PhotoImage(file='Img/copy.png')
paste_icon = tk.PhotoImage(file='Img/paste.png')
cut_icon = tk.PhotoImage(file='Img/cut.png')
clear_icon = tk.PhotoImage(file='Img/clear_all.png')
find_icon = tk.PhotoImage(file='Img/find.png')

edit = tk.Menu(main_menu,tearoff=False)

# copy ,cut , clear all , find 

# Configuration view Menu 
view = tk.Menu(main_menu,tearoff=False)

tool_icon = tk.PhotoImage(file='Img/tool_bar.png')
stutas_icon = tk.PhotoImage(file='Img/status_bar.png')



# Configuration Color theme Menu 
color_theme = tk.Menu(main_menu,tearoff=False)
light_default_icon = tk.PhotoImage(file='Img/light_default.png')
light_plus_icon = tk.PhotoImage(file='Img/light_plus.png')
dark_icon = tk.PhotoImage(file='Img/dark.png')
red_icon = tk.PhotoImage(file='Img/red.png')
monokai_icon = tk.PhotoImage(file='Img/monokai.png')
night_blue_icon = tk.PhotoImage(file='Img/night_blue.png')

theme_choice = StringVar()
color_icons  = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict = {
    'Light default': ('#000000','#ffffff'),
    'Light Plus': ('#000000','#e0e0e0'),
    'Dark': ('#c4c4c4','#2d2d2d'),
    'Red': ('#2d2d2d','#ffe8e8'),
    'Monokai': ('#d3b774','#474747'),
    'Night Blue': ('#ededed','#6b9dc2')
}


main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color',menu=color_theme)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ending Main Menu !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

############################################################# ToolBar #########################################################
Tool_Bar = Label(main_appication)
Tool_Bar.pack(side=tk.TOP,fill=tk.X)

font_tuple = tk.font.families()

# Configuration of Font Family 
font_family=StringVar()

font_box = ttk.Combobox(Tool_Bar,width=30,textvariable=font_family,state="readonly"   )
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

# Configuration of Font Size
font_var = tk.IntVar()
font_size = ttk.Combobox(Tool_Bar,width=15,textvariable=font_var)
font_size['value'] = tuple(range(8,80,2))
font_size.current(2)

font_size.grid(row=0,column=1,padx=5)

# Bold Button
bold_icon = tk.PhotoImage(file='Img/bold.png')

bold_button = Button(Tool_Bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=4)

# Italic Button
italic_icon = tk.PhotoImage(file='Img/italic.png')
bold_italic = Button(Tool_Bar,image=italic_icon)
bold_italic.grid(row=0,column=3,padx=4)

# Underline Button
underline_icon = tk.PhotoImage(file='Img/underline.png')
bold_underline = Button(Tool_Bar,image=underline_icon)
bold_underline.grid(row=0,column=4,padx=4)

# Font color Button 
Font_color_icon = tk.PhotoImage(file='Img/font_color.png')
Font_color_button = Button(Tool_Bar,image=Font_color_icon,)
Font_color_button.grid(row=0,column=5)

# Align Left Buttton
Align_left_icon = tk.PhotoImage(file='Img/align_left.png')
Align_center_icon = tk.PhotoImage(file='Img/align_center.png')
Align_right_icon = tk.PhotoImage(file='Img/align_right.png')

Align_left_button = Button(Tool_Bar,image=Align_left_icon)
Align_left_button.grid(row=0,column=6,padx=5)

Align_center_button = Button(Tool_Bar,image=Align_center_icon)
Align_center_button.grid(row=0,column=7,padx=5)

Align_right_button = Button(Tool_Bar,image=Align_right_icon)
Align_right_button.grid(row=0,column=8,padx=5)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ending ToolBar !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

############################################################# Text Editor#########################################################
text_editor = tk.Text(main_appication)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_appication)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

current_font = 'Arial'
current_size = 12
# Configuration The Font Family 
def font_Families(a):
    text_editor.config(font=(font_family.get(),font_size.get()))
    # print("hello ")
font_box.bind("<<ComboboxSelected>>",font_Families)

# Configuration Font Size 
def font_families_size(a):
    text_editor.config(font=(font_family.get(),font_size.get()))
font_size.bind("<<ComboboxSelected>>",font_families_size)

def font_text_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(font_box.get(), font_size.get(), 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(font_box.get(), font_size.get(), 'normal'))
   
bold_button.config(command=font_text_bold)

# Configuration italic Button 
def font_text_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(font_box.get(), font_size.get(),  'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(font_box.get(), font_size.get(), 'roman'))
   
bold_italic.config(command=font_text_italic)



# Configuration Underline Button 
text_underline = 0
def font_text_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(font_box.get(), font_size.get(),  'underline'))
    if text_property.actual()['undeline'] == 1:
        text_editor.configure(font=(font_box.get(), font_size.get(), 'noramal'))

bold_underline.config(command=font_text_underline)

# Configuration Font_color_button
def change_font_color():
    font_color = colorchooser.askcolor()
    text_editor.config(fg=font_color[1])

Font_color_button.config(command=change_font_color)

text_editor.config(font=(current_font,current_size))


def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

Align_left_button.configure(command=align_left)

## center 
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

Align_center_button.configure(command=align_center)

## right 
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

Align_right_button.configure(command=align_right)


# Configuration of word and charactore counter 

status_bar = tk.Label(main_appication,text='Hello I am Tenli Ramkrishna')
status_bar.pack(side=tk.BOTTOM)
text_changed = False
def Counter_text(a):
    global text_changed
    if text_editor.edit_modified():
        words = len(text_editor.get(1.0 , 'end-1c').split())
        Characotre = len(text_editor.get(1.0 , 'end-1c').replace(" ",""))
        text_changed = True


        status_bar.config(text=f"Charct : {Characotre}  words : {words} ")
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',Counter_text)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ending Text Editor!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#############################################################  StutasBar#########################################################
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ending StutasBar !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

############################################################# Main Menu Functionlity #########################################################
# File Menu functionality
# Variable
url = ''
# New file Functionality
def New_File(event=None):
    global url 
    url = ''
    text_editor.delete(1.0,END)

file.add_command(label="New",image=file_icon,compound=LEFT,accelerator='ctrl+n',command=New_File)

# Open File Functionality
def Open_New(event=None):
    global url
    true = 0
   
    if len(text_editor.get(1.0,END))-1==0:
        true = 1
    else:
        Ans = messagebox.askyesno(title='Text selection',message='do You want to Save data')
        print(Ans)
        if Ans==True:
            true = 1
            print("yes",true)

        else:
            true = 0
            print("No",true)
    if true==1:
        try:
            url  = filedialog.askopenfilename(initialdir=os.getcwd(),title="select File",filetypes=(('Text Files','*.txt'),('Text document','*.*')))

            with open(url) as fr:
                text_editor.delete(1.0,END)
                text_editor.insert(1.0,fr.read())
        
            main_appication.title(os.path.basename(url))
        except FileNotFoundError:
            return
        except:
            return

file.add_command(label="Open",image=open_icon,compound=LEFT,accelerator='ctrl+o',command=Open_New)

# save File Functionality
def Save_File(event=None):
    filedialog.asksaveasfilename(initialdir=os.getcwd(),filetypes=(('Text File','Ultitled.text')))
file.add_command(label="Save",image=save_icon,compound=LEFT,accelerator='ctrl+s',command=Save_File)


# save as File Functionality
def Save_as_File(event=None):
    pass

file.add_command(label="Save as",image=save_as_icon,compound=LEFT,accelerator='ctrl+alt+s',command=Save_as_File)


# Exit File Functionality
def Exit_File(event=None):
    pass

file.add_command(label="Exit",image=exit_icon,compound=LEFT,accelerator='ctrl+q',command=Exit_File)

# Edit Menu functionality
edit.add_command(label='Copy',compound=LEFT,image=copy_icon,accelerator='ctrl+c')
edit.add_command(label='Paste',compound=LEFT,image=paste_icon,accelerator='ctrl+c')
edit.add_command(label='Cut',compound=LEFT,image=cut_icon,accelerator='ctrl+x')
edit.add_command(label='Clear all',compound=LEFT,image=clear_icon,accelerator='ctrl+z')
edit.add_command(label='Find',compound=LEFT,image=find_icon,accelerator='ctrl+f')
# View Menu functionality

view.add_checkbutton(label='Tool Bar',compound=LEFT,image=tool_icon)
view.add_checkbutton(label='Status Bar',compound=LEFT,image=stutas_icon)
# Color Menu functionality
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],compound=LEFT,variable=theme_choice)
    count +=1



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Ending Main Menu Functionlity !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

main_appication.config(menu=main_menu)
main_appication.wm_iconbitmap('Img/ico.ico')
main_appication.mainloop()