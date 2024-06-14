import streamlit as st
import matplotlib.pyplot as plt


def getinfo(lines, option):
    count = {"male": 0, "female": 0}
    survived = {"male": 0, "female": 0}
    for line in lines:
        data = line.split(",")
        sex = data[5]
        SibSp = int(data[7])
        isSurvived = data[1]
        if sex == "male":
            count["male"] += 1
        else:
            count["female"] += 1
        if isSurvived == "1":
            if (
                (SibSp == 0 and option == "0")
                or (SibSp == 1 and option == "1-2")
                or (SibSp > 1 and option == "Больше 2")
            ):
                survived[sex] += 1

    maleRate = survived["male"] / count["male"] * 100
    femaleRate = survived["female"] / count["female"] * 100
    return maleRate, femaleRate


def var5():
    st.title(
        "Вычислить долю выживших среди мужчин и женщин, выбрав количество братьев, сестер... "
    )
    with open("data.csv") as f:
        option = st.selectbox(
            "Выбирете количество братьев или сестер", ["0", "1-2", "Больше 2"]
        )
        next(f)
        maleRate, femaleRate = getinfo(f.readlines(), option)
        st.table(
            {"Пол": ["Мужчины", "Женщины"], "Процент выживших": [maleRate, femaleRate]}
        )
        fig = plt.figure(figsize=(10, 5))
        plt.xlabel("Пол")
        plt.ylabel("Процент")
        plt.title("Распределение выживших")
        plt.bar(["Мужчины", "Женщины"], [maleRate, femaleRate])
        st.pyplot(fig)
