import pytest
from swagger_server.services.pet_service import service_find_pets_by_status


class TestFindPetsByStatusService():
    """---"""

    def test_valid_find_pets_by_status(self):
         # valid
        assert service_find_pets_by_status(['valid']) == """Status Return:['valid']"""
        assert service_find_pets_by_status('valid') == "Status Return:valid"
        assert service_find_pets_by_status(123) == "Status Return:123"

    def test_null_find_pets_by_status(self):
         # null
        assert service_find_pets_by_status('') == "Status Return:"
        assert service_find_pets_by_status(None) != "Status Return:"

    def test_undefined_find_pets_by_status(self):
         # undefined
         with pytest.raises(Exception):
             service_find_pets_by_status()

    # def test_invalid_find_pets_by_status(self):
    #      # invalid
    #     assert service_find_pets_by_status($%^%$) == """Status Return:['$%^%$']"""

    # def test_extreme_find_pets_by_status(self):
    #      # extreme
    #      # https://stackoverflow.com/questions/1739913/what-is-the-max-length-of-a-python-string
    #     assert service_find_pets_by_status(['']) == """Status Return:['valid']"""
