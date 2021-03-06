# Generated by Django 3.2 on 2022-04-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_alter_servicecategory_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitem',
            name='icon',
            field=models.CharField(blank=True, choices=[('fa-microscope', 'Microscope'), ('fa-teeth', 'Teeth'), ('fa-bone-break', 'Bone Break'), ('fa-scalpel-path', 'Scalpel Path'), ('fa-head-side-brain', 'Head Side Brain'), ('fa-heart-rate', 'Hearth Rate'), ('cagri-merkezi.svg', 'Cagri Merkezi'), ('dental-1.svg', 'Dental 1'), ('dis-koruma.svg', 'Dis Koruma'), ('dis-muayene.svg', 'Dis Muayene'), ('hollywood-smile.svg', 'Hollywood Smile'), ('implant-tedavisi.svg', 'Implant Tedavisi'), ('orthodonti.svg', 'Orthodonti'), ('orthodonti-2.svg', 'Orthodonti 2'), ('teeth-1.svg', 'Teeth 1'), ('teeth-2.svg', 'Teeth 2'), ('teeth-3.svg', 'Teeth 3'), ('teeth-4.svg', 'Teeth 4'), ('teeth-5.svg', 'Teeth 5'), ('teeth-6.svg', 'Teeth 6'), ('tomografi.svg', 'Tomografi')], max_length=50, null=True, verbose_name='Category Icon'),
        ),
    ]
