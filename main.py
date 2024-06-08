import streamlit as st
from var8 import var8
from var2 import var2
from var5 import var5
from var19 import var19
st.title('Статистика по Титанику')
variant = st.selectbox('выбрать вариант', ['8', '2', '5', '19'])
if variant == '8':
    var8()
if variant == '2':
    var2()
if variant == '5':
    var5()
if variant == '19':
    var19()
