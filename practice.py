import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

c1 = st.sidebar.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
l1 = st.sidebar.radio('선의 형태를 선택하시오', ['-', ':', '-.', '--'])
m1 = st.sidebar.radio('마커의 형태를 선택하시오', ['o', '^', 's', 'p', 'h'])

x = []
y = []

for i in range(-20, 21, 3):
    x.append(i)
    y.append(-2*i*i + 3*i + 5)


plt.plot(x, y, color = c1, linestyle = l1, markerstyle = m1)

st.pyplot(fig)