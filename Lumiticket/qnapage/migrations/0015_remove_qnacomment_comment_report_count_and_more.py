# Generated by Django 4.2 on 2023-06-28 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "qnapage",
            "0014_rename_report_count_qnacomment_comment_report_count_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="qnacomment",
            name="comment_report_count",
        ),
        migrations.RemoveField(
            model_name="qnareply",
            name="reply_report_count",
        ),
    ]
