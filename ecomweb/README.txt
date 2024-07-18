def index(request):
    if request.POST:
        category=request.POST.get('category')
        if category=="all":
            products = product.objects.all()
            return render(request,'index.html',{'products': products})
        else:    
            products = product.objects.filter(category=category)
            return render(request,'index.html',{'products': products})

       

    products = product.objects.all()
    return render(request,'index.html',{'products': products})