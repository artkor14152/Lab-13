from var2 import getinfo


def test_all():
    line = [
        '6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,C',
        '6,1,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,C',
        '6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q',
        '6,1,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q',
        '6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,S',
        '6,1,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,S',
    ]
    actual = getinfo(line)
    expected = {"C": 1, "Q": 1, "S": 1}, {"C": 1, "Q": 1, "S": 1}
    assert actual == expected


def test_C():
    line = [
        '17,0,3,"Rice, Master. Eugene",male,2,4,1,382652,29.125,,C',
        '23,1,3,"McGowan, Miss. Anna ""Annie""",female,15,0,0,330923,8.0292,,C',
    ]
    actual = getinfo(line)
    expected = {"C": 1, "Q": 0, "S": 0}, {"C": 1, "Q": 0, "S": 0}
    assert actual == expected


def test_S():
    line = [
        '16,1,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S',
        '16,0,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S',
    ]
    actual = getinfo(line)
    expected = {"C": 0, "Q": 0, "S": 1}, {"C": 0, "Q": 0, "S": 1}
    assert actual == expected


def test_Q():
    line = [
        '17,0,3,"Rice, Master. Eugene",male,2,4,1,382652,29.125,,Q',
        '17,1,3,"Rice, Master. Eugene",male,2,4,1,382652,29.125,,Q',
    ]
    actual = getinfo(line)
    expected = {"C": 0, "Q": 1, "S": 0}, {"C": 0, "Q": 1, "S": 0}
    assert actual == expected
