#!/usr/bin/env
# -*- encoding: utf-8
# vim: ts=4 et sw=4 sts=4

"""
"""

from django.test import TestCase, RequestFactory

from category.models import Category


class CategoryTest(TestCase):
    fixtures = [
        'categories.yaml',
    ]

    def setUp(self):
        self.factory = RequestFactory()

    def test_new_category(self):
        cat = Category(name="Test")
        pk, created = cat.save()
        self.assertEqual(pk, 2)
        self.assertEqual(created, True)

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
        from category.models import Tag
        c = Tag(name="Test")
        pk, created = c.save()
        self.assertEqual(pk, 2)
        self.assertEqual(created, True)
