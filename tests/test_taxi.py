import taxi


def test_when_run_1_km_pay_6_yuan():
    assert taxi.calculate(1) == 6


def test_when_run_3_km_pay_7_yuan():
    assert taxi.calculate(3) == 7


def test_when_run_10_km_pay_13_yuan():
    assert taxi.calculate(10) == 13


def test_when_run_2_km_wait_3_minutes_pay_7_yuan():
    assert taxi.calculate(2, 3) == 7


def test_format_output_6_yuan():
    assert taxi.format_output(6) == "收费6元"


def test_format_output_10_yuan():
    assert taxi.format_output(10) == "收费10元"


def test_parse_line_3_km():
    assert taxi.parse_line("3公里,等待0分钟") == (3, 0)


