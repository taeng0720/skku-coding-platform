from utils.api import APIView, validate_serializer

from ..models import Assignment
from course.models import Course
from ..serializers import AssginmentProfessorSerializer, CreateAssignmentSerializer, EditAssignmentSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from account.decorators import ensure_created_by, admin_role_required
import dateutil.parser

class AssignmentAPI(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="course_id",
                in_=openapi.IN_QUERY,
                description="Unique ID of a course",
                required=True,
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                name="assignment_id",
                in_=openapi.IN_QUERY,
                description="Unique ID of a assignment",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                name="limit",
                in_=openapi.IN_QUERY,
                description="Number of contests to show",
                type=openapi.TYPE_STRING,
                default=10,
            ),
            openapi.Parameter(
                name="offset",
                in_=openapi.IN_QUERY,
                description="ID of the first contest of list",
                type=openapi.TYPE_STRING,
                default=0,
            ),
        ],
        operation_description="Get assignment list of the course generated by requesting admin",
        responses={200: AssginmentProfessorSerializer},
    )
    @admin_role_required
    def get(self, request):
        assignment_id = request.GET.get("assignment_id")
        course_id = request.GET.get("course_id")

        if not course_id:
            return self.error("Invalid parameter, course_id is required")

        try:
            course = Course.objects.get(id=course_id)
            ensure_created_by(course, request.user)
        except Course.DoesNotExist:
            return self.error("Course does not exist")

        if assignment_id:
            try:
                assignment = Assignment.objects.get(id=assignment_id, course_id=course_id)
                return self.success(AssginmentProfessorSerializer(assignment).data)
            except Assignment.DoesNotExist:
                return self.error("Assignment does not exists")

        assignments = Assignment.objects.filter(course_id=course_id)
        return self.success(self.paginate_data(request, assignments, AssginmentProfessorSerializer))
    
    @swagger_auto_schema(
        request_body=CreateAssignmentSerializer,
        operation_description="Create one assignment",
        responses={200: AssginmentProfessorSerializer},
    )
    @validate_serializer(CreateAssignmentSerializer)
    @admin_role_required
    def post(self, request):
        data = request.data
        course_id = request.data["course_id"]

        try:
            course = Course.objects.get(id=course_id)
            ensure_created_by(course, request.user)
        except Course.DoesNotExist:
            return self.error("Course does not exists")
        data["start_time"] = dateutil.parser.parse(data["start_time"])
        data["end_time"] = dateutil.parser.parse(data["end_time"])
        data["created_by"] = request.user

        if data["end_time"] <= data["start_time"]:
            return self.error("Start time must occur earlier than end time")

        assignment = Assignment.objects.create(**data)
        return self.success(AssginmentProfessorSerializer(assignment).data)

    @swagger_auto_schema(
        request_body=EditAssignmentSerializer,
        operation_description="Update assignment",
        responses={200: AssginmentProfessorSerializer},
    )
    @validate_serializer(EditAssignmentSerializer)
    @admin_role_required
    def put(self, request):
        data = request.data
        try:
            assignment = Assignment.objects.get(id=data.pop("id"))
            ensure_created_by(assignment, request.user)
        except Assignment.DoesNotExist:
            return self.error("Assignment does not exist")

        data["start_time"] = dateutil.parser.parse(data["start_time"])
        data["end_time"] = dateutil.parser.parse(data["end_time"])

        if data["end_time"] <= data["start_time"]:
            return self.error("Start time must occur earlier than end time")

        for k, v in data.items():
            setattr(assignment, k, v)
        assignment.save()
        return self.success(AssginmentProfessorSerializer(assignment).data)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="course_id",
                in_=openapi.IN_QUERY,
                description="Id of course",
                required=True,
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                name="assignment_id",
                in_=openapi.IN_QUERY,
                description="Id of assignment to delete",
                required=True,
                type=openapi.TYPE_INTEGER,
            )
        ],
        operation_description="Delete one contest announcement",
    )
    @admin_role_required
    def delete(self, request):
        course_id = request.GET.get("course_id")
        assignment_id = request.GET.get("assignment_id")

        if not course_id:
            return self.error("Invalid parameter, course_id is required")
        if not assignment_id:
            return self.error("Invalid parameter, assignment_id is required")

        try:
            course = Course.objects.get(id=course_id)
            ensure_created_by(course, request.user)
        except Course.DoesNotExist:
            return self.error("Course does not exist")

        try:
            assignment = Assignment.objects.get(id=assignment_id)
            ensure_created_by(assignment, request.user)
        except Assignment.DoesNotExist:
            return self.error("Assignment does not exists")

        assignment.delete()
        return self.success()
