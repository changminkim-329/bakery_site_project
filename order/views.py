from django.shortcuts import render
from django.views.generic.list import ListView
from product.models import Product
# Create your views here.
def order(request):
    return render(request, "order.html")


class OrderView(ListView):
    template_name = "order.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(Product.objects.filter(bread_type='Baguette')[0].image)
        context['baguettes'] = Product.objects.filter(bread_type='Baguette')
        context['bagels'] = Product.objects.filter(bread_type='Bagel')
        context['muffins'] = Product.objects.filter(bread_type='Muffin')
        context['croissants'] = Product.objects.filter(bread_type='Croissant')
        return context