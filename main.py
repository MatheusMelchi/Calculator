import numpy as np
import math
from tkinter import *


def main():
    """Main Function"""

    # Window creation and configuration
    root = Tk()
    root.title('Calculator')
    root.iconbitmap('./images/icon-calc.ico')

    # Label num variable
    label_num_var = StringVar()
    label_num_var.set('')
    # Label op variable
    label_op_var = StringVar()
    label_op_var.set('')
    # List to put the numbers in (list_num == str, list_num_float == float)
    list_num = []
    list_num_float = []

    # All functions that command buttons
    def button_1():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '1')

    def button_2():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '2')

    def button_3():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '3')

    def button_4():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '4')

    def button_5():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '5')

    def button_6():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '6')

    def button_7():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '7')

    def button_8():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '8')

    def button_9():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '9')

    def button_0():
        nonlocal label_num_var
        label_num_var.set(label_num_var.get() + '0')

    def button_point():
        """Function that puts a point on the number"""
        nonlocal label_num_var
        if label_num_var.get() == '':
            pass
        elif label_num_var.get() != '' and '.' not in label_num_var.get():
            label_num_var.set(label_num_var.get() + '.')

    def button_plus():
        """Function that sets the var label_op_var to +, also resets label num"""
        nonlocal label_num_var, list_num
        if label_num_var.get() == '':
            pass
        elif label_num_var.get() != '':
            list_num.append(label_num_var.get())
        label_num_var.set('')
        label_op_var.set('+')

    def button_minus():
        """Function that sets the var label_op_var to -, also resets label num"""
        nonlocal label_num_var, list_num
        if label_num_var.get() == '':
            pass
        elif label_num_var.get() != '':
            list_num.append(label_num_var.get())
        label_num_var.set('')
        label_op_var.set('-')

    def button_mult():
        """Function that sets the var label_op_var to *, also resets label num"""
        nonlocal label_num_var, list_num
        if label_num_var.get() == '':
            pass
        elif label_num_var.get() != '':
            list_num.append(label_num_var.get())
        label_num_var.set('')
        label_op_var.set('*')

    def button_div():
        """Function that sets the var label_op_var to /, also resets label num"""
        nonlocal label_num_var, list_num
        if label_num_var.get() == '':
            pass
        elif label_num_var.get() != '':
            list_num.append(label_num_var.get())
        label_num_var.set('')
        label_op_var.set('/')

    def button_equal():
        """Function that does all the calculations based on the list_num and label_op_var"""
        nonlocal label_num_var, label_op_var, list_num, list_num_float
        list_num.append(label_num_var.get())
        list_num_float = [float(i) for i in list_num]
        print(list_num)
        if label_op_var.get() == '+':
            value_sum = sum(list_num_float)
            label_num_var.set(str(round(value_sum, 3)))
            label_op_var.set('')
            list_num = []
            list_num_float = []

        elif label_op_var.get() == '-':
            value_sum = sum(list_num_float[1:])
            value_minus = list_num_float[0] - value_sum
            label_num_var.set(str(round(value_minus, 3)))
            label_op_var.set('')
            list_num = []
            list_num_float = []

        elif label_op_var.get() == '*':
            value_mult = 1
            for i in list_num_float:
                value_mult = value_mult * i
            label_num_var.set(str(round(value_mult, 3)))
            label_op_var.set('')
            list_num = []
            list_num_float = []

        elif label_op_var.get() == '/':
            value_multi = 1
            for i, value in enumerate(list_num_float):
                if i > 0:
                    value_multi = value_multi * value
            value_div = list_num_float[0] / value_multi
            label_num_var.set(str(round(value_div, 3)))
            label_op_var.set('')
            list_num = []
            list_num_float = []

    def button_clear():
        """Function that clears all lists and labels"""
        nonlocal label_num_var, list_num, list_num_float
        label_num_var.set('')
        label_op_var.set('')
        list_num = []
        list_num_float = []

    # Label Number
    label_num = Label(root, width=60, textvariable=label_num_var, bg='#b5b9ba', text='')
    label_num.grid(row=0, column=0, columnspan=3)
    # Label Operator
    label_op = Label(root, width=10, textvariable=label_op_var, bg='#6e6e6e', fg='white', text='')
    label_op.grid(row=0, column=3, sticky=E + W)
    # Button 1
    button_1 = Button(root, text='1', width=15, command=button_1)
    button_1.grid(row=1, column=0, sticky=E + W)
    # Button 2
    button_2 = Button(root, text='2', width=15, command=button_2)
    button_2.grid(row=1, column=1, sticky=W + E)
    # Button 3
    button_3 = Button(root, text='3', width=15, command=button_3)
    button_3.grid(row=1, column=2, sticky=W + E)
    # Button 4
    button_4 = Button(root, text='4', width=15, command=button_4)
    button_4.grid(row=2, column=0, sticky=E + W)
    # Button 5
    button_5 = Button(root, text='5', width=15, command=button_5)
    button_5.grid(row=2, column=1, sticky=W + E)
    # Button 6
    button_6 = Button(root, text='6', width=15, command=button_6)
    button_6.grid(row=2, column=2, sticky=W + E)
    # Button 7
    button_7 = Button(root, text='7', width=15, command=button_7)
    button_7.grid(row=3, column=0, sticky=E + W)
    # Button 8
    button_8 = Button(root, text='8', width=15, command=button_8)
    button_8.grid(row=3, column=1, sticky=W + E)
    # Button 9
    button_9 = Button(root, text='9', width=15, command=button_9)
    button_9.grid(row=3, column=2, sticky=W + E)
    # Button 0
    button_0 = Button(root, text='0', width=15, command=button_0)
    button_0.grid(row=4, column=1, sticky=E + W)
    # Button .
    button_point = Button(root, text='.', width=15, bg='#cdeaf9', command=button_point)
    button_point.grid(row=4, column=3, sticky=E + W)
    # Button +
    button_plus = Button(root, text='+', width=15, bg='#cdeaf9', command=button_plus)
    button_plus.grid(row=4, column=0, sticky=E + W)
    # Button -
    button_minus = Button(root, text='-', width=15, bg='#cdeaf9', command=button_minus)
    button_minus.grid(row=4, column=2, sticky=W + E)
    # Button /
    button_div = Button(root, text='/', width=15, bg='#cdeaf9', command=button_div)
    button_div.grid(row=5, column=0, sticky=E + W)
    # Button *
    button_mult = Button(root, text='*', width=15, bg='#cdeaf9', command=button_mult)
    button_mult.grid(row=5, column=1, sticky=E + W)
    # Button =
    button_equal = Button(root, text='=', width=15, bg='#cdeaf9', command=button_equal)
    button_equal.grid(row=5, column=2, sticky=W + E, columnspan=2)
    # Button clear
    button_clear = Button(root, text='clear', width=15, bg='#cdeaf9', command=button_clear)
    button_clear.grid(row=1, column=3, rowspan=3, sticky=W + E + N + S)

    # Loop of the program
    root.mainloop()


# This is the script to play
if __name__ == '__main__':
    main()
