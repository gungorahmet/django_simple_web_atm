from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def calculate(request):
    # Get amount value from request.
    amount = request.GET['amount']
    try:
        amount_tmp = int(amount)
    except ValueError:
        return render(request, 'error_page.html', {'error_message': "Money should be integer"})

    # We already know about $ cash types. We can hold into tuples. It's stable
    t_cash_moneys = (100, 50, 20, 10, 5, 2, 1)

    # This will hold count of money types as dictionary.
    d_calculated_cash = {}

    for money in t_cash_moneys:
        d_calculated_cash[money] = int(amount_tmp / money)
        amount_tmp %= money

    return render(request, 'atm.html', {'calculated_cash': d_calculated_cash.items(),
                                        'sum_of_min_total': sum(d_calculated_cash.values()),
                                        'amount': amount})
