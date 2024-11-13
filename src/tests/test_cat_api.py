import pytest


@pytest.mark.smoke
def test_get_single_image(api_client):
    """Test to verify that a single image can be retrieved."""
    response = api_client.get_images(params={"limit": 1})
    assert len(response) == 1
    assert 'url' in response[0], "Image URL is not present in the response"


@pytest.mark.smoke
@pytest.mark.parametrize("limit", [5, 10, 15])
def test_get_multiple_images(api_client, limit):
    """Test to retrieve multiple images and check that the count matches the requested limit."""
    response = api_client.get_images(params={"limit": limit})
    assert len(response) == limit, f"Expected {limit} images but got {len(response)}"
    for image in response:
        assert 'url' in image, "Image URL is not present in one of the responses"


@pytest.mark.regression
@pytest.mark.parametrize("limit_provided, limit_expected", [(-5, 1), (-1, 1), (-10, 1)])
def test_get_negative_images_number(api_client, limit_provided, limit_expected):
    """Test to retrieve negative images number and check that the count matches 1."""
    response = api_client.get_images(params={"limit": limit_provided})
    assert len(response) == limit_expected, f"Expected {limit_expected} images but got {len(response)}"
    for image in response:
        assert 'url' in image, "Image URL is not present in one of the responses"


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("breed_ids", ["beng", "abys", "siam"])
def test_get_images_with_specific_breed_ids(api_client, breed_ids):
    """Test to retrieve images with specific breed_ids."""
    response = api_client.get_images(params={"breed_ids": breed_ids})
    assert len(response) > 0
    assert 'breeds' in response[0], "Image BREEDS is not present in the response"
    assert 'id' in response[0]['breeds'][0], "Image BREEDS ID is not present in the response"
    assert response[0]['breeds'][0][
               'id'] == breed_ids, f"Expected breed id {breed_ids} but got {response[0]['breeds'][0]['id']}"


@pytest.mark.regression
def test_get_images_with_unknown_breed_ids(api_client):
    """Test to retrieve images with an unknown breed_id"""
    response = api_client.get_images(params={"breed_ids": "---UNKNOWN_VALUE_NOT_SET_EVER"})
    assert len(response) == 0
