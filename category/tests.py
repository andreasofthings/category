#!/usr/bin/env
# -*- encoding: utf-8
# vim: ts=4 et sw=4 sts=4

"""
"""

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import reverse

from category.models import Category
from category.views import CategoryListView
from category.views import CategoryDetailView

from category.models import Tag


class CategoryTest(TestCase):
    fixtures = [
        'categories.yaml',
    ]

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.anonymous = AnonymousUser()

    def test_new_category(self):
        cat = Category.create(name="Test")
        self.assertEqual(cat.pk, 2)

    def test_category_list_view(self):
        request = self.factory.get('/category')
        response = CategoryListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view(self):
        request = self.factory.get(
            reverse('category:category-view', kwargs={'slug': 'test'})
        )

        request.user = self.anonymous
        response = CategoryDetailView.as_view()(request)
        self.assertEqual(response.status_code, 302)

        request.user = self.user
        response = CategoryDetailView.as_view()(request)
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
