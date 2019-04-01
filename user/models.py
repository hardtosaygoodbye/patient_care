from django.db.models import *
from uuid import uuid4

class User(Model):
    username = CharField('姓名', max_length = 10)
    password = CharField('密码', max_length = 10)
    def __str__(self):
        return self.username

class Authority(Model):
    user = OneToOneField(User, on_delete = CASCADE, primary_key = True)
    token = UUIDField(default = uuid4)

class Hospital(Model):
    name = CharField('医院名称', max_length = 20)

class Carer(Model):
    name = CharField('护工姓名', max_length = 20)
    hospital = ForeignKey(Hospital, on_delete = CASCADE)
    hospital_score = DecimalField('医院均分', max_digits = 10,\
    decimal_places = 2, default = 0.0)
    hospital_num = IntegerField(default = 0)
    patient_score = DecimalField('病人均分', max_digits = 10,\
    decimal_places = 2, default = 0.0)
    patient_num = IntegerField(default = 0)
    family_score = DecimalField('家属均分', max_digits = 10,\
    decimal_places = 2, default = 0.0)
    family_num = IntegerField(default = 0)
    total_score = DecimalField('总分', max_digits = 10,\
    decimal_places = 2, default = 0.0)

class Evaluation(Model):
    user = ForeignKey(User, on_delete = CASCADE)
    carer = ForeignKey(Carer, on_delete = CASCADE)
    q1 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q2 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q3 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q4 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q5 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q6 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q7 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q8 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q9 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q10 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q11 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q12 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q13 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q14 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q15 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q16 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q17 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    q18 = DecimalField('护工美吗？', max_digits = 10, decimal_places = 2)
    tip = TextField('建议', max_length = 100)
    side = IntegerField('方', default = 0)

class Suggestion(Model):
    user = ForeignKey(User, on_delete = CASCADE)
    msg = TextField('意见', max_length = 100)


