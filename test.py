import pytest
from main import get_random_cat_image

def test_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
         "id":"LutjkZJpH",
         "url":"https://cdn2.thecatapi.com/images/LutjkZJpH.jpg",
         "width":500,
         "height":375

         }]



def test_failure(mocker):
    mocker.patch('requests.get', return_value={'status_code': 404})
    url = get_random_cat_image()
    assert url is None