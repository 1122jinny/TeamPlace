# Generated by Django 2.1.1 on 2018-12-06 01:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('cal_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('start', models.CharField(max_length=50)),
                ('end', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('participate', models.IntegerField(default=100)),
                ('role', models.CharField(default='역할', max_length=50)),
                ('is_leader', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('par_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.Member')),
            ],
        ),
        migrations.CreateModel(
            name='TR',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.CharField(default='프로젝트', max_length=50)),
                ('subject', models.CharField(default='과목', max_length=50)),
                ('team', models.CharField(default='팀', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(null=True, upload_to='')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.Member')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.TR')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_name', models.CharField(default='', max_length=50)),
                ('user_id', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('user_psw', models.CharField(default='', max_length=50)),
                ('user_email', models.CharField(default='', max_length=50)),
                ('user_pos', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.TR'),
        ),
        migrations.AddField(
            model_name='participate',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.TR'),
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='sow_app.UserInfo'),
        ),
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='sow_app.UserInfo'),
        ),
        migrations.AddField(
            model_name='notification',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.TR'),
        ),
        migrations.AddField(
            model_name='notice',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.TR'),
        ),
        migrations.AddField(
            model_name='member',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.TR'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.UserInfo'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow_app.TR'),
        ),
    ]
