# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZoZ5hp5iuXMWINFaThHeukZhRjvWo3SQ
"""

l=[]
user_list = [int(x) for x in input("Enter elements separated by space:").split()]
print(user_list)
for i in user_list:
  i=int(i)
  if i>0:
    l.append(i)
print(l)