"""
using re-written names
"""

from unittest import TestCase
from unittest.mock import Mock, call

from magic_patch import magic_patch

from tests.case2_data.src import main
from datetime import datetime


class MagicPathTest2(TestCase):

    def test_magic_path(self):
        frozen_value = datetime(2021, 1, 2, 3, 4, 5, 6)
        datetime_mock = Mock(now=Mock(return_value=frozen_value))

        expected = (frozen_value, frozen_value, frozen_value)
        with magic_patch(main, datetime, datetime_mock, search_by_all_names=True):

            actual = main.main_func()

        self.assertEqual(actual, expected)
        self.assertEqual(datetime_mock.now.call_args_list, [call(), call(), call()])


