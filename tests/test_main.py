import os
from xml.etree import ElementTree as ET

import pytest
from lxml.html import parse as html_parse

from ..main import (
    build_item_context,
    get_item_details,
)


@pytest.fixture
def tree():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', 'ad-rss.xml')
    return ET.parse(path).getroot()


@pytest.fixture
def html_tree():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', 'article.html')
    return html_parse(path)


def test_get_item_details(tree):
    item = tree.find('.//item')
    details = get_item_details(item)
    assert details['link'] == 'https://www.architecturaldigest.com/story/why-high-gloss-paint-should-be-on-your-radar'
    assert details['guid'] == '59df9cf1f7610e67d7f16a0b'


def test_build_item(html_tree):
    item = build_item_context(html_tree)
    assert 'https://media.architecturaldigest.com/photos/59dfb79cc9ed4c222543c068/master/pass/high-gloss-paint-1.jpg' in item['description']
    assert '' in item['description']
