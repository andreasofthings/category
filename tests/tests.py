#!/usr/bin/env
# -*- encoding: utf-8
# vim: ts=4 et sw=4 sts=4

"""
"""

from django.test import TestCase, RequestFactory


class CategoryTest(TestCase):
    fixtures = [
        'Categories.yaml',
    ]

    def setUp(self):
        self.factory = RequestFactory()

    def test_category_list_view(self):
        from category.views import CategoryListView
        request = self.factory.get('/category')
        response = CategoryListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
