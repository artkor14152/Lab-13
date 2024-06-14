import streamlit as st
import matplotlib.pyplot as plt


def getinfo(lines):
    survived = {"C": 0, "Q": 0, "S": 0}
    notSurvived = {"C": 0, "Q": 0, "S": 0}
    for line in lines:
        data = line.split(",")
        isSurvived = data[1]
        port = data[12].strip()
        if port != "":
            if isSurvived == "1":
                survived[port] += 1
            else:
                notSurvived[port] += 1
    return survived, notSurvived


def var2():
    st.title("Подсчитать число спасенных и погибших для указанного пункта посадки.")
    option = st.selectbox(
        "Выбирете пункт посадки ", ["Шербур", "Квинстоун", "Саутгемптон"]
    )
    with open("data.csv") as f:
        next(f)
        survived, notSurvived = getinfo(f.readlines())
        convert = {"Шербур": "C", "Квинстоун": "Q", "Саутгемптон": "S"}
        st.table(
            {
                "Спасённых": survived[convert[option]],
                "Погибших": notSurvived[convert[option]],
            }
        )
        fig = plt.figure(figsize=(10, 5))
        plt.xlabel("Значение поля Survived")
        plt.ylabel("Количество")
        plt.title("Количество спасённых и погибших в " + option)
        plt.bar(
            ["Спасённых", "Погибших"],
            [survived[convert[option]], notSurvived[convert[option]]],
        )
        st.pyplot(fig)
