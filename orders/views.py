from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from orders.models import Customer, Order


# Create your views here.
class CustomerViewOrders(TemplateView):
    template_name = "order_list.html"

    def get_context_data(self, **kwargs):
        customer = self.kwargs["customer"]

        context = super().get_context_data(**kwargs)
        context["order_list"] = Order.objects.filter(customer__pk=customer)
        context["customer"] = Customer.objects.get(pk=customer)
        return context


class CustomerViewAll(ListView):
    template_name = "customer_list.html"
    model = Customer
