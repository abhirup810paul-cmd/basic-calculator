from tkinter import *


first_number = second_number = operator = None


def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)


def backspace():
    current = result_label['text']
    new = current[:-1]
    result_label.config(text=new)


def clear():
    result_label.config(text='')


def get_operator(op):
    global first_number, operator

    if result_label['text'] == '':
        if op == '+':
            get_digit('+')
        elif op == '-':
            get_digit('-')
    else:
        first_number = float(result_label['text'])
        operator = op
        result_label.config(text='')


    # first_number = float(result_label['text'])
    # operator = op

    # if first_number == None and op == '-':
    #     get_digit('-')
    # # result_label.config(text= str(first_number) + str(operator))
    # else:
    #     result_label.config(text='')


def get_result():
    global first_number, second_number, operator

    # Now we're gonna extract the second number
     

    second_number = float(result_label['text'])

    if first_number != None:
        if operator == '+':
            sum = str(round(first_number+second_number, 2))
            if sum[-2:] == '.0':
                result_label.config(text=sum[:-2])
            else:
                result_label.config(text=sum)
        elif operator == '-':
            diff = str(round(first_number-second_number, 2))
            if diff[-2:] == '.0':
                result_label.config(text=diff[:-2])
            else:
                result_label.config(text=diff)
        elif operator == 'x':
            mul = str(round(first_number*second_number, 2))
            if mul[-2:] == '.0':
                result_label.config(text=mul[:-2])
            else:
                result_label.config(text=mul)
        else:
            if second_number == 0:
                result_label.config(text='Error!')
            else:
                div = str(round(first_number/second_number , 2))
                if div[-2:] == '.0':
                    result_label.config(text=div[:-2])
                else:
                    result_label.config(text=div)

        first_number = None
    else:
        res = str(second_number)
        if res[-2:] == '.0':
            result_label.config(text=res[:-2])
        else:
            result_label.config(text=res)


def percentage():
    number = float(result_label['text'])
    num = str(round(number/100, 2))
    
    if num[-2:] == '.0':
        result_label.config(text=num[:-2])
    else:
        result_label.config(text=num)


root = Tk()
root.title('Calculator')
# root.geometry('280x380')
root.geometry('280x444')

root.resizable(0,0)      # This helps to make the size of the window non-changable

# root.config(bg='black')
root.configure(background='black')

result_label = Label(root, text='', fg='white',bg='black')
result_label.grid(row=0,column=0, columnspan=9000, pady=(50,25), sticky='w')
result_label.config(font=('verdana', 30, 'bold'))



# Buttons: -
# 1st row: -

button_all_clear = Button(root, text='AC', bg='#00a65a', fg='white', width=5, height=2, command=lambda :clear())
button_all_clear.grid(row=1, column=0)
button_all_clear.config(font=('verdana', 14))

button_percentage = Button(root, text='%', bg='#00a65a', fg='white', width=5, height=2, command=percentage)
button_percentage.grid(row=1, column=1)
button_percentage.config(font=('verdana', 14))

button_backspace = Button(root, text='<-', bg='#00a65a', fg='white', width=5, height=2, command=lambda :backspace())
button_backspace.grid(row=1, column=2)
button_backspace.config(font=('verdana', 14))

button_div = Button(root, text='/', bg='#00a65a', fg='white', width=5, height=2, command= lambda : get_operator('/'))
button_div.grid(row=1, column=3)
button_div.config(font=('verdana', 14))



# 2nd row: -

button_7 = Button(root, text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(7))
button_7.grid(row=2, column=0)
button_7.config(font=('verdana', 14))

button_8 = Button(root, text='8', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(8))
button_8.grid(row=2, column=1)
button_8.config(font=('verdana', 14))

button_9 = Button(root, text='9', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(9))
button_9.grid(row=2, column=2)
button_9.config(font=('verdana', 14))

button_mul = Button(root, text='x', bg='#00a65a', fg='white', width=5, height=2, command=lambda : get_operator('x'))
button_mul.grid(row=2, column=3)
button_mul.config(font=('verdana', 14))



# 3rd row: -

button_4 = Button(root, text='4', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(4))
button_4.grid(row=3, column=0)
button_4.config(font=('verdana', 14))

button_5 = Button(root, text='5', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(5))
button_5.grid(row=3, column=1)
button_5.config(font=('verdana', 14))

button_6 = Button(root, text='6', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(6))
button_6.grid(row=3, column=2)
button_6.config(font=('verdana', 14))

button_minus = Button(root, text='-', bg='#00a65a', fg='white', width=5, height=2, command= lambda : get_operator('-'))
button_minus.grid(row=3, column=3)
button_minus.config(font=('verdana', 14))



# 4th row: -

button_1 = Button(root, text='1', bg='#00a65a', fg='white', width=5, height=2, command= lambda :get_digit(1))
button_1.grid(row=4, column=0)
button_1.config(font=('verdana', 14))

button_2 = Button(root, text='2', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(2))
button_2.grid(row=4, column=1)
button_2.config(font=('verdana', 14))

button_3 = Button(root, text='3', bg='#00a65a', fg='white', width=5, height=2, command=lambda : get_digit(3))
button_3.grid(row=4, column=2)
button_3.config(font=('verdana', 14))

button_add = Button(root, text='+', bg='#00a65a', fg='white', width=5, height=2, command= lambda : get_operator('+'))
button_add.grid(row=4, column=3)
button_add.config(font=('verdana', 14))



# 5th row: -

button_00 = Button(root, text='00', bg='#00a65a', fg='white', width=5, height=2, command= lambda :get_digit('00'))
button_00.grid(row=5, column=0)
button_00.config(font=('verdana', 14))

button_0 = Button(root, text='0', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(0))
button_0.grid(row=5, column=1)
button_0.config(font=('verdana', 14))

button_point = Button(root, text='.', bg='#00a65a', fg='white', width=5, height=2, command= lambda : get_digit('.'))
button_point.grid(row=5, column=2)
button_point.config(font=('verdana', 14))

button_equal = Button(root, text='=', bg='#00a65a', fg='white', width=5, height=2, command=get_result)
button_equal.grid(row=5, column=3)
button_equal.config(font=('verdana', 14))


root.mainloop()