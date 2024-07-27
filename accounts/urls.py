from django.urls import path
import accounts.views as v
urlpatterns = [
    path("login/",v.UserLoginView.as_view(),name="login"),
    path("signup/",v.UserSignUpView.as_view(),name="signup"),
    path("profile/",v.ProfileView.as_view(),name="profile"),
    path("logout/",v.logout_view,name="logout"),
    path("profile/edit",v.ProfileEditView.as_view(),name='profile_edit'),
    path("password_change/",v.MyPasswordChangeView.as_view(),name="password_change"),
    path("password_change/done",v.MyPasswordChangeDoneView.as_view(),name="password_change_done"),
    path("password_reset/",v.MyPasswordResetView.as_view(),name="password_reset"),
    path("password_reset/done",v.MyPasswordResetDoneView.as_view(),name="password_reset_done"),
    path("password_reset/<uidb64>/<token>",v.MyPasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("password_reset/complete",v.MyPasswordResetCompleteView.as_view(),name="password_reset_complete"),
]