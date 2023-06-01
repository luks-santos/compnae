from django.urls import include, path

from . import views

from django.contrib.auth import views as auth_views
from .forms import PasswordResetForm

urlpatterns = [
    path('', views.logar_usuario, name='home'),
    path('login/',views.logar_usuario, name='login'), # acesso para login
    path('logout/', views.logout_user, name='logout'), # logout de usuário
    path('cadastro/fornecedor/', views.cadastrar_fornecedor, name='cadastro_fornecedor'), # registro de fornecedores
 
    path('servidor/', include('servidor.urls'), name='servidor'), #Home do servidor
    path('fornecedor/', include('fornecedor.urls'), name='fornecedor'), #Home do fornecedor

    #recuperação de senha
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html", form_class=PasswordResetForm), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name = "password_reset_complete"),
]
