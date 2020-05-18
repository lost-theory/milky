import unittest
import logging

logging.getLogger().setLevel(logging.CRITICAL)

from milky.api import API
from milky.error import RTMRequestError

BAD_API_KEY = "bad-api-key"
BAD_SECRET = "bad-secret"


class TestAPI(unittest.TestCase):
    def test_create_api(self):
        rtm = API(BAD_API_KEY, BAD_SECRET)

    def test_echo_with_bad_api_creds_fails(self):
        rtm = API(BAD_API_KEY, BAD_SECRET)
        try:
            rtm.test.echo()
        except RTMRequestError as exc:
            assert "Invalid API Key" in repr(exc)

    def test_list_methods_exist(self):
        rtm = API(BAD_API_KEY, BAD_SECRET)
        assert rtm.lists.methods.keys() == {
            "add",
            "archive",
            "delete",
            "getList",
            "setDefaultList",
            "setName",
            "unarchive",
        }


if __name__ == "__main__":
    unittest.main()
