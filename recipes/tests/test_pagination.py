from unittest import TestCase

from recipes.utils.pages import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_paginas=4,
            current_page=1,
        )['pag']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_pages_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_paginas=4,
            current_page=2,
        )['pag']
        self.assertEqual([1, 2, 3, 4], pagination)
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_paginas=4,
            current_page=3,
        )['pag']
        self.assertEqual([2, 3, 4, 5], pagination)

    def test_mid_pages_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_paginas=4,
            current_page=10,
        )['pag']
        self.assertEqual([9, 10, 11, 12], pagination)
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_paginas=4,
            current_page=12,
        )['pag']
        self.assertEqual([11, 12, 13, 14], pagination)

    def test_pages_range_last(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_paginas=4,
            current_page=12,
        )['pag']
        self.assertEqual([11, 12, 13, 14], pagination)
