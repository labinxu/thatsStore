#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thatsStore.settings")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thatsStore.settings")  # project_name 项目名称

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
