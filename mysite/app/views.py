from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from app.models import MegaOrder, MiniOrder
from django.urls import reverse
from django.http import HttpResponseRedirect


def home(request):
    all_mega_orders = MegaOrder.objects.all()
    return render(request, 'home.html', {"all_mega_orders": all_mega_orders})


def create_order(request):
    if request.method == "GET":
        return render(request, 'create-order.html')
    else:
        itemurl = request.POST['itemurl']
        # would use API
        if itemurl.startswith("https://www.amazon.com/Cannery-Row-Centennial-John-Steinbeck/dp/014200068X/"):
            name = "Cannery Row: (Centennial Edition) Paperback – Deckle Edge, February 5, 2002"
            picture = "https://images-na.ssl-images-amazon.com/images/I/51pKtoV%2Bd2L._SX332_BO1,204,203,200_.jpg"
            asin = "014200068X"
            units = 1
            price = 13.89
            description = "Steinbeck's tough yet charming portrait of people on the margins of society, dependant on " \
                          "one another for both physical and emotional survival"
        else:
            name = "Cannery Row: (Centennial Edition) Paperback – Deckle Edge, February 5, 2002"
            picture = "https://images-na.ssl-images-amazon.com/images/I/51pKtoV%2Bd2L._SX332_BO1,204,203,200_.jpg"
            asin = "014200068X"
            units = 1
            price = 13.89
            description = "Steinbeck's tough yet charming portrait of people on the margins of society, dependant on " \
                          "one another for both physical and emotional survival"
        if MegaOrder.objects.filter(asin=asin).count() == 0:
            megaOrder = MegaOrder(name=name, link=itemurl, picture=picture, asin=asin, units=units, price=price, description=description)
            megaOrder.save()
        # m = MegaOrder.orders.filter(asin=asin)
    
        return redirect("order-details", asin=asin)
        # url = reverse('app/order-details', kwargs={'name': name, 'picture': picture, 'price': price})
        # return HttpResponseRedirect(url)
        # return render(request, 'order-details.html')
    # template = loader.get_template("app/order-details.html")
    # context = {'name': name; 'picture': picture; 'price': price}
    # return redirect(template.render(context, request))


def order_details(request, asin):
    if request.method == "GET":
        mega_order = get_object_or_404(MegaOrder, asin=asin)
        return render(request, 'order-details.html', {"mega_order": mega_order})
    else:
        order = request.POST['order']
        name = request.POST['name']
        email = request.POST['email']
        units = request.POST['units']
        mini_order = MiniOrder(order=order, name=name, email=email, units=units)
        mini_order.save()
        check_order()
        # return render(request, 'complete-order.html')
        return redirect("complete-order")


def complete_order(request):
    return render(request, "complete-order.html")


def check_order():
    return HttpResponse("Check order") # TODO
