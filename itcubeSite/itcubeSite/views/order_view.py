from django.shortcuts import render, redirect

from itcubeSite.forms import OrderNew
from itcubeSite.models import Orders, Customer, Product


def new_order(request):
    if request.method == "POST":
        try:
            form = OrderNew(request.POST)
            if form.is_valid():
                customer_id = form["customer"].value()
                date = form["date"].value()
                products = form["products"].value()

                order = Orders(date=date,
                               customer=Customer.objects.get(id=customer_id))

                order.save()
                for product_id in products:
                    product = Product.objects.get(id=product_id)
                    if product is not None:
                        order.products.add(product)

                return redirect("/order")
        except Exception as e:
            form = OrderNew(request.POST)
            return render(request, "addOrder.html", {
                'form': form,
                'error_message': e
            })
    else:
        form = OrderNew()
        return render(request, "addOrder.html", {'form': form})


def list_order(request):
    out = Orders.objects.all()
    orders = []

    for order in out:
        products = []
        for product in order.products.all():
            products.append(
                (product.id,
                 product.name)
            )

        orders.append((
            order.id,
            order.date,
            order.customer,
            products
        ))

    return render(request, "orderList.html", {'orders': orders})