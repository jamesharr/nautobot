# Generated by Django 3.1.7 on 2021-04-01 06:35

from django.db import migrations, models
import django.db.models.deletion
import nautobot.extras.models.statuses
import nautobot.extras.utils
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("tenancy", "0001_initial"),
        ("virtualization", "0001_initial"),
        ("dcim", "0003_initial_part_3"),
        ("extras", "0002_initial_part_2"),
        ("ipam", "0001_initial_part_1"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="cluster",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="devices",
                to="virtualization.cluster",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="device_role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="devices", to="dcim.devicerole"
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="instances", to="dcim.devicetype"
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="local_context_data_owner_content_type",
            field=models.ForeignKey(
                blank=True,
                default=None,
                limit_choices_to=nautobot.extras.utils.FeatureQuery("config_context_owners"),
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="platform",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="devices",
                to="dcim.platform",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="primary_ip4",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="primary_ip4_for",
                to="ipam.ipaddress",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="primary_ip6",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="primary_ip6_for",
                to="ipam.ipaddress",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="rack",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="devices",
                to="dcim.rack",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="devices", to="dcim.site"
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="dcim_device_related",
                to="extras.status",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="device",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="devices",
                to="tenancy.tenant",
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="virtual_chassis",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="members",
                to="dcim.virtualchassis",
            ),
        ),
        migrations.AddField(
            model_name="consoleserverporttemplate",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consoleserverporttemplates",
                to="dcim.devicetype",
            ),
        ),
        migrations.AddField(
            model_name="consoleserverport",
            name="_cable_peer_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="consoleserverport",
            name="_path",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.cablepath"
            ),
        ),
        migrations.AddField(
            model_name="consoleserverport",
            name="cable",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="dcim.cable"
            ),
        ),
        migrations.AddField(
            model_name="consoleserverport",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="consoleserverports", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="consoleserverport",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="consoleporttemplate",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="consoleporttemplates", to="dcim.devicetype"
            ),
        ),
        migrations.AddField(
            model_name="consoleport",
            name="_cable_peer_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="consoleport",
            name="_path",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.cablepath"
            ),
        ),
        migrations.AddField(
            model_name="consoleport",
            name="cable",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="dcim.cable"
            ),
        ),
        migrations.AddField(
            model_name="consoleport",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="consoleports", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="consoleport",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="cablepath",
            name="destination_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="cablepath",
            name="origin_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="+", to="contenttypes.contenttype"
            ),
        ),
        migrations.AddField(
            model_name="cable",
            name="_termination_a_device",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="+", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="cable",
            name="_termination_b_device",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="+", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="cable",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="dcim_cable_related",
                to="extras.status",
            ),
        ),
        migrations.AddField(
            model_name="cable",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="cable",
            name="termination_a_type",
            field=models.ForeignKey(
                limit_choices_to=models.Q(
                    models.Q(
                        models.Q(("app_label", "circuits"), ("model__in", ("circuittermination",))),
                        models.Q(
                            ("app_label", "dcim"),
                            (
                                "model__in",
                                (
                                    "consoleport",
                                    "consoleserverport",
                                    "frontport",
                                    "interface",
                                    "powerfeed",
                                    "poweroutlet",
                                    "powerport",
                                    "rearport",
                                ),
                            ),
                        ),
                        _connector="OR",
                    )
                ),
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="cable",
            name="termination_b_type",
            field=models.ForeignKey(
                limit_choices_to=models.Q(
                    models.Q(
                        models.Q(("app_label", "circuits"), ("model__in", ("circuittermination",))),
                        models.Q(
                            ("app_label", "dcim"),
                            (
                                "model__in",
                                (
                                    "consoleport",
                                    "consoleserverport",
                                    "frontport",
                                    "interface",
                                    "powerfeed",
                                    "poweroutlet",
                                    "powerport",
                                    "rearport",
                                ),
                            ),
                        ),
                        _connector="OR",
                    )
                ),
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="rearporttemplate",
            unique_together={("device_type", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="rearport",
            unique_together={("device", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="rackgroup",
            unique_together={("site", "slug"), ("site", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="rack",
            unique_together={("group", "facility_id"), ("group", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="powerporttemplate",
            unique_together={("device_type", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="powerport",
            unique_together={("device", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="powerpanel",
            unique_together={("site", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="poweroutlettemplate",
            unique_together={("device_type", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="poweroutlet",
            unique_together={("device", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="powerfeed",
            unique_together={("power_panel", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="inventoryitem",
            unique_together={("device", "parent", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="interfacetemplate",
            unique_together={("device_type", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="interface",
            unique_together={("device", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="frontporttemplate",
            unique_together={("device_type", "name"), ("rear_port", "rear_port_position")},
        ),
        migrations.AlterUniqueTogether(
            name="frontport",
            unique_together={("rear_port", "rear_port_position"), ("device", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="devicetype",
            unique_together={("manufacturer", "model"), ("manufacturer", "slug")},
        ),
        migrations.AlterUniqueTogether(
            name="devicebaytemplate",
            unique_together={("device_type", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="devicebay",
            unique_together={("device", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="device",
            unique_together={
                ("rack", "position", "face"),
                ("virtual_chassis", "vc_position"),
                ("site", "tenant", "name"),
            },
        ),
        migrations.AlterUniqueTogether(
            name="consoleserverporttemplate",
            unique_together={("device_type", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="consoleserverport",
            unique_together={("device", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="consoleporttemplate",
            unique_together={("device_type", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="consoleport",
            unique_together={("device", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="cablepath",
            unique_together={("origin_type", "origin_id")},
        ),
        migrations.AlterUniqueTogether(
            name="cable",
            unique_together={("termination_b_type", "termination_b_id"), ("termination_a_type", "termination_a_id")},
        ),
    ]
