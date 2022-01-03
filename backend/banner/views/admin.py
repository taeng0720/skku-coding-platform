from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from banner.models import Banner
from banner.serializers import (BannerAdminSerializer, CreateBannerSerializer, EditBannerSerializer)
from utils.api import APIView, validate_serializer
from utils.decorators import super_admin_required
from utils.shortcuts import check_is_id


class BannerAdminAPI(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="id", in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="unique banner id",
            )
        ],
        operation_description="Get Banner image"
    )
    @validate_serializer(BannerAdminSerializer)
    @super_admin_required
    def get(self, request):
        banner_id = request.GET.get("id")
        # get single banner image
        if banner_id:
            if not id or not check_is_id(id):
                return self.error("Invalid parameter, id is required")
            try:
                banner = Banner.objects.get(id=banner_id)
                return self.success(BannerAdminSerializer(banner).data)
            except Banner.DoesNotExist:
                return self.error("Banner does not exist")
        # get all banner images
        else:
            banners = Banner.objects.all()
            return self.success(BannerAdminSerializer(banners).data)

    @swagger_auto_schema(
        request_body=CreateBannerSerializer,
        operation_description="Create new Banner image",
        responses={200: BannerAdminSerializer},
    )
    @validate_serializer(CreateBannerSerializer)
    @super_admin_required
    def post(self, request):
        data = request.data
        banner = Banner.objects.create(title=data["title"],
                                       path=data["path"])
        return self.success(BannerAdminSerializer(banner).data)

    @swagger_auto_schema(
        request_body=EditBannerSerializer,
        operation_description="Edit Banner image"
    )
    @validate_serializer(EditBannerSerializer)
    @super_admin_required
    def put(self, request):
        data = request.data
        try:
            banner = Banner.objects.get(id=data.pop("id"))
        except Banner.DoesNotExist:
            return self.error("Banner does not exist")

        for k, v in data.items():
            setattr(banner, k, v)
        banner.save()

        return self.success(BannerAdminSerializer(banner).data)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="id", in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="unique banner id",
            ),
        ],
        operation_description="Delete Banner Image"
    )
    @super_admin_required
    def delete(self, request):
        id = request.GET.get("id")
        if not id:
            return self.error("Invalid Parameter, id is required")
        Banner.objects.filter(id__in=id).delete()
        return self.success()
