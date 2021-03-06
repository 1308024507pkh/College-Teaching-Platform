# Generated by Django 3.0.3 on 2020-12-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='学工号')),
                ('user_password', models.CharField(default='123456', max_length=20, verbose_name='登录密码')),
                ('email', models.CharField(default='无', max_length=64, verbose_name='用户邮箱')),
                ('introduction', models.CharField(default='无', max_length=512, verbose_name='个人介绍')),
                ('user_kind', models.IntegerField(default=1, verbose_name='用户类型')),
                ('department', models.CharField(default='无', max_length=64, verbose_name='院系')),
                ('major_class', models.CharField(default='无', max_length=64, verbose_name='专业班级（为学生时有效）')),
                ('last_login_time', models.DateTimeField(verbose_name='最后登录时间')),
                ('homework_not_corrected', models.IntegerField(null=True, verbose_name='教师/助教未批改作业数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name_plural': '用户表',
                'db_table': 'User',
            },
        ),
    ]
