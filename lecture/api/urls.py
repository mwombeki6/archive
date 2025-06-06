from django.urls import path
from .views import (
    registerView,
    get_csrf,
    loginView,
    WhoAmIView,
    LectureOnlyView,
    check_auth,
    logoutView,
    update_account,
    delete_account,
    LectureView,
    AssignmentListCreateView,
    AssignmentRetrieveUpdateDestroyView,
    AssignmentSubmissionListView,
    AssignmentSubmissionFeedbackView,
)

urlpatterns = [
    path("csrf_cookie", get_csrf),
    path("check_auth", check_auth),
    path("register", registerView),
    path("login", loginView),
    path("get_user", WhoAmIView.as_view()),
    path('retrieve_user/<username>', LectureView.as_view({'get': 'retrieve'})),
    path("lecture_dashboard", LectureOnlyView.as_view()),
    path("logout", logoutView),
    path("update", update_account),
    path("delete", delete_account),
    path('assignments/', AssignmentListCreateView.as_view(), name='lecturer-assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentRetrieveUpdateDestroyView.as_view(), name='lecturer-assignment-detail'),
    path('submissions/', AssignmentSubmissionListView.as_view(), name='lecturer-submission-list'),
    path('submissions/<int:pk>/feedback/', AssignmentSubmissionFeedbackView.as_view(), name='lecturer-submission-feedback'),
]