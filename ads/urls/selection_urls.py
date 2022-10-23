from django.urls import path

from ads.views import SelectionListView, SelectionDetailView, SelectionUpdateView, SelectionCreateView, \
    SelectionDeleteView

urlpatterns = [
    path('', SelectionListView.as_view()),
    path('<int:pk>/', SelectionDetailView.as_view()),
    path('<int:pk>/update/', SelectionUpdateView.as_view()),
    path('create/', SelectionCreateView.as_view()),
    path('<int:pk>/delete/', SelectionDeleteView.as_view())
]
