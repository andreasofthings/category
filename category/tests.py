#!/usr/bin/env
# -*- encoding: utf-8
# vim: ts=4 et sw=4 sts=4

"""
"""

import django
from django.conf import settings
from django.test import TestCase, RequestFactory
from django.core.management.commands.migrate import Command as Migrate
databases = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
installed_apps = {
    'category',
}
settings.configure(
    DATABASES=databases,
    INSTALLED_APPS=installed_apps,
    DEFAULT_INDEX_TABLESPACE="",
    ROOT_URLCONF='urls',
    DEBUG=True
)
django.setup()
Migrate.handle()


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
