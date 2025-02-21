from django.shortcuts import render
from django.contrib.auth.views import LogoutView,LoginView

from .forms import CustomAuthenticationForm

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'app00Administration/00_login.html'
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        # UserLoginDetails.objects.create(
        #     login_user=user,
        #     login_time=timezone.now(),  
        #     accepted_terms_and_conditions=True  
        # )
        # # Delete module data on successful login
        # userAttObject = UserAttributes.objects.get(id=user.id)
        # try:
        #     config = nexiaIntelligenceConfigs.objects.get(user_id=userAttObject)
        #     delete_module_data(userAttObject, config.current_app)
        #     config.delete()
        # except nexiaIntelligenceConfigs.DoesNotExist:
        #     print("No existing configuration for user", user.id)
        
        # try:
        #     #in success case Clear all login attempts for the user's IP address
        #     ip, is_routable = get_client_ip(self.request)
        #     if ip:
        #         print("in success case Clearing all login attempts for the user's IP address")
        #         AccessAttempt.objects.filter(ip_address=ip).delete()
        # except Exception as e:
        #     print("An error occurred in CustomLoginView form_valid while clearing login attempts for IP",str(e))

        return response
    
    def form_invalid(self, form):
        errors = form.errors.as_data()
        print("Form CustomLoginView validation errors for user ", self.request.user.id, " : ", errors)
        for field in form.fields:
            form.fields[field].widget.attrs['class'] = 'form-control is-invalid'

        
        response = super().form_invalid(form)
        return response
    
    def get(self, request, *args, **kwargs):
        print("=========================inside login GET===================\n")
        print("Session Data: ", request.session.items())
        
        # ip, is_routable = get_client_ip(request)
                
        # # this is to make sure that Ip is unblocked after 1 hour
        # self.clear_expired_attempts(ip)
        # if ip:
        #      # Check the latest attempt time
        #     latest_attempt = AccessAttempt.objects.filter(ip_address=ip).order_by('-attempt_time').first()
        #     if latest_attempt and (timezone.now() - latest_attempt.attempt_time )<= timezone.timedelta(hours=1):
        #         attempts_sum = AccessAttempt.objects.filter(ip_address=ip).aggregate(total_failures=Sum('failures_since_start'))['total_failures']

        #         # Check if the sum is greater than or equal to 6
        #         if attempts_sum is not None and attempts_sum >= 6:
        #             print(f"Login blocked for IP: {ip}")
        #             return self.block_request(request)
               
        
        return super().get(request, *args, **kwargs)
        
    # @staticmethod
    # def clear_expired_attempts(ip):
    #     latest_attempt = AccessAttempt.objects.filter(ip_address=ip).order_by('-attempt_time').first()
    #     if latest_attempt and timezone.now() - latest_attempt.attempt_time > timezone.timedelta(hours=1):
    #         print("Clearing expired attempts for IP:", ip)
    #         AccessAttempt.objects.filter(ip_address=ip).delete()

    # def block_request(self, request):
    #     return render(request, '04_nexia_intelligence_lockout_IP.html')

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        print("inside CustomLogoutView for user ",request.user.id)
        # userAttObject=UserAttributes.objects.get(id=request.user.id)
        # try:
        #     config = nexiaIntelligenceConfigs.objects.get(user_id=userAttObject)
        #     delete_module_data(userAttObject, config.current_app)
        #     config.delete()
            
        # except nexiaIntelligenceConfigs.DoesNotExist:
        #     print("inside CustomLogoutView nexiaIntelligenceConfigs does not exist for user ",request.user.id)

        response = super().dispatch(request, *args, **kwargs)
        # print("outsiding  CustomLogoutView ")
        return response
    