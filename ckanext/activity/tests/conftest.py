# -*- coding: utf-8 -*-

import pytest
from pytest_factoryboy import register

from ckan import model
import ckan.plugins
from ckan.tests import helpers, factories
from ckan.cli.db import _run_migrations
from ckan.tests.factories import CKANFactory
from ckanext.activity.model import Activity

from sqlalchemy import inspect


@register
class ActivityFactory(CKANFactory):
    """A factory class for creating CKAN activity objects."""

    class Meta:
        model = Activity
        action = "activity_create"


@pytest.fixture()
def clean_db(reset_db, migrate_db_for):
    reset_db()
    migrate_db_for("activity")


@pytest.fixture(scope="session")
def reset_db_once(reset_db, migrate_db_for):
    reset_db()
    migrate_db_for("activity")
