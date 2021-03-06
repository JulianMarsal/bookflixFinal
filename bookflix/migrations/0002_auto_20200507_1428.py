# Generated by Django 3.0.6 on 2020-05-07 17:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='plan',
            field=models.CharField(choices=[('1', 'free'), ('2', 'normal'), ('4', 'premium'), ('9', 'admin')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pleasures_author',
            field=models.ManyToManyField(blank=True, null=True, to='bookflix.Author'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pleasures_editorial',
            field=models.ManyToManyField(blank=True, null=True, to='bookflix.Editorial'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pleasures_gender',
            field=models.ManyToManyField(blank=True, null=True, to='bookflix.Gender'),
        ),
        migrations.CreateModel(
            name='UserSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_solicitud', models.CharField(choices=[('1', 'alta'), ('2', 'cambio'), ('4', 'baja')], default='1', max_length=2)),
                ('type_of_plan', models.CharField(choices=[('f', 'free'), ('n', 'normal'), ('p', 'premium')], default='f', max_length=2)),
                ('date_of_solicitud', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_limit_to_attend', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Account')),
            ],
        ),
        migrations.CreateModel(
            name='StateOfBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('state', models.CharField(choices=[('10', 'reading'), ('20', 'future_reading'), ('30', 'finished')], default='30', max_length=2)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Book')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile')),
            ],
        ),
    ]
