import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

fig, ax = plt.subplots()

col1, col2, col3 = st.columns(3)

with col1:
    c1 = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
with col2:
    l1 = st.radio('선의 형태를 선택하시오', ['-', ':', '-.', '--'])
with col3:
    m1 = st.radio('마커의 형태를 선택하시오', ['o', '^', 's', 'p', 'h'])


x = []
y = []
ysin = []

for i in range(-20, 21, 5):
    x.append(i)
    y.append(3*i*i - 5*i + 2)
    ysin.append(1200*np.sin(i))

plt.plot(x, y, 'go--', label = '2nd Equation')
plt.plot(x, ysin, 'rs:', label = 'sin Function')
plt.legend()
plt.plot(x, y, color = c1, linestyle = l1, marker = m1)

st.pyplot(fig)