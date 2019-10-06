# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/10/6 14:48
# @File     : fuzzy_set.py
# @Software : PyCharm


import _tkinter
import tkinter
from numpy import *

root = tkinter.Tk()
frm1 = tkinter.LabelFrame(root, text="计算模糊规则（从A到B）", padx=40,pady=30)
frm2 = tkinter.LabelFrame(root, text="输入事实并得到结论", padx=40,pady=30)
frm1.pack()
frm2.pack()
root.title("模糊推理")

def CFRM():
	LSD1 = v1.get().split(',')
	LSD2 = v2.get().split(',')
	i = -1
	j = -1
	for x in LSD1:
		i = i +1
		LSD1[i] = float(LSD1[i])
	for x in LSD2:
		j = j +1
		LSD2[j] = float(LSD2[j])
	global FRM
	FRM = mat(zeros((len(LSD1),len(LSD1))))
	i = 0
	while i < len(LSD1):
		j = 0
		while j < len(LSD1):
			FRM[i,j] = max([min([LSD1[i],LSD2[j]]),1-LSD1[i]])
			j = j + 1
		i = i +1
	print(FRM)
	t = tkinter.Text(frm1,width=30,height=5)
	t.grid(row=2,column=1)
	t.insert(tkinter.END, FRM)

def CD():
	global FRM
	LSD3 = v3.get().split(',')
	i = -1
	for x in LSD3:
		i = i +1
		LSD3[i] = float(LSD3[i])
	D = mat(zeros((1,len(LSD3))))
	i = 0
	while i < len(LSD3):
		j = 0
		while j < len(LSD3):
			D[0,i] = max(min([FRM[j,i],LSD3[j]]),D[0,j])
			j = j + 1
		i = i + 1
	v4.set(D[0])


v1 = tkinter.StringVar()
v2 = tkinter.StringVar()
v3 = tkinter.StringVar()
v4 = tkinter.StringVar()
tkinter.Label(frm1,text="输入A:").grid(row=0,column=0)
tkinter.Label(frm1,text="输入B:").grid(row=1,column=0)
# tkinter.Label(frm1,text="计算模糊关系矩阵").grid(row=2,column=0)
tkinter.Button(frm1, text="计算模糊关系矩阵", font=('Arial', 9), width=16, height=1, command=CFRM).grid(row=2,column=0)
tkinter.Label(frm2,text="输入A':").grid(row=3,column=0)
tkinter.Button(frm2,text="输入B':",command=CD).grid(row=4,column=0)
e1 = tkinter.Entry(frm1,textvariable=v1).grid(row=0,column=1,padx=10,pady=10)
e2 = tkinter.Entry(frm1,textvariable=v2).grid(row=1,column=1,padx=10,pady=10)
e3 = tkinter.Entry(frm1,textvariable=v2,width=30).grid(row=2,column=1,padx=10,pady=10)
e4 = tkinter.Entry(frm2,textvariable=v3).grid(row=3,column=1,padx=10,pady=10)
e5 = tkinter.Entry(frm2,textvariable=v4).grid(row=4,column=1,padx=10,pady=10)
root.mainloop()

