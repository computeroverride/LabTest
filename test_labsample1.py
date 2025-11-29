import labsample1


def test_get_longest_workout():
    workouts = labsample1.load_csv()
    expected = {"date": "25.01.2022", "activity": "Cycling","duration": 75}
    result = labsample1.get_longest_workout(workouts)
    assert (result == expected)


def test_calc_total_duration():
    workouts = labsample1.load_csv()
    expected = 853
    result = labsample1.calc_total_duration(workouts)
    assert (result == expected)


def test_calc_average_duration():
    workouts = labsample1.load_csv()
    expected = 853/ 20
    result = labsample1.calc_average_duration(workouts)
    assert (result == expected)
