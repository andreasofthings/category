#! /usr/bin/env python

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.devsettings'


if __name__ == '__main__':
    """
    Test Django App in travis.ci
    """
    import django
    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], "migrate"])
    execute_from_command_line([sys.argv[0], "makemigrations", "userprofile",])
    if hasattr(django, 'setup'):
        django.setup()
    from django.test.runner import DiscoverRunner
    failures = DiscoverRunner().run_tests(("category",), verbosity=2)
    if failures:
        sys.exit(failures)
