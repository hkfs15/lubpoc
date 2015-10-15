from django.db import models

# Create your models here.


class Make(models.Model):

    name = models.CharField("Make name", max_length=40)
    website = models.URLField("Make offical website", blank=True)
    # picture = models.ImageField(upload_to="make_picture", blank=True)
    description = models.TextField("Make description", blank=True)
    last_modified = models.DateField("Last modified", auto_now=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Make"
        verbose_name_plural = "Makes"

    def __str__(self):
        return self.name


class Series(models.Model):

    make = models.ForeignKey(Make)
    name = models.CharField("Series name", max_length=128)
    last_modified = models.DateField("Last modified", auto_now=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.name


class LubMake(models.Model):

    name = models.CharField("Lubricator maker", max_length=128)
    website = models.URLField("Lubricator maker offical website", blank=True)
    # picture = models.ImageField(upload_to="lubmake_picture", blank=True)
    description = models.TextField("Lub description", blank=True)
    last_modified = models.DateField("Last modified", auto_now=True)
    slug = models.SlugField("LubMaker slug", unique=True)

    class Meta:
        verbose_name = "LubMake"
        verbose_name_plural = "LubMakes"

    def __str__(self):
        return self.name


class Lub(models.Model):

    MOTOR_TYPE_LIST = (
        ('CHAIYOU', '柴油发动机'),
        ('QIYOU', '汽油发动机'),
        )

    LUB_TYPE_LIST = (
        ('ADVANCED', '高级润滑油'),
        ('NORMAL', '普通润滑油'),
        )

    SAE_GRADE_LIST = (
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4'),
        ('S5', 'S5'),
        ('S6', 'S6'),
        ('S7', 'S7'),
        )

    lubmake = models.ForeignKey(LubMake)
    name = models.CharField("Lub name", max_length=128)
    # picture = models.ImageField(upload_to="lub_picture", blank=True)
    datasheet = models.TextField("Lub datasheet", blank=True)
    # features = models.TextField()
    # applications = models.TextField()
    lub_type = models.CharField(max_length=50, choices=LUB_TYPE_LIST)
    motor_type = models.CharField(max_length=50, choices=MOTOR_TYPE_LIST)
    specifications = models.TextField(blank=True)
    builderapproval = models.CharField(max_length=128, blank=True)
    sae_grade = models.CharField(max_length=50, choices=SAE_GRADE_LIST)
    density = models.CharField(max_length=128, blank=True)
    viscosity_40 = models.CharField(max_length=128, blank=True)
    viscosity_100 = models.CharField(max_length=128, blank=True)
    viscosity_index = models.CharField(max_length=128, blank=True)
    sulfated_ash = models.CharField(max_length=128, blank=True)
    wt = models.CharField(max_length=128, blank=True)
    totalbase = models.CharField(max_length=128, blank=True)
    flashpoint = models.CharField(max_length=128, blank=True)
    pourpoint = models.CharField(max_length=128)
    last_modified = models.DateField("Last modified", auto_now=True)
    slug = models.SlugField("Lub slug", unique=True)

    class Meta:
        verbose_name = "Lub"
        verbose_name_plural = "Lubs"

    def __str__(self):
        return self.name


class Car(models.Model):

    series = models.ForeignKey(Series)
    manual_listed_lubs = models.ManyToManyField(Lub, blank=True)

    MOTOR_TYPE_LIST = (
        ('CHAIYOU', '柴油发动机'),
        ('QIYOU', '汽油发动机'),
        )

    LUB_TYPE_LIST = (
        ('ADVANCED', '高级润滑油'),
        ('NORMAL', '普通润滑油'),
        )

    SAE_GRADE_LIST = (
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4'),
        ('S5', 'S5'),
        ('S6', 'S6'),
        ('S7', 'S7'),
        )

    year = models.IntegerField(blank=True)
    model = models.CharField(max_length=128)
    spec = models.FilePathField(path="static/manual/", match="car_manual_*",
                                recursive=True, blank=True)

    # vescosity_grade = models.ChoiceField()
    lub_type = models.CharField(max_length=50, choices=LUB_TYPE_LIST,
                                blank=True)
    motor_type = models.CharField(max_length=50, choices=MOTOR_TYPE_LIST,
                                  blank=True)
    last_modified = models.DateField("Last modified", auto_now=True)
    slug = models.SlugField("Car slug", unique=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.model


class Engine(models.Model):

    series = models.OneToOneField(Series)
    brand = models.CharField(max_length=128)
    model = models.CharField(max_length=128)
    spec = models.TextField(blank=True)
    # vescosity_grade
    # granted_lub_type
    # optional_lub_types
    last_modified = models.DateField("Last modified", auto_now=True)
    slug = models.SlugField("Engine slug", unique=True)

    class Meta:
        verbose_name = "Engine"
        verbose_name_plural = "Engines"

    def __str__(self):
        return self.model

