from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views import View
from .models import Customer,Product,Cart,Orderplaced
from .forms import userregistation,profile_From
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class homeView(View):
    def get(self,request):
        totalitem=0
        botoomware =Product.objects.filter(categary='BW')
        topware =Product.objects.filter(categary='TW')
        laptop =Product.objects.filter(categary='L')
        mobile =Product.objects.filter(categary='M')
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        dic={
            'botoomware':botoomware,
            'topware':topware,
            'laptop':laptop,
            'mobile':mobile,
            'totalitem':totalitem,
        }
        return render(request,'app/home.html',dic)

class product_detail_View(View):
    def get(self,request,id): 
        totalitem=0
        product = Product.objects.get(pk=id)
        item_alredy_in_cart=False
        if request.user.is_authenticated:
           item_alredy_in_cart=Cart.objects.filter(Q(product= product.id) & Q(user=request.user)).exists()
           totalitem=len(Cart.objects.filter(user=request.user))

       
        dic={
            'ob':product , 
            'item_alredy_in_cart':item_alredy_in_cart,
             'totalitem':totalitem,
          }
        return render(request, 'app/productdetail.html', dic)
     
 
@login_required
def add_to_cart(request):
    usr=request.user
    product_id=request.GET.get('prod-id')
    product=Product.objects.get(id=product_id)
    ct=Cart(user=usr,product=product)
    ct.save()

    return HttpResponseRedirect('/show-cart')

@login_required
def show_cart(request):
    totalitem=0
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        amount=0.0
        shipping_amount=50.0
        totalitem=len(Cart.objects.filter(user=request.user))

        cart_product=[p for p in Cart.objects.all() if p.user == request.user]  
        if cart_product :
            for p in cart_product:
                tempamount=(p.quantity * p.product.discount_price)
                amount+=tempamount

            dic={
                'carts':cart,
                'amount':amount,
                'shipping_amount':shipping_amount,
                'total_amount':amount+shipping_amount,
                 'totalitem':totalitem,
                 }
            return render(request, 'app/addtocart.html',dic)
        else:
            return render (request,'app/emptycart.html')
 


@method_decorator(login_required,name='dispatch')
class Profile_View(View):
    def get (slef,request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        fm=profile_From()
        dic={
            'form':fm,
            'active':'btn-primary',
            'totalitem':totalitem,
        }
        return render(request, 'app/profile.html',dic)
    
    def post(self,request):
        fm=profile_From(request.POST)
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        if fm.is_valid():
            usr=request.user
            name=fm.cleaned_data['name']
            locality=fm.cleaned_data['locality']
            city=fm.cleaned_data['city']
            state=fm.cleaned_data['state']
            zipcode=fm.cleaned_data['zipcode']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            fm=profile_From()
            messages.success(request,'Prfile Successfully Save !!!')

        dic={
            'form':fm,
            'active':'btn-primary',
            'totalitem':totalitem,
        }
        return render(request, 'app/profile.html',dic)



@login_required
def address(request):
     totalitem=0
     if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
     fm=Customer.objects.all()
     dic={
         'form':fm,
         'active':'btn-primary',
         'totalitem':totalitem,
     }
     return render(request, 'app/address.html',)

@login_required
def orders(request):
     totalitem=0
     if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
     order_placed=Orderplaced.objects.filter(user=request.user)

     return render(request, 'app/orders.html',{'order_placed':order_placed,  'totalitem':totalitem,})



def mobile(request,data=None):
    
    if data==None:
        mb=Product.objects.filter(categary='M')
    elif data=='sumsung' or data=='redmi':
        mb=Product.objects.filter(categary='M').filter(brand=data)
    elif data=='avobe':
        mb=Product.objects.filter(categary='M').filter(discount_price__gt=10000)
    elif data=='below':
        mb=Product.objects.filter(categary='M').filter(discount_price__lt=10000)
    elif data=='equel':
        mb=Product.objects.filter(categary='M').filter(discount_price=10000)

    totalitem=0
    if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))

    dic={
        'mb':mb,
        'totalitem':totalitem,
    }
    return render(request, 'app/mobile.html',dic)
 

def laptop(request,data=None):
    if data==None:
        lp=Product.objects.filter(categary='L')
    elif data=='asus' or data=='hp':
        lp=Product.objects.filter(categary='L').filter(brand=data)
    elif data=='avobe':
        lp=Product.objects.filter(categary='L').filter(discount_price__gt=50000)
    elif data=='below':
        lp=Product.objects.filter(categary='L').filter(discount_price__lt=50000)
    elif data=='equel':
        lp=Product.objects.filter(categary='L').filter(discount_price=50000)
    
    totalitem=0
    if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))

    dic={
        'lp':lp,
         'totalitem':totalitem,
    }
    return render(request, 'app/laptop.html',dic)

def bottomware(request,data=None):
    if data==None:
        bw=Product.objects.filter(categary='BW')
    elif data=='dildo' or data=='boishaki':
        bw=Product.objects.filter(categary='BW').filter(brand=data)
    elif data=='avobe':
        bw=Product.objects.filter(categary='BW').filter(discount_price__gt=500)
    elif data=='below':
        bw=Product.objects.filter(categary='BW').filter(discount_price__lt=500)
    elif data=='equel':
        bw=Product.objects.filter(categary='BW').filter(discount_price=500)
   
    totalitem=0
    if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))

    dic={
        'bw':bw,
         'totalitem':totalitem,
    }
    return render(request, 'app/bottomware.html',dic)
 
def topware(request,data=None):
    if data==None:
        tw=Product.objects.filter(categary='TW')
    elif data=='dildo' or data=='boishaki':
        tw=Product.objects.filter(categary='TW').filter(brand=data)
    elif data=='avobe':
        tw=Product.objects.filter(categary='TW').filter(discount_price__gt=500)
    elif data=='below':
        tw=Product.objects.filter(categary='TW').filter(discount_price__lt=500)
    elif data=='equel':
        tw=Product.objects.filter(categary='TW').filter(discount_price=500)
    
    
    totalitem=0
    if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))

    dic={
        'tw':tw,
        'totalitem':totalitem,
    }
    return render(request, 'app/topware.html',dic)

class user_regi_View(View):
    def get(self,request):
        form=userregistation()
        dic={
            'form':form
        }
        return render(request, 'app/customerregistration.html',dic)
    def post(self,request):
        form=userregistation(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations !!! Registered Successfully")
            form.save()
        
        dic={
            'form':form
        }
        return render(request, 'app/customerregistration.html',dic)

@login_required
def checkout(request):
    add=Customer.objects.filter(user=request.user)
    cart_item=Cart.objects.filter(user=request.user)
    amount=0.0
    shipping_amount=50.0
    cart_product=[p for p in Cart.objects.all()  if p.user==request.user]
    for o in cart_product:
        tempamount=(o.quantity * o.product.discount_price) 
        amount+=tempamount
    
    totalitem=0
    if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))

    dic={
        'add': add,
        'cart_item':cart_item,
        'amount':amount,
        'shipping_amount':shipping_amount,
        'total_amount':amount + shipping_amount,
         'totalitem':totalitem,
    }
    return render(request, 'app/checkout.html',dic)

@login_required
def paymentdone(request):
    user=request.user
    custid=request.GET.get('custid')
  
    customer=Customer.objects.get(id = custid)
    cart =Cart.objects.filter(user=user)
    for c in cart:
        Orderplaced(user=user,customer=customer,product=c.product,quantity=c.quantity) .save()
        c.delete()

    return redirect("orders")



@login_required
def pluscart(request):
    if request.method=='GET':
        pid =request.GET['prod_id']
        print (pid)
        c=Cart.objects.get(Q(product=pid) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        shipping_amount=50.0

        cart_product=[p for p in Cart.objects.all() if p.user == request.user]
      
        for p in cart_product:
            tempamount=(p.quantity * p.product.discount_price)
            amount+=tempamount
        
        dic={
            'quantity':c.quantity,
            'amount':amount,
            'shipping_amount':shipping_amount,
            'total_amount':amount + shipping_amount,
                }

        return JsonResponse(dic)

@login_required
def minus_cart(request):
    if request.method=='GET':
        pid=request.GET['prod_id']
        c=Cart.objects.get(Q(product=pid) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        shipping_amount=50.0
        cart_product=[p for p in Cart.objects.all()  if p.user==request.user]
        for o in cart_product:
            tempamount=(o.quantity * o.product.discount_price) 
            amount+=tempamount
        dic={
            'quantity':c.quantity,
            'amount':amount,
            'shipping_amount':shipping_amount,
            'total_amount':amount + shipping_amount,

        }
        return JsonResponse(dic)

@login_required
def remove_cart(request):
    if request.method=='GET':
        pid=request.GET['prod_id']
        c=Cart.objects.get(Q(product=pid) & Q(user=request.user))
        c.delete()
        amount=0.0
        shipping_amount=50.0
        cart_product=[p for p in Cart.objects.all()  if p.user==request.user]
        for o in cart_product:
            tempamount=(o.quantity * o.product.discount_price) 
            amount+=tempamount
        dic={
            'amount':amount,
            'shipping_amount':shipping_amount,
            'total_amount':amount + shipping_amount,

        }
        return JsonResponse(dic)

