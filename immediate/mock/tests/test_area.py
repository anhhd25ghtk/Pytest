from mock_examples.area import area_of_circle


def test_area_of_circle_with_mock(mocker):
    """
    Function to test area of circle with mocked Pi value
    :param mocker:
    :return:
    """
    mocker.patch('mock_examples.area.PI',4)
    assert area_of_circle(2) == 16


