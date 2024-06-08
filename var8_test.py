from var8 import getinfo


def test_male():
    testline = '1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S'
    actual = getinfo([testline], "3 класс")
    expected = {"мужчин:": 1, "женщин:": 0}
    assert expected == actual


def test_female():
    testline = '11,1,3,"Sandstrom, Miss. Marguerite Rut",female,4,1,1,PP 9549,16.7,G6,S'
    actual = getinfo([testline], "3 класс")
    expected = {"мужчин:": 0, "женщин:": 1}
    assert expected == actual


def test_multiline():
    testline = [
        '19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S',
        '20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C',
        '21,0,2,"Fynney, Mr. Joseph J",male,35,0,0,239865,26,,S',
        '22,1,2,"Beesley, Mr. Lawrence",male,34,0,0,248698,13,D56,S',
        '23,1,3,"McGowan, Miss. Anna ""Annie""",female,15,0,0,330923,8.0292,,Q',
    ]
    actual = getinfo(testline, "3 класс")
    expected = {"мужчин:": 0, "женщин:": 3}
    assert expected == actual


def test_multiline2():
    testline = [
        '19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S',
        '20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C',
        '21,0,2,"Fynney, Mr. Joseph J",male,35,0,0,239865,26,,S',
        '22,1,2,"Beesley, Mr. Lawrence",male,34,0,0,248698,13,D56,S',
        '23,1,3,"McGowan, Miss. Anna ""Annie""",female,15,0,0,330923,8.0292,,Q',
    ]
    actual = getinfo(testline, "2 класс")
    expected = {"мужчин:": 2, "женщин:": 0}
    assert expected == actual
