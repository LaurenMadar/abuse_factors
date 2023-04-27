from django import forms

from django.forms import ModelForm
from adt_flask.models import SurveyResponse


AGE_CHOICES =(
    (1, "12 to 17 years old"),
    (2, "18 to 25 years old"),
    (3, "26 to 35 years old"),
    (4, "36 to 49 years old"),
    (5, "50 years and older"),
)

EMPL_CHOICES=(
    (0, "Not employed or unemployed"),
    (1, "Employed part time"),
    (2, "Employed full time"),
)
  
GENDER_CHOICES = (
	(0, "Male"),
	(1, "Female"),
)

CITY_CHOICES = (
	(0, "Rural"),
	(1, "Small City"),
	(2, "Large Metro Area"),
	(3, "Other"),
)

MARRIAGE_CHOICES = (
	(0, "Not married"),
	(1, "Widowed"),
	(2, "Divorced"),
	(3, "Married"),
	(4, "Other"),
)

EDU_CHOICES = (
	(1, "Highschool or less"),
	(2, "Highschool graduate"),
	(3, "Some college"),
	(4, "College graduate"),
	(5, "Advanced degree"),
)

BOOL_CHOICES = (
	(0, "No"),
	(1, "Yes"),
)

LIKERT5_CHOICES = (
	(0, "0"),
	(1, "1"),
	(2, "2"),
	(3, "3"),
	(4, "4"),
	(5, "5"),
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
	(10, "10"),
)


class SurveyForm(ModelForm):
	year = forms.IntegerField(widget=forms.HiddenInput(), initial=2023)
	gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
	age = forms.ChoiceField(choices=AGE_CHOICES, required=True)
	married = forms.ChoiceField(choices=MARRIAGE_CHOICES, required=True)
	education = forms.ChoiceField(choices=EDU_CHOICES, required=True)
	employment = forms.ChoiceField(choices=EMPL_CHOICES, required=True)
	metrosize = forms.ChoiceField(choices=CITY_CHOICES, required=True)

	TRQLZRS = forms.ChoiceField(choices=LIKERT5_CHOICES, required=False, initial=0)
	SEDATVS = forms.ChoiceField(choices=LIKERT5_CHOICES, required=False, initial=0)
	HEROINUSE = forms.ChoiceField(choices=LIKERT5_CHOICES, required=False, initial=0)
	COCAINE = forms.ChoiceField(choices=LIKERT5_CHOICES, required=False, initial=0)
	AMPHETMN = forms.ChoiceField(choices=LIKERT5_CHOICES, required=False, initial=0)
	HALUCNG = forms.ChoiceField(choices=LIKERT5_CHOICES, required=False, initial=0)

	HEALTH = forms.ChoiceField(choices=LIKERT10_CHOICES, required=False, initial=0)
	MENTHLTH = forms.ChoiceField(choices=LIKERT5_CHOICES, required=False, initial=0)
	HEROINEVR = forms.ChoiceField(choices=BOOL_CHOICES, required=False, initial=0)
	TRTMENT = forms.ChoiceField(choices=LIKERT10_CHOICES, required=False, initial=0)
	MHTRTMT = forms.ChoiceField(choices=LIKERT10_CHOICES, required=False, initial=0)

	class Meta:
		model = SurveyResponse
		exclude=["id"]



