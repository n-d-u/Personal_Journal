from django.urls import path
from . import views
from .views import entryCreate, entryDelete, entryList, entryUpdate, journalLogIn, journalLogOut, journalSignUp
from .views  import entryDetail
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[

    path('login/', journalLogIn.as_view(), name ='login'),
    path('logout/', journalLogOut.as_view(), name = 'logout'),
    path('signup/', journalSignUp.as_view(), name = 'signup'),
    path('', entryList.as_view(), name = 'My Journal'),
    path('entry/<int:pk>/', entryDetail.as_view(), name = 'Entries Details'),
    path('add-entry/', entryCreate.as_view(), name = 'Add'),
    path('edit-entry/<int:pk>/', entryUpdate.as_view(), name = 'Edit'),
    path('delete-entry/<int:pk>/', entryDelete.as_view(), name = 'Delete'),
    




]

urlpatterns += staticfiles_urlpatterns()
