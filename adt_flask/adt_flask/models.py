from django.db import models
import datetime

class SurveyResponse(models.Model):
    GENDERS = (
        (0, 'male'),
        (1, 'female'),
        )

    ECATS = (
        (0, 'not employed'),
        (1, 'part-time'),
        (2, 'full-time'),
        )

    CITYSIZE = (
        (0, 'rural'),
        (1, 'small'),
        (2, 'large'),
        (3, 'other'),
        )

    EDLEVEL = (
        (1, 'highschool or less'),
        (2, 'highschool graduate'),
        (3, 'some college'),
        (4, 'college graduate'),
        (5, 'other'),
        )

    AGECAT = (
        (0, '11 years or younger'),
        (1, '12 to 17 years'),
        (2, '18 to 25 years'),
        (3, '26 to 35 years'),
        (4, '36 to 49 years'),
        (5, '50 and over'),
        )

    MSTATUS = (
        (0, 'Unmarried'),
        (1, 'Widowed'),
        (2, 'Divorced'),
        (3, 'Married'),
        (4, 'Other'),
        )

    BOOL_CHOICES = (
        (0, "No"),
        (1, "Yes")
    )

    LIKERT5_CHOICES = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )

    LIKERT10_CHOICES = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10")
    )


    id = models.AutoField(primary_key=True,db_column='idsurvey_resp')
    currentyear = datetime.date.today().year
    year = models.IntegerField(db_column='survey_yr', default=currentyear)
    gender = models.IntegerField(db_column='reported_gender',choices=GENDERS)
    employment = models.IntegerField(db_column='employment',choices=ECATS)
    married = models.IntegerField(db_column='marital_status',choices=MSTATUS)
    education = models.IntegerField(db_column='edu_lvl',choices=EDLEVEL)
    age = models.IntegerField(db_column='age_group',choices=AGECAT)
    metrosize = models.IntegerField(db_column='city_metro',choices=CITYSIZE)

    TRQLZRS = models.IntegerField(choices=LIKERT5_CHOICES, default=0)
    SEDATVS = models.IntegerField(choices=LIKERT5_CHOICES, default=0)
    HEROINUSE = models.IntegerField(choices=LIKERT5_CHOICES, default=0)
    COCAINE = models.IntegerField(choices=LIKERT5_CHOICES, default=0)
    AMPHETMN = models.IntegerField(choices=LIKERT5_CHOICES, default=0)
    HALUCNG = models.IntegerField(choices=LIKERT5_CHOICES, default=0)

    HEALTH = models.IntegerField(choices=LIKERT10_CHOICES, default=0)
    MENTHLTH = models.IntegerField(choices=LIKERT5_CHOICES, default=0)
    HEROINEVR = models.IntegerField(choices=BOOL_CHOICES, default=0)
    TRTMENT = models.IntegerField(choices=LIKERT10_CHOICES, default=0)
    MHTRTMT = models.IntegerField(choices=LIKERT10_CHOICES, default=0)

    def __str__(self):
        return self.id

    class Meta:
        managed = True
        db_table = 'survey_response'

