import pytest

from ..gilded_rose import Item, GildedRose

@pytest.fixture()
def item(sell_in=0, quality=40):
    return Item(name="Sulfuras, Hand of Ragnaros", sell_in=sell_in, quality=quality)

def update_item(item):
    GildedRose([item]).update_quality()

class TestSulfuras():
    def test_sulfuras_positive_sell_in(self, item):
        item.sell_in = 1
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == 1
        assert item.quality == original_quality


    def test_sulfuras_sell_in_of_zero(self, item):
        item.sell_in = 0
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == 0
        assert item.quality == original_quality

    def test_sulfuras_negative_sell_in(self, item):
        item.sell_in = -1
        original_quality = item.quality

        update_item(item)

        assert item.sell_in == -1
        assert item.quality == original_quality