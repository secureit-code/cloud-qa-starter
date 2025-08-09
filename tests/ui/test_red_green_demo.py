def test_red_demo_should_fail():
    # Medveten “bugg”: 2+2 är INTE 5 ? testet ska bli rött i CI
    assert 2 + 2 == 5
