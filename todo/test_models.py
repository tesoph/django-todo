from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):
    def test_done_defaults_to_False(self):
        #if we create a new item without specifiying done it will default to false (not done)
        item = Item(name="Create a test")
        item.save()
        self.assertEqual(item.name, "Create a test")
        self.assertFalse(item.done)

    def test_can_creat_item_with_name_and_status(self):
        #if we create a new item without specifiying done it will default to false (not done)
        item = Item(name="Create a test", done=True)
        item.save()
        self.assertEqual(item.name, "Create a test")
        self.assertTrue(item.done)
    
    def test_item_as_a_string(self):
        item = Item(name="Create a test")
        self.assertEqual("Create a test", str(item))
    #probably don't need to test for this as django does validate itself?    
    '''def test_name_must_not_be_blank(self):
        item = Item(name="")
        item.save()
        self.assertFalse(item)'''