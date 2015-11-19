# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(unique=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'django_site'

class NytNotification(models.Model):
    id = models.IntegerField(primary_key=True)
    subscription = models.ForeignKey('NytSubscription', blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    message = models.TextField()
    url = models.CharField(max_length=200, blank=True)
    is_viewed = models.BooleanField()
    is_emailed = models.BooleanField()
    created = models.DateTimeField()
    occurrences = models.PositiveIntegerField()
    class Meta:
        managed = False
        db_table = 'nyt_notification'

class NytNotificationtype(models.Model):
    key = models.CharField(unique=True, max_length=128)
    label = models.CharField(max_length=128, blank=True)
    content_type = models.ForeignKey(DjangoContentType, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'nyt_notificationtype'

class NytSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    interval = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'nyt_settings'

class NytSubscription(models.Model):
    id = models.IntegerField(primary_key=True)
    settings = models.ForeignKey(NytSettings)
    notification_type = models.ForeignKey(NytNotificationtype)
    object_id = models.CharField(max_length=64, blank=True)
    send_emails = models.BooleanField()
    latest_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'nyt_subscription'

class ThumbnailKvstore(models.Model):
    key = models.CharField(unique=True, max_length=200)
    value = models.TextField()
    class Meta:
        managed = False
        db_table = 'thumbnail_kvstore'

class WikiArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    current_revision_id = models.IntegerField(unique=True, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    owner = models.ForeignKey(AuthUser, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, blank=True, null=True)
    group_read = models.BooleanField()
    group_write = models.BooleanField()
    other_read = models.BooleanField()
    other_write = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'wiki_article'

class WikiArticleforobject(models.Model):
    id = models.IntegerField(primary_key=True)
    article = models.ForeignKey(WikiArticle)
    content_type = models.ForeignKey(DjangoContentType)
    object_id = models.PositiveIntegerField()
    is_mptt = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'wiki_articleforobject'

class WikiArticleplugin(models.Model):
    id = models.IntegerField(primary_key=True)
    article = models.ForeignKey(WikiArticle)
    deleted = models.BooleanField()
    created = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'wiki_articleplugin'

class WikiArticlerevision(models.Model):
    id = models.IntegerField(primary_key=True)
    revision_number = models.IntegerField()
    user_message = models.TextField()
    automatic_log = models.TextField()
    ip_address = models.CharField(max_length=15, blank=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    modified = models.DateTimeField()
    created = models.DateTimeField()
    previous_revision = models.ForeignKey('self', blank=True, null=True)
    deleted = models.BooleanField()
    locked = models.BooleanField()
    article = models.ForeignKey(WikiArticle)
    content = models.TextField()
    title = models.CharField(max_length=512)
    class Meta:
        managed = False
        db_table = 'wiki_articlerevision'

class WikiAttachmentsAttachment(models.Model):
    reusableplugin_ptr = models.ForeignKey('WikiReusableplugin', primary_key=True)
    current_revision_id = models.IntegerField(unique=True, blank=True, null=True)
    original_filename = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'wiki_attachments_attachment'

class WikiAttachmentsAttachmentrevision(models.Model):
    id = models.IntegerField(primary_key=True)
    revision_number = models.IntegerField()
    user_message = models.TextField()
    automatic_log = models.TextField()
    ip_address = models.CharField(max_length=15, blank=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    modified = models.DateTimeField()
    created = models.DateTimeField()
    previous_revision = models.ForeignKey('self', blank=True, null=True)
    deleted = models.BooleanField()
    locked = models.BooleanField()
    attachment = models.ForeignKey(WikiAttachmentsAttachment)
    file = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        managed = False
        db_table = 'wiki_attachments_attachmentrevision'

class WikiImagesImage(models.Model):
    revisionplugin_ptr = models.ForeignKey('WikiRevisionplugin', primary_key=True)
    class Meta:
        managed = False
        db_table = 'wiki_images_image'

class WikiImagesImagerevision(models.Model):
    revisionpluginrevision_ptr = models.ForeignKey('WikiRevisionpluginrevision', primary_key=True)
    image = models.CharField(max_length=2000, blank=True)
    width = models.SmallIntegerField(blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'wiki_images_imagerevision'

class WikiNotificationsArticlesubscription(models.Model):
    articleplugin_ptr = models.ForeignKey(WikiArticleplugin, primary_key=True)
    subscription = models.ForeignKey(NytSubscription, unique=True)
    class Meta:
        managed = False
        db_table = 'wiki_notifications_articlesubscription'

class WikiReusableplugin(models.Model):
    articleplugin_ptr = models.ForeignKey(WikiArticleplugin, primary_key=True)
    class Meta:
        managed = False
        db_table = 'wiki_reusableplugin'

class WikiReusablepluginArticles(models.Model):
    id = models.IntegerField(primary_key=True)
    reusableplugin_id = models.IntegerField()
    article = models.ForeignKey(WikiArticle)
    class Meta:
        managed = False
        db_table = 'wiki_reusableplugin_articles'

class WikiRevisionplugin(models.Model):
    articleplugin_ptr = models.ForeignKey(WikiArticleplugin, primary_key=True)
    current_revision_id = models.IntegerField(unique=True, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'wiki_revisionplugin'

class WikiRevisionpluginrevision(models.Model):
    id = models.IntegerField(primary_key=True)
    revision_number = models.IntegerField()
    user_message = models.TextField()
    automatic_log = models.TextField()
    ip_address = models.CharField(max_length=15, blank=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    modified = models.DateTimeField()
    created = models.DateTimeField()
    previous_revision = models.ForeignKey('self', blank=True, null=True)
    deleted = models.BooleanField()
    locked = models.BooleanField()
    plugin = models.ForeignKey(WikiRevisionplugin)
    class Meta:
        managed = False
        db_table = 'wiki_revisionpluginrevision'

class WikiSimpleplugin(models.Model):
    articleplugin_ptr = models.ForeignKey(WikiArticleplugin, primary_key=True)
    article_revision = models.ForeignKey(WikiArticlerevision)
    class Meta:
        managed = False
        db_table = 'wiki_simpleplugin'

class WikiUrlpath(models.Model):
    id = models.IntegerField(primary_key=True)
    article = models.ForeignKey(WikiArticle)
    slug = models.CharField(max_length=50, blank=True)
    site = models.ForeignKey(DjangoSite)
    parent = models.ForeignKey('self', blank=True, null=True)
    lft = models.PositiveIntegerField()
    rght = models.PositiveIntegerField()
    tree_id = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    class Meta:
        managed = False
        db_table = 'wiki_urlpath'

