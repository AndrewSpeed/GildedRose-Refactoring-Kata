# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_backstage_pass(self, item):
        if item.quality < 50:
            if item.sell_in <= 0:
                item.quality = 0
            elif item.sell_in <= 5:
                item.quality += 3
            elif item.sell_in <= 10:
                item.quality += 2
            else:
                item.quality += 1

        item.sell_in -= 1

        return item

    def update_brie(self, item):
        if item.quality < 50:
            if item.sell_in > 0:
                item.quality += 1
            else:
                item.quality += 2

        item.sell_in -= 1
        
        return item

    def update_normal_item(self, item):
        if item.quality > 0:
            if item.sell_in > 0:
                item.quality -= 1
            else:
                item.quality -= 2
        item.sell_in -=1

        return item

    def update_sulfuras(self, item):
        return item

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                return self.update_brie(item)
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                return self.update_backstage_pass(item)
            if item.name == "Sulfuras, Hand of Ragnaros":
                return self.update_sulfuras(item)
            return self.update_normal_item(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
