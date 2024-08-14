# Generated by Django 4.2.13 on 2024-07-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_tasks_database", "0004_dbtaskresult_started_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dbtaskresult",
            name="priority",
            field=models.IntegerField(default=0),
        ),
        migrations.AddConstraint(
            model_name="dbtaskresult",
            constraint=models.CheckConstraint(
                check=models.Q(("priority__range", (-100, 100))), name="priority_range"
            ),
        ),
    ]
