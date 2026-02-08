from django.shortcuts import render


def cars_view(request):
    return render(
        request,
        'cars.html',
        {'cars': {'model': 'HB20 Confort'} }
        )
