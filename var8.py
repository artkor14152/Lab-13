import streamlit as st
import matplotlib.pyplot as plt


def getinfo(lines, choise):
    data = {"мужчин:": 0, "женщин:": 0}
    for line in lines:
        d = line.split(",")
        gender = d[5]
        pclass = d[2]
        if choise == "1 класс" and pclass == "1":
            if gender == "male":
                data["мужчин:"] += 1
            else:
                data["женщин:"] += 1
        if choise == "2 класс" and pclass == "2":
            if gender == "male":
                data["мужчин:"] += 1
            else:
                data["женщин:"] += 1
        if choise == "3 класс" and pclass == "3":
            if gender == "male":
                data["мужчин:"] += 1
            else:
                data["женщин:"] += 1
    return data


def var8():
    st.title(
        "Найти количество пассажиров каждого пола по указанному классу обслуживания"
    )
    choise = st.selectbox("укажите пол:", ["1 класс", "2 класс", "3 класс"])
    info = {"мужчин:": 0, "женщин:": 0}
    with open("data.csv") as file:
        info = getinfo(file.readlines(), choise)
    st.dataframe(info)
    fig = plt.figure(figsize=(10, 5))
    plt.bar(["мужчин", "женщин"], [info["мужчин:"], info["женщин:"]])
    st.pyplot(fig)
