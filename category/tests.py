#!/usr/bin/env
# -*- encoding: utf-8
# vim: ts=4 et sw=4 sts=4

"""
"""

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import reverse

from .models import Category

from .models import Tag


class CategoryTest(TestCase):
    fixtures = [
        'categories.yaml',
    ]

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.anonymous = AnonymousUser()

    def test_new_category(self):
        cat = Category.create(name="Test")
        self.assertEqual(cat.pk, 7)

    def test_category_list_view(self):
        url = reverse('category:category-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view(self):
        url = reverse('category:category-detail', kwargs={'pk': 1, })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_category_add_view(self):
        url = reverse('category:category-add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_category_add_view_authenticated(self):
        url = reverse('category:category-add')
        self.client.login(username="jacob", password="top_secret")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_category_update_view(self):
        url = reverse('category:category-update', kwargs={'pk': 1, })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        url = reverse('category:category-update', kwargs={'slug': 'business'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_category_update_view_authenticated(self):
        self.client.login(username="jacob", password="top_secret")
        url = reverse('category:category-update', kwargs={'pk': 1, })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('category:category-update', kwargs={'slug': 'business'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()


class TagTest(TestCase):
    fixtures = [
        'categories.yaml',
    ]

    def setUp(self):
        self.factory = RequestFactory()

    def test_new_tag(self):
        c = Tag.create(name="Test")
        self.assertEqual(c.pk, 3)
