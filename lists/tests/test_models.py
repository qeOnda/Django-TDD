from ..models import Item, List
from django.test import TestCase
from django.core.exceptions import ValidationError


class ItemModelTest(TestCase):

    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')

    def test_item_is_related_to_list(self):
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(text='bla', list=list_)
        with self.assertRaises(ValidationError):
            item = Item(text='bla', list=list_)
            item.full_clean()
    
    def test_CAN_save_item_to_different_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text="bla")
        item = Item.objects.create(list=list2, text="bla")
        item.full_clean() #should not raise an error

class ListModelTest(TestCase):
    
    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')


