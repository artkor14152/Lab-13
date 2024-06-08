from var5 import getinfo


def test_1():
    line = [
        '6,1,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q',
        '11,1,3,"Sandstrom, Miss. Marguerite Rut",female,4,1,1,PP 9549,16.7,G6,S',
    ]
    actual = getinfo(line, "0")
    expected = (100.0, 100.0)
    assert actual == expected


def test_2():
    line = [
        '21,0,2,"Fynney, Mr. Joseph J",male,35,1,0,239865,26,,S',
        '22,1,2,"Beesley, Mr. Lawrence",male,34,1,0,248698,13,D56,S',
        '23,1,3,"McGowan, Miss. Anna ""Annie""",female,15,1,0,330923,8.0292,,Q',
        '23,0,3,"McGowan, Miss. Anna ""Annie""",female,15,1,0,330923,8.0292,,Q',
    ]
    actual = getinfo(line, "1-2")
    expected = (50.0, 50.0)
    assert actual == expected


def test_3():
    line = [
        '19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S',
        '20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C',
        '21,0,2,"Fynney, Mr. Joseph J",male,35,0,0,239865,26,,S',
        '22,1,2,"Beesley, Mr. Lawrence",male,34,0,0,248698,13,D56,S',
    ]
    actual = getinfo(line, "Больше 2")
    expected = (50.0, 50.0)
    assert actual == expected
