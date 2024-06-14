from var5 import getinfo


def test_sb0():
    line = [
        '6,1,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q',
        '11,1,3,"Sandstrom, Miss. Marguerite Rut",female,4,0,1,PP 9549,16.7,G6,S',
    ]
    actual = getinfo(line, "0")
    expected = (100.0, 100.0)
    assert actual == expected


def test_sb1_2():
    line = [
        '6,1,3,"Moran, Mr. James",male,,1,1,330877,8.4583,,Q',
        '11,1,3,"Sandstrom, Miss. Marguerite Rut",female,1,1,1,PP 9549,16.7,G6,S',
    ]
    actual = getinfo(line, "1-2")
    expected = (100.0, 100.0)
    assert actual == expected


def test_sbMore2():
    line = [
        '6,1,3,"Moran, Mr. James",male,,3,1,330877,8.4583,,Q',
        '11,1,3,"Sandstrom, Miss. Marguerite Rut",female,1,3,1,PP 9549,16.7,G6,S',
    ]
    actual = getinfo(line, "Больше 2")
    expected = (100.0, 100.0)
    assert actual == expected
