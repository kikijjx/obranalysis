from django.contrib import admin
from .models import TownTypeTable
from .models import AreaTable
from .models import ResultTable
from .models import SchoolTable
from .models import SubjectTable
from .models import SubjectFormTable
from .models import TaskTable
from .models import SchoolTypeTable
from .models import SchoolKindTable
from .models import SchoolStudentTable

# Register your models here.

admin.site.register(TownTypeTable)
admin.site.register(AreaTable)
admin.site.register(ResultTable)
admin.site.register(SchoolTable)
admin.site.register(SubjectTable)
admin.site.register(SubjectFormTable)
admin.site.register(TaskTable)
admin.site.register(SchoolKindTable)
admin.site.register(SchoolTypeTable)
admin.site.register(SchoolStudentTable)