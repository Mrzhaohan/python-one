import tkinter
import turtle
def wjx(event):   #事件响应函数
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)

root = tkinter.Tk()
label = tkinter.Label(root,text='你好') #标签设定
label.pack()
button1 = tkinter.Button(root,text='五角星')
button1.bind('<Button-1>',wjx)   #绑定事件
button1.pack()
menu = tkinter.Menu(root)  #生成菜单
submenu = tkinter.Menu(menu,tearoff=0)  #生成下拉菜单
submenu.add_command(label='open')  #向下拉菜单添加指令名为open
submenu.add_command(label='save')  #向下拉菜单添加指令名为save
menu.add_cascade(label='File',menu=submenu) #将下拉菜单添加到菜单
root.config(menu=menu)
root.mainloop()
