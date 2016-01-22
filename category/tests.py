#!/usr/bin/env
# -*- encoding: utf-8
# vim: ts=4 et sw=4 sts=4

"""
"""

from django.test import TestCase, RequestFactory

from category.models import Category
from category.models import Tag


class CategoryTest(TestCase):
    fixtures = [
        'categories.yaml',
    ]

    def setUp(self):
        self.factory = RequestFactory()

    def test_new_category(self):
        cat = Category.create(name="Test")
        self.assertEqual(cat.pk, 2)

    def test_category_list_view(self):
        from category.views import CategoryListView
        request = self.factory.get('/category')
        response = CategoryListView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class TagTest(TestCase):
    fixtures = [
        'categories.yaml',
    ]

    def setUp(self):
        self.factory = RequestFactory()

    def test_new_tag(self):
        c = Tag.create(name="Test")
        self.assertEqual(c.pk, 1)
