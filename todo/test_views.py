#testing for: 
# 1. going to the correct url
# 2. correct template has been used
from django.test import TestCase
from .models import Item
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page,"todo_list.html")

    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEquals(page.status_code,200)
        self.assertTemplateUsed(page,"item_form.html")

    def test_get_edit_item_page(self):
        #have to create an instance of the item model to allow test to retrieve id from the database
        item=Item(name="Create a test")
        item.save()
        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEquals(page.status_code,200)
        self.assertTemplateUsed(page,"item_form.html")
    
    def test_get_edit_page_for_item__that_does_not_exist(self):
         #have to create an instance of the item model to allow test to retrieve id from the database
        #item=Item(name="Create a test")
        #item.save()
        page = self.client.get("/edit/{0}".format(1))
        self.assertEquals(page.status_code,404)
        #self.assertTemplateUsed(page,"item_form.html")

    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
    
    def test_post_edit_an_item(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)
        self.assertEqual("A different name", item.name)

    def test_toggle_status(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id

        response = self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)