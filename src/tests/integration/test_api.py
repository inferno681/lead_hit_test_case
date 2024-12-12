import pytest
from fastapi import status


@pytest.mark.anyio
async def test_create_form_body(
    client,
    add_form_link,
    add_test_data,
    test_response,
):
    """Тест добавления формы в бд через тело запроса."""
    response = await client.post(
        add_form_link,
        json=add_test_data,
    )
    assert response.status_code == status.HTTP_200_OK
    assert test_response == response.json()


@pytest.mark.anyio
async def test_get_form_body(client, get_form_link, get_test_data):
    """Тест получения форм через тело запроса."""
    response = await client.post(
        get_form_link,
        json=get_test_data['data'],
    )
    assert response.status_code == status.HTTP_200_OK
    assert get_test_data['response'] == response.json()


@pytest.mark.anyio
async def test_get_form_list_body(
    client,
    get_form_list_link,
    get_form_list_data,
):
    """Тест получения списка форм через тело запроса."""
    response = await client.post(
        get_form_list_link,
        json=get_form_list_data['data'],
    )
    assert response.status_code == status.HTTP_200_OK
    assert get_form_list_data['response'] == response.json()


@pytest.mark.anyio
async def test_create_form_query(
    client,
    add_form_link,
    add_test_data,
    test_response,
):
    """Тест добавления формы в бд через параметры запроса."""
    add_test_data['name'] = 'Some name query'
    response = await client.post(
        add_form_link,
        params=add_test_data,
    )
    test_response['name'] = 'Some name query'
    assert response.status_code == status.HTTP_200_OK
    assert test_response == response.json()


@pytest.mark.anyio
async def test_get_form_query(client, get_form_link, get_test_data):
    """Тест получения форм через параметры запроса."""
    response = await client.post(
        get_form_link,
        params=get_test_data['data'],
    )
    assert response.status_code == status.HTTP_200_OK
    assert get_test_data['response'] == response.json()


@pytest.mark.anyio
async def test_get_form_list_query(
    client,
    get_form_list_link,
    get_form_list_data,
):
    """Тест получения списка форм через параметры запроса."""
    response = await client.post(
        get_form_list_link,
        params=get_form_list_data['data'],
    )
    assert response.status_code == status.HTTP_200_OK
    assert get_form_list_data['response'] == response.json()


@pytest.mark.anyio
@pytest.mark.parametrize(
    'links',
    [
        pytest.param('add_form_link', id='add_form_link'),
        pytest.param('add_form_link', id='add_form_link'),
        pytest.param('add_form_link', id='add_form_link'),
    ],
    indirect=True,
)
async def test_no_data_request(client, links):
    """Тест на отсутствие данных в запросе."""
    response = await client.post(links)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
