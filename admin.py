from django.contrib import admin

class BookAdminSite(admin.AdminSite):
    title_header = 'Book Admin'
    site_header = 'Book administration'
    index_title = 'Book site admin'