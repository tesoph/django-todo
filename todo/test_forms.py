from django.test import TestCase
#from .models import Item
from .forms import ItemForm
# Create your tests here.
class TestToDoItemForm(TestCase):
    
    #methods
    #make a long descriptive name
    def test_can_create_an_item_with_just_a_name(self): #methods have to precede with test_ or django won't find them
        #self.assertEqual(1,1)
        form = ItemForm({"name":"Create tests"}) #instantiate it from the ItemForm
        self.assertTrue(form.is_valid())
        #self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_name(self):
        form = ItemForm({"name":""}) #instantiate it from the ItemForm
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], [u'This field is required.'])