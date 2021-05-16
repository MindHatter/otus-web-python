import graphene
from graphene_django import DjangoObjectType

from .models import Subject, Course, Module
from django.contrib.auth.models import User



class TeacherType(DjangoObjectType):
    class Meta:
        model = User


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class StudentType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    all_teachers = graphene.List(of_type=TeacherType)
    # all_course = graphene.List(of_type=CourseType)
    all_students = graphene.List(of_type=StudentType)

    course = graphene.Field(CourseType, id=graphene.Int(), title=graphene.String())

    def resolve_all_teachers(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_students(self, info, **kwargs):
        return User.objects.all()

    def resolve_course(self, info, **kwargs):
        if kwargs['id']:
            return Course.objects.get(id=kwargs['id'])

schema = graphene.Schema(query=Query)