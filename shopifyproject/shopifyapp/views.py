from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Shopify
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
def index(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)

    paginator = Paginator(products_list, 12)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "index.html", {'category': c_page, 'products': products})


def proDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Product.DoesNotExist:
        product = None  # Handle the missing product case gracefully
    return render(request, "product.html", {'product': product})


def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,"search.html",{'query':query,'products':products})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        # Prepare errors dictionary
        errors = {}
        if Shopify.objects.filter(username=username).exists():
            errors['username_error'] = 'Username already exists. Please choose another one.'
        if Shopify.objects.filter(email=email).exists():
            errors['email_error'] = 'Email already registered. Please use another email.'
        if len(password) < 8:
            errors['password_length_error'] = 'Password must be at least 8 characters long.'
        if password != cpassword:
            errors['password_mismatch'] = 'Passwords do not match.'
        if errors:
            return render(request, 'register.html', errors)

        # Save the user if there are no errors
        user = Shopify(username=username, email=email, password=password, cpassword=cpassword)
        user.save()
        return redirect('shopifyapp:login')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        errors = {}
        try:
            user = Shopify.objects.get(email=email)
        except Shopify.DoesNotExist:
            errors['email_error'] = 'Invalid email'
            user = None
        if user and user.password != password:
            errors['password_error'] = 'Invalid password'
        if errors:
            return render(request, 'login.html', {'errors': errors})
        # Set session data after successful login
        request.session['user_id'] = user.id
        return redirect('shopifyapp:index')
    return render(request, 'login.html')


def logout(request):
    if 'user_id' in request.session:
        request.session.flush()
        messages.success(request, 'You have been logged out successfully.')
    return redirect('shopifyapp:login')








