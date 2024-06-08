import streamlit as st
import matplotlib.pyplot as plt


def getinfo(lines, option):
    males = 0
    survived_males = 0
    females = 0
    survived_females = 0
    for line in lines:
        data = line.split(",")
        sex = data[5]
        SibSp = data[7]
        survived = data[1]
        if SibSp == "0" and option == "0":
            if sex == "male":
                males += 1
                if survived == "1":
                    survived_males += 1
            else:
                females += 1
                if survived == "1":
                    survived_females += 1
        elif SibSp == "1" or SibSp == "2" and option == "1-2":
            if sex == "male":
                males += 1
                if survived == "1":
                    survived_males += 1
            else:
                females += 1
                if survived == "1":
                    survived_females += 1
        elif option == "Больше 2":
            if sex == "male":
                males += 1
                if survived == "1":
                    survived_males += 1
            else:
                females += 1
                if survived == "1":
                    survived_females += 1
    maleRate = survived_males / males * 100
    femaleRate = survived_females / females * 100
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
