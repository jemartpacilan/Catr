from rest_framework import routers
from registration.viewsets import CatererViewSet,\
    ConsumerViewSet,\
    CatrUserViewSet,\
    MenuViewSet,\
    ItemViewSet,\
    TransactionViewSet,\
    PackageViewSet,\
    ImageViewSet
from orders.viewsets import CourseViewSet,\
    TrayViewSet,\
    HistoryViewSet
from review.viewsets import ReviewViewSet,\
    QuestionViewSet,\
    AnswerViewSet


# router object is used to register routes from the
# consumable api
router = routers.DefaultRouter()

# all caterers can then be queried at '/api/caterers'
# once server is run
router.register(r'caterers', CatererViewSet)
router.register(r'consumers', ConsumerViewSet)
router.register(r'catrusers', CatrUserViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'items', ItemViewSet)
router.register(r'images', ImageViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'trays', TrayViewSet)
router.register(r'histories', HistoryViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
