# Generated by Django 3.0.6 on 2020-06-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeptideSeq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Protein_found', models.CharField(max_length=10)),
                ('Recommended_Protein_Name', models.CharField(max_length=200)),
                ('Species', models.CharField(max_length=50)),
                ('Chromosome', models.CharField(max_length=10)),
                ('Accession', models.CharField(max_length=30)),
                ('Input_Sequence', models.CharField(max_length=100)),
                ('P1_Position', models.CharField(max_length=4)),
                ('Cleaving_proteases', models.CharField(max_length=4)),
            ],
            options={
                'ordering': ['Input_Sequence'],
            },
        ),
    ]
