from django.shortcuts import render, redirect
from datetime import datetime
from app.models import Coffee, Transaction


# Renders the base page for the app, along with passing all coffee objects
# to the page within the context.


def home(request):
    coffees = Coffee.objects.all()
    return render(request, "app/coffee_list.dhtml", {"coffees": coffees})


# Renders the transaction correlating to a specific purchase
# via context to a unique page for viewing transactions.


def transaction_detail(request, id):
    transaction = Transaction.objects.get(id=id)
    return render(request, "app/transaction_detail.dhtml", {"transaction": transaction})


# Gets the selected coffee, calculates the information need to construct
# a new transaction to accompany the sell, then renders the
# newly created transaction in a similar way as the
# transaction_detail view above.


def buy_coffee(request, id):
    coffee = Coffee.objects.get(id=id)
    pre_tax = coffee.price
    time = datetime.now()
    tax = round((pre_tax * 0.07), 2)
    transaction = Transaction.objects.create(
        time=time, pre_tax=pre_tax, tax=tax, item=coffee
    )
    trans_id = transaction.id
    return redirect("transaction_detail", trans_id)


# Makes some default coffees to use during testing, didn't have the models
# registered while the app was in construction so used this a
# quick way to just go ahead and have some models to use while testing.


def make_coffee(request):
    Coffee.objects.create(name="Latte", price=2.99)
    Coffee.objects.create(name="Stuff", price=4.99)
    return redirect("home")

