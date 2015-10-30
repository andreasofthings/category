#!/usr/bin/env
# -*- encoding: utf-8
# vim: ts=4 et sw=4 sts=4

"""
"""

from django.conf import settings

settings.configure(DEBUG=True)

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
