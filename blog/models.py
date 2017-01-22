from django.db import models
from django.core.urlresolvers import reverse
from tagging.fields import *
from ckeditor.fields import RichTextField


class Post(models.Model):

    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    content = RichTextField('CONTENT')
    create_date =models.DateTimeField('Create Date', auto_now_add = True)
    modify_date = models.DateTimeField('Modify Date', auto_now = True)
    tag =TagField()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()


"""
class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    password = models.CharField(max_length=50)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)


    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        db_table = 'my_comment'

    def __str__(self):
        return self.text

    def get_absolute_url(self):
       return reverse('blog:add_comment_to_post', args=(self.slug,))
"""

