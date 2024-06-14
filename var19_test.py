from var19 import getSurvivedCount


def test_S15():
    line = [
        '13,0,3,"Saundercock, Mr. William Henry",male,5,0,0,A/5. 2151,8.05,,S',
        '13,0,3,"Saundercock, Mr. William Henry",male,10,0,0,A/5. 2151,8.05,,S',
        '13,0,3,"Saundercock, Mr. William Henry",male,20,0,0,A/5. 2151,8.05,,S',
        '13,0,3,"Saundercock, Mr. William Henry",male,25,0,0,A/5. 2151,8.05,,S',
    ]
    actual = getSurvivedCount(line, 15.0)
    expected = (0, 0, 2)
    assert actual == expected


def test_Q22():
    line = [
        '13,0,3,"Saundercock, Mr. William Henry",male,5,0,0,A/5. 2151,8.05,,Q',
        '13,0,3,"Saundercock, Mr. William Henry",male,10,0,0,A/5. 2151,8.05,,Q',
        '13,0,3,"Saundercock, Mr. William Henry",male,20,0,0,A/5. 2151,8.05,,Q',
        '13,0,3,"Saundercock, Mr. William Henry",male,25,0,0,A/5. 2151,8.05,,Q',
    ]
    actual = getSurvivedCount(line, 22.0)
    expected = (0, 1, 0)
    assert actual == expected


def test_C30():
    line = [
        '13,0,3,"Saundercock, Mr. William Henry",male,5,0,0,A/5. 2151,8.05,,C',
        '13,0,3,"Saundercock, Mr. William Henry",male,10,0,0,A/5. 2151,8.05,,C',
        '13,0,3,"Saundercock, Mr. William Henry",male,20,0,0,A/5. 2151,8.05,,C',
        '13,0,3,"Saundercock, Mr. William Henry",male,25,0,0,A/5. 2151,8.05,,C',
    ]
    actual = getSurvivedCount(line, 30)
    expected = (0, 0, 0)
    assert actual == expected


test_C30()
