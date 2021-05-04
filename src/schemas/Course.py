from src import mm


class CoursesSchema(mm.SQLAlchemySchema):
    class Meta:
        fields = ('course_id',
                  'course_name',
                  'course_description',
                  'course_start_date',
                  'course_end_date',
                  'course_lectures')
