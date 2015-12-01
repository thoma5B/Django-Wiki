# this file is Pseudocode, to illustrate the models

class Article(models.Model):
    objects = managers.ArticleManager()
    current_revision = models.OneToOneField('ArticleRevision', related_name='current_set')
    created = models.DateTimeField()
    modified = models.DateTimeField()
    owner = models.ForeignKey(compat.USER_MODEL, related_name='owned_articles', on_delete=models.SET_NULL)
    group = models.ForeignKey(settings.GROUP_MODEL,on_delete=models.SET_NULL)
    group_read = models.BooleanField(default=True)
    group_write = models.BooleanField(default=True)
    other_read = models.BooleanField(default=True)
    other_write = models.BooleanField(default=True)


class URLPath(MPTTModel):
    INHERIT_PERMISSIONS = True
    objects = managers.URLPathManager()
    articles = GenericRelation( ArticleForObject,content_type_field='content_type',object_id_field='object_id',)
    article = models.ForeignKey( Article, # Do NOT modify this field
        on_delete=models.CASCADE, editable=False, verbose_name=_('Cache lookup value for articles'))
    slug = models.SlugField()
    site = models.ForeignKey(Site)
    parent = TreeForeignKey('self', related_name='children')
    slug2 = models.OneToOneField('Slug')

# TODO: create a class 'Slug' and redefine 'slug' as property in 'URLPath'
# TODO: set FK slug = models.OneToOneField('Slug') in class 'Article'
# TODO: delete slug = models.SlugField() in class 'URLPath'
    slug = models.OneToOneField('Slug')

    @property
    def slug(self):
        return Slug.objects.get().values_list('article__slug')


class Slug(models.Model):
    slug = models.SlugField()


###################################################


class ArticleRevision(BaseRevisionMixin, models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    content = models.TextField(blank=True, verbose_name=_('article contents'))
    title = models.CharField()

get(article__slug)

################################################################################
################################################################################
################################################################################

import pymongo
client = pymongo.MongoClient()
# client.database_names() # [u'academy_etherpad', u'local']
etherpad = client['academy_etherpad']


for i, store in enumerate(etherpad.store.find()):
    if i > 20:
        break
    else:
        print store


{
  u'_id': ObjectId('5628e7da26c1cde1fa66d2ac'),
  u'val': u'"r.f255a4aab948deba624ec331f2926b39"',
  u'key': u'pad2readonly:Nummer1'
}
{
  u'_id': ObjectId('5628e7da26c1cde1fa66d2ad'),
  u'val': u'"Nummer1"',
  u'key': u'readonly2pad:r.f255a4aab948deba624ec331f2926b39'
}
{
  u'_id': ObjectId('5628e7da26c1cde1fa66d2ae'),
  u'val': u'{
    "changeset": "Z:1>6b|5+6b$Welcome to Etherpad!\\n\\nThis pad text is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents!\\n\\nGet involved with Etherpad at http://etherpad.org\\n",
    "meta": {
      "author": "",
      "timestamp": 1445521370422,
      "atext": {
        "text": "Welcome to Etherpad!\\n\\nThis pad text is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents!\\n\\nGet involved with Etherpad at http://etherpad.org\\n\\n",
        "attribs": "|6+6c"
      }
    }
  }',
  u'key': u'pad:Nummer1:revs:0'
}

etherpad.store.find_one({u'key': u'pad:Nummer1:revs:0'})
