from __future__ import unicode_literals

# from django.db import models
from django.template.loader import render_to_string
from django.utils import six

# from . import columns



class TableMetaclass(type):
    def __new__(cls, name, bases, attrs):
        super_new = super(TableMetaclass, cls).__new__
        parents = [b for b in bases if isinstance(b, TableMetaclass)]
        if not parents:
            return super_new(cls, name, bases, attrs)

        module = attrs.pop('__module__')
        new_attrs = {'__module__': module}
        classcell = attrs.pop('__classcell__', None)
        if classcell is not None:
            new_attrs['__classcell__'] = classcell

        new_class = super_new(cls, name, bases, new_attrs)
        new_class._meta = attrs.pop('Meta', None)

        return new_class


class TableBase(six.with_metaclass(TableMetaclass)):
    structure_template = 'djdatatableview/default.html'

    # column_mapping = {
    #     models.AutoField: '',  # IntegerField,
    #     models.BigIntegerField: '',  # IntegerField,
    #     models.BooleanField: '',  # BooleanField,
    #     models.CharField: '',  # CharField,
    #     models.CommaSeparatedIntegerField: '',  # CharField,
    #     models.DateField: '',  # DateField,
    #     models.DateTimeField: '',  # DateTimeField,
    #     models.DecimalField: '',  # DecimalField,
    #     models.EmailField: '',  # EmailField,
    #     models.Field: '',  # ModelField,
    #     models.FileField: '',  # FileField,
    #     models.FloatField: '',  # FloatField,
    #     models.ImageField: '',  # ImageField,
    #     models.IntegerField: '',  # IntegerField,
    #     models.NullBooleanField: '',  # NullBooleanField,
    #     models.PositiveIntegerField: '',  # IntegerField,
    #     models.PositiveSmallIntegerField: '',  # IntegerField,
    #     models.SlugField: '',  # SlugField,
    #     models.SmallIntegerField: '',  # IntegerField,
    #     models.TextField: '',  # CharField,
    #     models.TimeField: '',  # TimeField,
    #     models.URLField: '',  # URLField,
    #     models.GenericIPAddressField: '',  # IPAddressField,
    #     models.FilePathField: '',  # FilePathField,
    # }

    def __init__(self):
        self.id = getattr(self._meta, 'id', None)
        self.url = getattr(self._meta, 'url', None)
        self.method = getattr(self._meta, 'method', 'GET')
        self.fields = getattr(self._meta, 'fields', '__all__')

        self.columns = self.fields

    def __str__(self):
        """ Renders ``structure_template`` with ``self`` as a context variable. """

        context = {
            # 'url': self.url,
            # 'config': self.config,
            # 'datatable': self,
            # 'columns': self.columns.values(),
        }

        context = dict(
            url=self.url,
            id=self.id,
            method=self.method,
            columns=self.columns
        )

        return render_to_string(self.structure_template, context)


class Table(TableBase):
    class Meta:
        id = 'my_id'
        url = 'my_url'
        method = 'POST'
        fields = ['col_1', 'col_2']

