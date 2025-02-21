# Administration Urls.py

from django.urls import path,  reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'administration'

urlpatterns = [

    # added on 04-09-2024 for Password Reset And Change Functionality
    #this url will display the page to enter email for getting the link to reset password
    #the email link will call password_reset_confirm page 
    path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='app00Administration/03_password_reset/03_password_reset.html',
            email_template_name='app00Administration/03_password_reset/07_password_reset_email.html',
            success_url=reverse_lazy('administration:password_reset_email_sent'),
        ), name='password_reset'),
    
    #this will diaplay page that email have been send
    #changes done on 09-01-2025
    path('password_reset_email_sent/done', auth_views.PasswordResetDoneView.as_view(
            template_name = 'app00Administration/03_password_reset/04_password_reset_email_sent.html'
        ), name='password_reset_email_sent'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name = 'app00Administration/03_password_reset/05_password_reset_confirm.html',
            success_url=reverse_lazy('administration:password_reset_complete')
        ), name='password_reset_confirm'),
    
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='app00Administration/03_password_reset/06_password_reset_complete.html'
        ), name='password_reset_complete'),
    
    path('change-password/', auth_views.PasswordChangeView.as_view(
            template_name='app00Administration/03_password_reset/01_password_change.html',
            success_url=reverse_lazy('administration:password_change_done')
        ), name='password_change'),
    
    path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(
            template_name='app00Administration/03_password_reset/02_password_change_done.html'
        ), name='password_change_done'),
    
]
