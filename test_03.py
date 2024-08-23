import pytest
from AT_03 import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('AT_03.requests.get')

    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        'url': 'https://example.com/cat.jpg'
    }]

    api_key = 'test_api_key'
    cat_image_url = get_random_cat_image(api_key)

    assert cat_image_url == 'https://example.com/cat.jpg'


def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('AT_03.requests.get')

    # Создаем мок-ответ для неуспешного запроса
    mock_get.return_value.status_code = 404

    api_key = 'test_api_key'
    cat_image_url = get_random_cat_image(api_key)

    assert cat_image_url is None


if __name__ == "__main__":
    # Запускаем pytest и отображаем результаты
    pytest.main(["-v", __file__])