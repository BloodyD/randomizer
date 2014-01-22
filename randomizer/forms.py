#coding: utf-8

from django import forms
from randomizer import NAMES, NATIONS

def to_choice(l):
  res = []
  i = 0
  for val in l:
    res.append([i, val])
    i += 1

  return res

class MainForm(forms.Form):
  names = forms.ChoiceField(label= "Namen", choices=to_choice(NAMES))
  nations = forms.ChoiceField(label= "Völker", choices=to_choice(NATIONS))
  test = forms.BooleanField(label= "test", )