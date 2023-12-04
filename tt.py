# from tkinter import S
# import streamlit as st


# import tables


#import turtle
#t = turtle.Turtle()
#t.shape("turtle")
#t.speed(1)



#turtle.done()


# st.write('집 가고싶다  ......')
# st.title("집 보내주세요 으헝헝  ......")
# st.image('im.jfif')



#a = 3.141592*10*10.0
#b = (1/100)*1234

#print(a, b)
#a, b


#print('Hello')
#st.write('Hello')
#st.write('강아지'+'고양이')
#st.write('1'+'1')


#r = 20
#area = 3.14*r*r
#area 

#s = 0 #초기값

#for i in range(1, 101, 2):
    #'s = ', s, 'i = ', i
    #s = s + i
    #s += i
#'s + i =', s

#s


# s = 70

# if s >= 90:
#     st.write('귀하의 점수는' + str(s) + '점으로 :blue[A등급]입니다')
# elif s >= 80:
#     '귀하의 점수는' + str(s) + '점으로 :green[B등급]입니다'
# elif s >= 70:
#     '귀하의 점수는' + str(s) + '점으로 :rainbow[C등급]입니다'
# elif s >=60 :
#     '귀하의 점수는' + str(s) + '점으로 :orange[D등급]입니다'
# else:
#     '귀하의 점수는' + str(s) + '점으로 :red[F등급]입니다'


# for i in range(1, 10):
#     if i%3 == 1:
#         i


# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)

# t.width(2)
#turtle.bgcolor('black')

#colors = ['red', 'purple', 'blue', 'yellow', 'orange', 'green']

# length = 5
# for i in range(100):
#     t.forward(length)
#     #t.pencolor(colors[length%6])
#     t.right(45)
#     length += 1
    


# n = 40
# ang = 360/n

# for i in range(n):
#     t.circle(100)
#     t.left(ang)


# turtle.done()




#for i in range(1, 101, 2):
    #'s = ', s, 'i = ', i
    #s = s + i
   # s += i
#'s + i =', s

#s

#for i in range(1, 101):
      #if i % 5 == 2:
        #print(i) 


#def user_sum(n):
    #s = 0 
    #for i in range(1, n+1):
       # s = s + i
    #s

#user_sum(100)
#user_sum(200)




#정사각형 그리기(turtle)

#import turtle
#t = turtle.Turtle()
#t.shape("turtle")
#t.speed(1)



#def square(x, y, length):
 #   t.up()
 #   t.goto(x, y)
  #  t.down()
   # for i in range(4):
    #    t.forward(length)
     #   t.left(90)

#square(-200, 0, 100)
#square(0, 0, 100)
#square(200, 0, 100)


#turtle.done()



#직사각형 그리기(turtle)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)



# def rec(x, y, lx, ly):
#     t.up()
#     t.goto(x, y)
#     t.down()
#     for i in range(2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)

# rec(-200, 0, 100, 50)
# rec(0, 0, 100, 150)
# rec(200, 0, 100, 100)


# turtle.done()



# import streamlit as st
# import time
# import random

# a1 = random.randint(1, 45)
# a1



# import turtle
# import random as r

# screen = turtle.Screen()
# image1 ="토끼.gif"
# image2 = "꼬부기.gif"
# screen.addshape(image1)
# screen.addshape(image2)

# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t1.shape(image1)
# t2.shape(image2)

# t1.penup()
# t1.shapesize(3)
# t1.color("pink")
# t1.goto(-300, 100)
# t1.pensize(3)
# t1.speed(1)

# t2.penup()
# t2.shapesize(3)
# t2.color("blue")
# t2.goto(-300, -100)
# t2.pensize(3)
# t2.speed(1)

# t1.pendown()
# t2.pendown()
# t1.speed(1)
# t2.speed(1)


# for i in range(50):
#     d1 = r.randint(1, 30)
#     t1 .forward(d1)
#     d2 = r.randint(1, 30)
#     t2.forward(d2)


# turtle.done()



# 원 애니메이션 그리기

# import turtle
# import random
# t = turtle.Turtle()

# t.speed(0)
# t.pensize(5)
# t.goto(0,0)
# while True:
#     for i in range(30):
#         t.circle(1+5*i)
#         t.color((random.random(),random.random(),random.random()))
#         t.goto(i*20, 0)
#     t.clear()
        

# turtle.done()



# 색깔 바꾸기

# import turtle

# t = turtle.Turtle()
# t.shape('turtle')
# t.color(77/255, 239/255, 93/255)

# t.forward(100)

# turtle.done()




# 사각형 애니메이션 그리기

# import turtle
# import random
# t = turtle.Turtle()

# t.speed(0)
# t.pensize(5)
# t.goto(0,0)
# while True:
#     for i in range(30):
#         t.forward(1+5*i)
#         t.left(90)
#         t.forward(1+5*i)
#         t.left(90)
#         t.forward(1+5*i)
#         t.left(90)
#         t.forward(1+5*i)
#         t.left(90)
#         t.color((random.random(),random.random(),random.random()))
#         t.goto(i*10, 0)
#     t.clear

# turtle.done()




# 3,4,5각형 애니메이션 그리기

# import turtle
# import random
# t = turtle.Turtle()
# t.shape('turtle')

# t.forward(100)

# def shape(sh):
#     for j in range(sh):
#         t.forward(1 + 5*i)
#         t.left(360/sh)


# t.speed()
# t.pensize(5)
# t.goto(0,0)
# while True:
#     for i in range(30):
#         if i < 10:
#             shape(3)
#         elif i < 20:
#             shape(4)
#         elif i < 25:
#             shape(5)
#         elif i < 30:
#             t.circle(i + 5*i)
#         t.color((random.random(),random.random(),random.random()))
#         t.goto(i*20, 0)
#     t.clear()

# turtle.done()





#  나무 그리기

# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)
# t.goto(0, -200)

# def tree(length):
#     if length > 5:
#         t.forward(length)
#         t.right(20)
#         tree(length-10)
#         t.left(40)
#         tree(length-10)
#         t.right(20)
#         t.backward(length)

# t.left(90)

# t. color("green")
# tree(90)

# turtle.done()


# 최대값 구하는 코드
# 최소값 구할 경우 > 를 < 로 바꾸기

# import streamlit as st
# import time
# import random as r


# s = [3, 7, 1, 9, -3, 3, 10]
# s

# mx = -1e10
# for i in s:
#     if i > mx:
#         mx = i
# mx



# import streamlit as st
# import time
# import random as r
# import numpy as np

# s = [3, 7, 1, 9, -3, 3, 10]
# S
# a = np.sort(s)
# a1= np.std(s)



# s = ['a', 'b', 'c', 'd', 'e']

# s.append('사과')
# s.remove('c')
# S
# i = s.index('d')
# i


# 리스트로 그래프 그리기

# import streamlit as st
# import random
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1,10))


# # numbers
# plt.plot(numbers)
# plt.ylabel('some random numbers')
# plt.xlabel('x-axis')

# st.pyplot(fig)




# import streamlit as st
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# x = []
# for i in range(-100, 101):
#     x.append(i/10.0)

# col = st.columns(3)
# with col[0]:
#     a = st.number_input('Insert a', step = 1)
# with col[1]:
#     b = st.number_input('Insert b', step = 1)
# with col[2]:
#     c = st.number_input('Insert c', step = 1)

# y = []
# for i in x:
#     y.append(a*i**2 + b*i + c)

# plt.plot(x, y)

# st.pyplot(fig)


# import streamlit as st


# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

# st.dataframe(df)  # Same as st.write(df)

# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")

# st.write('# :green[**Hello**], 👻 *World!* :sunglasses:')
# st.write('## :blue[**Hello**], 👻 *World!* :sunglasses:')
# st.write('### :red[**Hello**], 👻 *World!* :sunglasses:')
# st.write('#### :orange[**Hello**], 👻 *World!* :sunglasses:')
# st.write('##### **Hello**, 👻 *World!* :sunglasses:')
# st.write('###### **Hello**, 👻 *World!* :sunglasses:')

# st.markdown("*Streamlit* is **really** ***cool***.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')
# st.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.
# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

col1, col2, col3 = st.columns(3)

with col1:
    c1 = st.sidebar.radio('선의 색을 선택하시오.',['red','green','blue', 'orange'])
with col2:
    s1 = st.sidebar.radio('선의 형태를 선택하시오.',['-',':','-.', '--'])
with col3:
    a1 = st.sidebar.radio('마커의 형태를 선택하시오.',['o','^','s', 'p', 'h'])


fig, ax = plt.subplots()

x = []
y = []
for i in range(-20, 21, 2):
    x.append(i)
    y.append(-2*i*i + 3*i + 5)

#위아래 둘다 결과 값은 같음(간단하게 표현할 때는 1번, 꾸미거나 라디오 버튼 쓸 때는 2번이 유용함)
#plt.plot(x, y, 'r:p')
plt.plot(x, y, color = c1, linestyle = s1, marker = a1)

st.pyplot(fig)


#  append=덧 붙이기

#밑에 있는 코딩은 코딩 밑에 있는 명령어를 읽지 않겠다는 뜻. 즉, 주석.
import sys
sys.exit()


x = []
y = []
ysin = []                                                                              
for i in range(-20,21,1):
    x. append(i)
    y.append(3*i*i - 5*i + 2)
    ysin.append(1200*np.sin(i))

plt.plot(x,y,color=c1,label='2nd Equation')
plt.plot(x,ysin,color=c1,label='sin Function')
plt.plot('x-asin')
plt.plot('x-ysin')
plt.xlim([-15,15])
plt.ylim([-2000,2000])
plt.legend()
st.pyplot(fig)