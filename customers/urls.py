from django.urls import path, include

urlpatterns = [

    # Customers api end-point
    path('api/', include('customers.api.v1.urls')),
]
