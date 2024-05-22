from django.db import models


class AreaTable(models.Model):
    area_id = models.AutoField(primary_key=True, blank=True, null=False)
    area_name = models.TextField(blank=True, null=True)
    township_name = models.TextField(blank=True, null=True)
    government_id = models.IntegerField(blank=True, null=True)
    government_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Area_Table'


class SchoolKindTable(models.Model):
    school_kind_id = models.AutoField(primary_key=True, blank=True, null=False)
    school_kind_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'School_Kind_Table'


class SchoolTypeTable(models.Model):
    school_type_id = models.AutoField(primary_key=True, blank=True, null=False)
    school_type_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'School_Type_Table'


class SubjectTable(models.Model):
    subject_id = models.AutoField(primary_key=True, blank=True, null=False)
    subject_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Subject_Table'


class TownTypeTable(models.Model):
    town_type_id = models.AutoField(primary_key=True, blank=True, null=False)
    town_type_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Town_Type_Table'


class SchoolTable(models.Model):
    school_id = models.TextField(primary_key=True, blank=True, null=False)
    school_code = models.IntegerField(db_column='school_CODE', blank=True, null=True, unique=True)  # Field name made lowercase.
    law_address = models.TextField(blank=True, null=True)
    school_name = models.TextField(blank=True, null=True)
    school_kind = models.ForeignKey('SchoolKindTable', models.DO_NOTHING, blank=True, null=True)
    school_type = models.ForeignKey('SchoolTypeTable', models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey('AreaTable', models.DO_NOTHING, blank=True, null=True)
    town_type = models.ForeignKey('TownTypeTable', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'School_Table'


class SchoolStudentTable(models.Model):
    student_id = models.TextField(primary_key=True, blank=True, null=False)
    school_code = models.ForeignKey('SchoolTable', models.DO_NOTHING, db_column='school_CODE', to_field='school_code', blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'School_Student_Table'


class SubjectFormTable(models.Model):
    subject_form_id = models.AutoField(primary_key=True, blank=True, null=False)
    subject = models.ForeignKey('SubjectTable', models.DO_NOTHING, blank=True, null=True)
    year_of_exam = models.IntegerField(blank=True, null=True)
    a_tasks_count = models.IntegerField(db_column='A_tasks_count', blank=True, null=True)  # Field name made lowercase.
    b_tasks_count = models.IntegerField(db_column='B_tasks_count', blank=True, null=True)  # Field name made lowercase.
    c_tasks_count = models.IntegerField(db_column='C_tasks_count', blank=True, null=True)  # Field name made lowercase.
    d_tasks_count = models.IntegerField(db_column='D_tasks_count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Subject_Form_Table'


class ResultTable(models.Model):
    result_id = models.TextField(primary_key=True, blank=True, null=False)
    student = models.ForeignKey('SchoolStudentTable', models.DO_NOTHING, blank=True, null=True)
    subject_form = models.ForeignKey('SubjectFormTable', models.DO_NOTHING, blank=True, null=True)
    primary_score = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    score_100 = models.IntegerField(blank=True, null=True)
    result_5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Result_Table'


class TaskTable(models.Model):
    task_id = models.TextField(primary_key=True, blank=True, null=False)
    result = models.ForeignKey('ResultTable', models.DO_NOTHING, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Task_Table'