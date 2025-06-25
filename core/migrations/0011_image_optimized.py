from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_adress_customer_address_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='optimized',
            field=models.ImageField(blank=True, upload_to='optimized/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
