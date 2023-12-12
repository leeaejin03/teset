import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()


a = st.number_input('a의 값을 입력하시오', value = 2.0, step = 1.0)
b = st.number_input('b의 값을 입력하시오', value = -1.0, step = 1.0)
c = st.number_input('c의 값을 입력하시오', value  =15.0, step = 1.0)
d = st.number_input('d의 값을 입력하시오', value = 2000.0, step = 100.0)



x = []
y1 = []
y2 = []


for i in range(-29, 31, 3):
     x.append(i)
     y1.append(a*i*i + b*i + c)
     y2.append(d/i)


col1, col2, col3 = st.columns(3)

with col1:
    c1 = st.sidebar.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
with col2:
    l1 = st.sidebar.radio('선의 형태를 선택하시오', ['-', ':', '-.', '--'])
with col3:
    m1 = st.sidebar.radio('마커의 형태를 선택하시오', ['o', '^', 's', 'p', 'h'])



plt.legend()
plt.plot(x, y1, color = c1, linestyle = l1, marker = m1)
plt.plot(x, y2, color = c1, linestyle = l1, marker = m1)



st.pyplot(fig)