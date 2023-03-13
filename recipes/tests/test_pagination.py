from unittest import TestCase

from recipes.utils.pages import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_paginas=4,
            current_page=1,
        )
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_pages_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_paginas=4,
            current_page=2,
        )
        self.assertEqual([1, 2, 3, 4], pagination)
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_paginas=4,
            current_page=3,
        )
        self.assertEqual([2, 3, 4, 5], pagination)
