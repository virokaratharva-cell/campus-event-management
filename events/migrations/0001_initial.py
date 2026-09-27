from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("location", models.CharField(max_length=200)),
                ("organizer", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("capacity", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
