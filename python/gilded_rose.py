# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            processor = ProcessorFactory.for_item(item)
            processor.update()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemProcessor:
    def __init__(self, item):
        self.item = item

    def has_expired(self):
        return self.item.sell_in > 0

    def update_quality_before_expiry(self):
        self.item.quality -= 1

    def update_quality_after_expiry(self):
        self.item.quality -= 2

    def update_quality(self):
        if self.item.quality > 0 and self.item.quality < 50:
            if self.has_expired():
                self.update_quality_before_expiry()
            else:
                self.update_quality_after_expiry()

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update(self):
        self.update_quality()
        self.update_sell_in()

class AgedBrieProcessor(ItemProcessor):
    """Item that increases in quality"""
    def update_quality_before_expiry(self):
        self.item.quality += 1

    def update_quality_after_expiry(self):
        self.item.quality += 2

class BackstagePassProcessor(ItemProcessor):
    """Item that increases in quality until it expires, then drops to zero"""
    def update_quality_before_expiry(self):
        if self.item.sell_in <= 5:
            self.item.quality += 3
        elif self.item.sell_in <= 10:
            self.item.quality += 2
        else:
            self.item.quality += 1

    def update_quality_after_expiry(self):
        self.item.quality = 0

class ConjuredProcessor(ItemProcessor):
    """Item that degrades in quality twice as fast as normal items"""
    def update_quality_before_expiry(self):
        self.item.quality -= 2

    def update_quality_after_expiry(self):
        self.item.quality -= 4


class SulfurasProcessor(ItemProcessor):
    def update(self):
        # item does not have to be sold, or decrease in value
        pass

class ProcessorFactory:
    item_to_processor_mapping = {
        "Aged Brie": AgedBrieProcessor,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassProcessor,
        "Conjured Mana Cake": ConjuredProcessor,
        "Sulfuras, Hand of Ragnaros": SulfurasProcessor,
    }

    @staticmethod
    def for_item(item):
        return ProcessorFactory.item_to_processor_mapping.get(item.name, ItemProcessor)(item)