from utils.api import APIView
from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer
from drf_yasg.utils import swagger_auto_schema


class AnnouncementAPI(APIView):
    @swagger_auto_schema(
        manual_parameters=[],
        operation_description="Get Announcement"
    )
    def get(self, request):
        announcements = Announcement.objects.filter(visible=True)
        return self.success(self.paginate_data(request, announcements, AnnouncementSerializer))
