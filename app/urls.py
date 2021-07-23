from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib.auth import views as auth_views
from .forms import login_form,MypasswordchangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('', views.homeView.as_view(),name='home'),
    path('product-detail/<int:id>', views.product_detail_View.as_view(), name='product-detail'),
    path('profile/', views.Profile_View.as_view(), name='profile'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('show-cart/', views.show_cart, name='show-cart'),

   
    path('address/', views.address, name='address'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('topware/', views.topware, name='topware'),
    path('topware/<slug:data>', views.topware, name='topwaredata'),
    path('bottomware/', views.bottomware, name='bottomware'),
    path('bottomware/<slug:data>', views.bottomware, name='bottomwaredata'),

 # registration
    path('registration/', views.user_regi_View.as_view(),name='customerregistration'),

  #loging logout
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form= login_form ) , name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


   # password change 

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MypasswordchangeForm,success_url='/passwordchnagedone/'),name='passwordchange'),
    path('passwordchnagedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchnagedone'),

   #forget password
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),

    path('pluscart/', views.pluscart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
   
    path('checkout/', views.checkout, name='checkout'), 
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('orders/', views.orders, name='orders'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
