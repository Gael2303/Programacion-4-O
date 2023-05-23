import streamlit as st
import pandas as pd
import numpy as np

st.title('_Curvas de Titulación_')

option = st.selectbox(
  'Selecciona el tipo de curva',
  ('Acido-Base (Fuertes)', 'Base-Acido (Fuertes)', 'Experimental'))

if option == 'Acido-Base (Fuertes)':
  
  CA = st.text_input("Ingresa la concentración del _analito_:", value=" ")
  VA = st.text_input("Ingresa volumen del _analito_:", value=" ")
  CT = st.text_input("Ingresa la concentración del _titulante_:", value=" ")
  
  volumen = st.radio(
    '¿Cuantos volumenes requieres?',
    ('5', '6', '7', '8', '9', '10'))
  if volumen == '5':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e], y='pH')
      
  elif volumen == '6':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f], y='pH')
      
  elif volumen == '7':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      g= st.text_input("Ingresa volumen 7:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      mT7 = np.multiply(float(CT), float(g))
      if mT7<mA:
        C7= (float(mA)-float(mT7))/(float(VA)+float(g))
        ph7= np.log10(float(C7))*-1
      elif mT7==mA:
        ph7=7
      elif mT7>mA:
        C7= (float(mT7)-float(mA))/(float(VA)+float(g))
        ph7= 14+np.log10(float(C7))
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f, g], y='pH')
      
  elif volumen == '8':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      g= st.text_input("Ingresa volumen 7:", value=" ")
      h= st.text_input("Ingresa volumen 8:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      mT7 = np.multiply(float(CT), float(g))
      if mT7<mA:
        C7= (float(mA)-float(mT7))/(float(VA)+float(g))
        ph7= np.log10(float(C7))*-1
      elif mT7==mA:
        ph7=7
      elif mT7>mA:
        C7= (float(mT7)-float(mA))/(float(VA)+float(g))
        ph7= 14+np.log10(float(C7))
      mT8 = np.multiply(float(CT), float(h))
      if mT8<mA:
        C8= (float(mA)-float(mT8))/(float(VA)+float(h))
        ph8= np.log10(float(C8))*-1
      elif mT8==mA:
        ph8=7
      elif mT8>mA:
        C8= (float(mT8)-float(mA))/(float(VA)+float(h))
        ph8= 14+np.log10(float(C8))
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g, h], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2), np.round(ph8, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7", "Lab 8"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f, g, h], y='pH')
      
  elif volumen == '9':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      g= st.text_input("Ingresa volumen 7:", value=" ")
      h= st.text_input("Ingresa volumen 8:", value=" ")
      i= st.text_input("Ingresa volumen 9:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      mT7 = np.multiply(float(CT), float(g))
      if mT7<mA:
        C7= (float(mA)-float(mT7))/(float(VA)+float(g))
        ph7= np.log10(float(C7))*-1
      elif mT7==mA:
        ph7=7
      elif mT7>mA:
        C7= (float(mT7)-float(mA))/(float(VA)+float(g))
        ph7= 14+np.log10(float(C7))
      mT8 = np.multiply(float(CT), float(h))
      if mT8<mA:
        C8= (float(mA)-float(mT8))/(float(VA)+float(h))
        ph8= np.log10(float(C8))*-1
      elif mT8==mA:
        ph8=7
      elif mT8>mA:
        C8= (float(mT8)-float(mA))/(float(VA)+float(h))
        ph8= 14+np.log10(float(C8))
      mT9 = np.multiply(float(CT), float(i))
      if mT9<mA:
        C9= (float(mA)-float(mT9))/(float(VA)+float(i))
        ph9= np.log10(float(C9))*-1
      elif mT9==mA:
        ph9=7
      elif mT9>mA:
        C9= (float(mT9)-float(mA))/(float(VA)+float(i))
        ph9= 14+np.log10(float(C9))
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g, h, i], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2), np.round(ph8, 2), np.round(ph9, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7", "Lab 8", "Lab 9"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f, g, h, i], y='pH')
      
  elif volumen == '10':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      g= st.text_input("Ingresa volumen 7:", value=" ")
      h= st.text_input("Ingresa volumen 8:", value=" ")
      i= st.text_input("Ingresa volumen 9:", value=" ")
      j= st.text_input("Ingresa volumen 10:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      mT7 = np.multiply(float(CT), float(g))
      if mT7<mA:
        C7= (float(mA)-float(mT7))/(float(VA)+float(g))
        ph7= np.log10(float(C7))*-1
      elif mT7==mA:
        ph7=7
      elif mT7>mA:
        C7= (float(mT7)-float(mA))/(float(VA)+float(g))
        ph7= 14+np.log10(float(C7))
      mT8 = np.multiply(float(CT), float(h))
      if mT8<mA:
        C8= (float(mA)-float(mT8))/(float(VA)+float(h))
        ph8= np.log10(float(C8))*-1
      elif mT8==mA:
        ph8=7
      elif mT8>mA:
        C8= (float(mT8)-float(mA))/(float(VA)+float(h))
        ph8= 14+np.log10(float(C8))
      mT9 = np.multiply(float(CT), float(i))
      if mT9<mA:
        C9= (float(mA)-float(mT9))/(float(VA)+float(i))
        ph9= np.log10(float(C9))*-1
      elif mT9==mA:
        ph9=7
      elif mT9>mA:
        C9= (float(mT9)-float(mA))/(float(VA)+float(i))
        ph9= 14+np.log10(float(C9))
      mT10 = np.multiply(float(CT), float(j))
      if mT10<mA:
        C10= (float(mA)-float(mT10))/(float(VA)+float(j))
        ph10= np.log10(float(C10))*-1
      elif mT10==mA:
        ph10=7
      elif mT10>mA:
        C10= (float(mT10)-float(mA))/(float(VA)+float(j))
        ph10= 14+np.log10(float(C10))
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g, h, i, j], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2), np.round(ph8, 2), np.round(ph9, 2), np.round(ph10, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7", "Lab 8", "Lab 9", "Lab "])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f, g, h, i, j], y='pH')
      
st.write("Made by Fernando Aguilera, Andrés Fernández y Gael Arámbula")
elif option == 'Base-Acido (Fuertes)':
  
  CA = st.text_input("Ingresa la concentración del _analito_:", value=" ")
  VA = st.text_input("Ingresa volumen del _analito_:", value=" ")
  CT = st.text_input("Ingresa la concentración del _titulante_:", value=" ")
  
  volumen = st.radio(
    '¿Cuantos volumenes requieres?',
    ('5', '6', '7', '8', '9', '10'))
  if volumen == '5':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))-1
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e], y='pH')
      
  elif volumen == '6':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f], y='pH')
      
  elif volumen == '7':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      g= st.text_input("Ingresa volumen 7:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      mT7 = np.multiply(float(CT), float(g))
      if mT7<mA:
        C7= (float(mA)-float(mT7))/(float(VA)+float(g))
        ph7= 14+np.log10(float(C7))
      elif mT7==mA:
        ph7=7
      elif mT7>mA:
        C7= (float(mT7)-float(mA))/(float(VA)+float(g))
        ph7= np.log10(float(C7))*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f, g], y='pH')
      
  elif volumen == '8':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      g= st.text_input("Ingresa volumen 7:", value=" ")
      h= st.text_input("Ingresa volumen 8:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      mT7 = np.multiply(float(CT), float(g))
      if mT7<mA:
        C7= (float(mA)-float(mT7))/(float(VA)+float(g))
        ph7= 14+np.log10(float(C7))
      elif mT7==mA:
        ph7=7
      elif mT7>mA:
        C7= (float(mT7)-float(mA))/(float(VA)+float(g))
        ph7= np.log10(float(C7))*-1
      mT8 = np.multiply(float(CT), float(h))
      if mT8<mA:
        C8= (float(mA)-float(mT8))/(float(VA)+float(h))
        ph8= np.log10(float(C8))*-1
      elif mT8==mA:
        ph8=7
      elif mT8>mA:
        C8= (float(mT8)-float(mA))/(float(VA)+float(h))
        ph8= np.log10(float(C8))*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g, h], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2), np.round(ph8, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7", "Lab 8"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f, g, h], y='pH')
      
  elif volumen == '9':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      g= st.text_input("Ingresa volumen 7:", value=" ")
      h= st.text_input("Ingresa volumen 8:", value=" ")
      i= st.text_input("Ingresa volumen 9:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      mT7 = np.multiply(float(CT), float(g))
      if mT7<mA:
        C7= (float(mA)-float(mT7))/(float(VA)+float(g))
        ph7= 14+np.log10(float(C7))
      elif mT7==mA:
        ph7=7
      elif mT7>mA:
        C7= (float(mT7)-float(mA))/(float(VA)+float(g))
        ph7= np.log10(float(C7))*-1
      mT8 = np.multiply(float(CT), float(h))
      if mT8<mA:
        C8= (float(mA)-float(mT8))/(float(VA)+float(h))
        ph8= np.log10(float(C8))*-1
      elif mT8==mA:
        ph8=7
      elif mT8>mA:
        C8= (float(mT8)-float(mA))/(float(VA)+float(h))
        ph8= np.log10(float(C8))*-1
      mT9 = np.multiply(float(CT), float(i))
      if mT9<mA:
        C9= (float(mA)-float(mT9))/(float(VA)+float(i))
        ph9= 14+np.log10(float(C9))
      elif mT9==mA:
        ph9=7
      elif mT9>mA:
        C9= (float(mT9)-float(mA))/(float(VA)+float(i))
        ph9= np.log10(float(C9))*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g, h, i], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2), np.round(ph8, 2), np.round(ph9, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7", "Lab 8", "Lab 9"])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f, g, h, i], y='pH')
      
  elif volumen == '10':
      a= st.text_input("Ingresa volumen 1:", value=" ")
      b= st.text_input("Ingresa volumen 2:", value=" ")
      c= st.text_input("Ingresa volumen 3:", value=" ")
      d= st.text_input("Ingresa volumen 4:", value=" ")
      e= st.text_input("Ingresa volumen 5:", value=" ")
      f= st.text_input("Ingresa volumen 6:", value=" ")
      g= st.text_input("Ingresa volumen 7:", value=" ")
      h= st.text_input("Ingresa volumen 8:", value=" ")
      i= st.text_input("Ingresa volumen 9:", value=" ")
      j= st.text_input("Ingresa volumen 10:", value=" ")
      
      mA = np.multiply(float(CA), float(VA))
      mT1 = np.multiply(float(CT), float(a))
      if mT1<mA:
        C1= (float(mA)-float(mT1))/(float(VA)+float(a))
        ph1= 14+np.log10(float(C1))
      elif mT1==mA:
        ph1=7
      elif mT1>mA:
        C1= (float(mT1)-float(mA))/(float(VA)+float(a))
        ph1= np.log10(float(C1))*-1
      mT2 = np.multiply(float(CT), float(b))
      if mT2<mA:
        C2= (float(mA)-float(mT2))/(float(VA)+float(b))
        ph2= 14+np.log10(float(C2))
      elif mT2==mA:
        ph2=7
      elif mT2>mA:
        C2= (float(mT2)-float(mA))/(float(VA)+float(b))
        ph2= np.log10(float(C2))*-1
      mT3 = np.multiply(float(CT), float(c))
      if mT3<mA:
        C3= (float(mA)-float(mT3))/(float(VA)+float(c))
        ph3= 14+np.log10(float(C3))
      elif mT3==mA:
        ph3=7
      elif mT3>mA:
        C3= (float(mT3)-float(mA))/(float(VA)+float(c))
        ph3= np.log10(float(C3))*-1
      mT4 = np.multiply(float(CT), float(d))
      if mT4<mA:
        C4= (float(mA)-float(mT4))/(float(VA)+float(d))
        ph4= 14+np.log10(float(C4))
      elif mT4==mA:
        ph4=7
      elif mT4>mA:
        C4= (float(mT4)-float(mA))/(float(VA)+float(d))
        ph4= np.log10(float(C4))*-1
      mT5 = np.multiply(float(CT), float(e))
      if mT5<mA:
        C5= (float(mA)-float(mT5))/(float(VA)+float(e))
        ph5= 14+np.log10(float(C5))
      elif mT5==mA:
        ph5=7
      elif mT5>mA:
        C5= (float(mT5)-float(mA))/(float(VA)+float(e))
        ph5= np.log10(float(C5))*-1
      mT6 = np.multiply(float(CT), float(f))
      if mT6<mA:
        C6= (float(mA)-float(mT6))/(float(VA)+float(f))
        ph6= 14+np.log10(float(C6))
      elif mT6==mA:
        ph6=7
      elif mT6>mA:
        C6= (float(mT6)-float(mA))/(float(VA)+float(f))
        ph6= np.log10(float(C6))*-1
      mT7 = np.multiply(float(CT), float(g))
      if mT7<mA:
        C7= (float(mA)-float(mT7))/(float(VA)+float(g))
        ph7= 14+np.log10(float(C7))
      elif mT7==mA:
        ph7=7
      elif mT7>mA:
        C7= (float(mT7)-float(mA))/(float(VA)+float(g))
        ph7= np.log10(float(C7))*-1
      mT8 = np.multiply(float(CT), float(h))
      if mT8<mA:
        C8= (float(mA)-float(mT8))/(float(VA)+float(h))
        ph8= np.log10(float(C8))*-1
      elif mT8==mA:
        ph8=7
      elif mT8>mA:
        C8= (float(mT8)-float(mA))/(float(VA)+float(h))
        ph8= np.log10(float(C8))*-1
      mT9 = np.multiply(float(CT), float(i))
      if mT9<mA:
        C9= (float(mA)-float(mT9))/(float(VA)+float(i))
        ph9= 14+np.log10(float(C9))
      elif mT9==mA:
        ph9=7
      elif mT9>mA:
        C9= (float(mT9)-float(mA))/(float(VA)+float(i))
        ph9= np.log10(float(C9))*-1
      mT10 = np.multiply(float(CT), float(j))
      if mT10<mA:
        C10= (float(mA)-float(mT10))/(float(VA)+float(j))
        ph10= 14+np.log10(float(C10))
      elif mT10==mA:
        ph10=7
      elif mT10>mA:
        C10= (float(mT10)-float(mA))/(float(VA)+float(j))
        ph10= np.log10(float(C10))*-1
      
      datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g, h, i, j], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2), np.round(ph8, 2), np.round(ph9, 2), np.round(ph10, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7", "Lab 8", "Lab 9", "Lab "])
      datos
      
      st.line_chart(datos, x=[a, b, c, d, e, f, g, h, i, j], y='pH')

st.write("Made by Fernando Aguilera, Andrés Fernández y Gael Arámbula")
  
elif option == 'Experimental':
  ph1=float(st.text_input('Ingresa el primer pH:', value=' '))
  ph2=float(st.text_input('Ingresa el segundo pH:', value=' '))
  ph3=float(st.text_input('Ingresa el tercer pH:', value=' '))
  ph4=float(st.text_input('Ingresa el cuarto pH:', value=' '))
  ph5=float(st.text_input('Ingresa el quinto pH:', value=' '))
  ph6=float(st.text_input('Ingresa el sexto pH:', value=' '))
  ph7=float(st.text_input('Ingresa el septimo pH:', value=' '))

  a= float(st.text_input("Ingresa volumen 1:", value=" "))
  b= float(st.text_input("Ingresa volumen 2:", value=" "))
  c= float(st.text_input("Ingresa volumen 3:", value=" "))
  d= float(st.text_input("Ingresa volumen 4:", value=" "))
  e= float(st.text_input("Ingresa volumen 5:", value=" "))
  f= float(st.text_input("Ingresa volumen 6:", value=" "))
  g= float(st.text_input("Ingresa volumen 7:", value=" "))
      
  datos=pd.DataFrame({'Volumen': [a, b, c, d, e, f, g], 'pH':[np.round(ph1, 2), np.round(ph2, 2), np.round(ph3, 2), np.round(ph4, 2), np.round(ph5, 2), np.round(ph6, 2), np.round(ph7, 2)]}, index=["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7"])
  datos
  st.line_chart(datos, x=[a, b, c, d, e, f, g], y='pH')
  
st.write("Made by Fernando Aguilera, Andrés Fernández y Gael Arámbula")
