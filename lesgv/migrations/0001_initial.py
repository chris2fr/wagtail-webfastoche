# Generated by Django 5.0.9 on 2024-10-26 08:01

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="FaireMainPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("body", wagtail.fields.RichTextField(blank=True, null=True)),
                ("intro", wagtail.fields.RichTextField(blank=True, null=True)),
                ("footer1", wagtail.fields.RichTextField(blank=True, null=True)),
                ("footer2", wagtail.fields.RichTextField(blank=True, null=True)),
                ("redirect_url", models.URLField(blank=True, null=True)),
                (
                    "extramenu",
                    wagtail.fields.StreamField(
                        [("menu", 4)],
                        blank=True,
                        block_lookup={
                            0: ("wagtail.blocks.CharBlock", (), {}),
                            1: ("wagtail.blocks.URLBlock", (), {}),
                            2: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 0), ("url", 1)]],
                                {},
                            ),
                            3: ("wagtail.blocks.ListBlock", (2,), {"required": False}),
                            4: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 0), ("url", 1), ("submenu", 3)]],
                                {},
                            ),
                        },
                        null=True,
                    ),
                ),
                ("ghost_post_tag", models.SlugField(blank=True, null=True)),
                (
                    "theme",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("generique", "generique"),
                            ("boule", "boule"),
                            ("lesartsvoisins", "lesartsvoisins"),
                        ],
                        default="generique",
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="FaireMainAgendaItemPage",
            fields=[
                (
                    "fairemainpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="lesgv.fairemainpage",
                    ),
                ),
                ("start", models.DateField(blank=True, null=True)),
                ("end", models.DateField(blank=True, null=True)),
                ("place", models.CharField(blank=True, max_length=128, null=True)),
                ("place_url", models.URLField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("lesgv.fairemainpage",),
        ),
        migrations.CreateModel(
            name="FaireMainHomePage",
            fields=[
                (
                    "fairemainpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="lesgv.fairemainpage",
                    ),
                ),
                ("agenda", wagtail.fields.RichTextField(blank=True, null=True)),
                ("ghost_tag", models.CharField(blank=True, max_length=32, null=True)),
                (
                    "ghost_filter",
                    models.CharField(blank=True, max_length=32, null=True),
                ),
                ("ghost_order", models.CharField(blank=True, max_length=32, null=True)),
                ("ghost_limit", models.CharField(blank=True, max_length=8, null=True)),
                (
                    "ghost_include",
                    models.CharField(blank=True, max_length=32, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("lesgv.fairemainpage",),
        ),
        migrations.CreateModel(
            name="FaireMainMenu",
            fields=[
                (
                    "fairemainpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="lesgv.fairemainpage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("lesgv.fairemainpage",),
        ),
        migrations.CreateModel(
            name="WagtailSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("homepage_link", models.URLField(blank=True, null=True)),
                ("footer1", wagtail.fields.RichTextField(blank=True, null=True)),
                ("footer2", wagtail.fields.RichTextField(blank=True, null=True)),
                (
                    "theme",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("generique", "generique"),
                            ("boule", "boule"),
                            ("lesartsvoisins", "lesartsvoisins"),
                        ],
                        default="generique",
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "menu",
                    wagtail.fields.StreamField(
                        [("menu", 4)],
                        blank=True,
                        block_lookup={
                            0: ("wagtail.blocks.CharBlock", (), {}),
                            1: ("wagtail.blocks.URLBlock", (), {}),
                            2: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 0), ("url", 1)]],
                                {},
                            ),
                            3: ("wagtail.blocks.ListBlock", (2,), {"required": False}),
                            4: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 0), ("url", 1), ("submenu", 3)]],
                                {},
                            ),
                        },
                        null=True,
                    ),
                ),
                (
                    "site_logo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Default Settings for All Websites",
            },
        ),
        migrations.CreateModel(
            name="WebsiteSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("homepage_link", models.URLField(blank=True, null=True)),
                ("footer1", wagtail.fields.RichTextField(blank=True, null=True)),
                ("footer2", wagtail.fields.RichTextField(blank=True, null=True)),
                (
                    "menu",
                    wagtail.fields.StreamField(
                        [("menu", 4)],
                        blank=True,
                        block_lookup={
                            0: ("wagtail.blocks.CharBlock", (), {}),
                            1: ("wagtail.blocks.URLBlock", (), {}),
                            2: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 0), ("url", 1)]],
                                {},
                            ),
                            3: ("wagtail.blocks.ListBlock", (2,), {"required": False}),
                            4: (
                                "wagtail.blocks.StructBlock",
                                [[("label", 0), ("url", 1), ("submenu", 3)]],
                                {},
                            ),
                        },
                        null=True,
                    ),
                ),
                (
                    "theme",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("generique", "generique"),
                            ("boule", "boule"),
                            ("lesartsvoisins", "lesartsvoisins"),
                        ],
                        default="generique",
                        max_length=32,
                        null=True,
                    ),
                ),
                ("csscolors", models.TextField(blank=True, null=True)),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
                (
                    "site_logo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Settings Per Website",
            },
        ),
        migrations.CreateModel(
            name="RelatedAgendaItemHomePage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "agenda_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="lesgv.fairemainagendaitempage",
                    ),
                ),
                (
                    "home_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agenda_home",
                        to="lesgv.fairemainhomepage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
