from django.db import models
from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField
import math

import numpy as np


# Create your models here.


cleancen2inches = lambda decimalCM, isHeight: f"{math.floor(decimalCM)}'{round(((decimalCM % 1) * 12)*2)/2}\"" if isHeight else f"{round(decimalCM*2)/2}\""

cen2inches = lambda cm , isHeight : cleancen2inches(cm/30.48) if isHeight else cleancen2inches(cm/2.54, isHeight)

women_list1 = np.arange(2.5, 14.5, 0.5).tolist()
# => [2.5,3.0,3.54.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0]

men_list1 = np.arange(6, 12.5, 0.5).tolist()
# => [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5,
# 11.0, 11.5, 12.0]


womenEUDict:{2.5:"33",3:"33.5",3:"34", 3.5: "34.5", 4: "35", 4.5: "35", 5: "35-36", 5.5: "36", 6: "36-37", 6.5: "37", 7: "37-38", 7.5: "38",
                    8: "38-39", 8.5: "39", 9: "39-40", 9.5: "40", 10: "40-41", 10.5: "41", 11: "41-42", 11.5: "42", 12: "42-43",
             12.5: "43.5", 13: "44", 13.5: "44.5", 14: "45"}

menEUDict: {6: "39", 6.5: "39", 7: "40", 7.5: "40-41", 8: "41", 8.5: "41-42", 9: "42", 9.5: "42-43",
                  10: "43", 10.5: "43-44", 11: "44", 11.5: "44-45", 12: "45", 13: "46", 14: "47", 15: "48", 16: "49"}

# create new list with 6.0 shoe sizes converted to 6
dropZeroInSize = lambda size: int(size) if size % 1 == 0 else size
final_men_chart = dict.fromkeys([ dropZeroInSize(size) for size in men_list1]).update(menEUDict)
final_women_chart = dict.fromkeys([ dropZeroInSize(size) for size in women_list1]).update(womenEUDict)
class TalentServicesOffered(models.Model):
    ARTIST_SERVICE_CHOICES = [
        ("NAIL", "NAIL ARTISTS"),
        ("PHOTO", "PHOTOGRAPHERS"),
        ("PROPS", "PROPS & SET DESIGN"),
        ("STYLING", "WARDROBE & STYLING"),
        ("HAIR", "HAIR & MAKEUP"),
    ]


class ModelingBoards(models.Model):
    GENDER_CHOICES = [
        ("W","Women"),
        ("M", "Men")
    ]
    WOMEN_BOARD_CHOICES = [
        ("WGW", "WOMEN"),
        ("WDE", "DEVELOPMENT"),
        ("WDI", "DIRECT"),
        ("WCU", "CURVE"),
        ("WSR", "SHOWROOM")
    ]
    MEN_BOARD_CHOICES = [
        ("MGM", "MEN"),
        ("MDE", "DEVELOPMENT"),
        ("MDI", "DIRECT"),
        ("MBT", "BIG & TALL"),
        ("MSR", "SHOWROOM")
    ]
    women_type_of_board = models.CharField(max_length=4, choices=WOMEN_BOARD_CHOICES, default='WGW')
    men_type_of_board = models.CharField(max_length=4, choices=WOMEN_BOARD_CHOICES, default='MGM')




class AgencyOffice(models.Model):
    ACCRA = 'ACC'
    LAGOS = 'LOS'
    NAIROBI = 'NBO'
    JOHANNESBURG = 'JNB'
    KIGALI = 'KGL'
    CASABLANCA = 'CMN'
    NEWYORK = 'JFK'
    LOSANGELES = 'LAX'
    MIAMI = 'MIA'
    LONDON = 'LHR'
    PARIS = 'CDG'
    MILAN = 'MXP'
    SYDNEY = 'SYD'
    HOME_AGENCY_OFFICE_CHOICES = [
        (ACCRA, 'Accra'),
        (LAGOS, 'Lagos'),
        (NAIROBI, "Nairobi"),
        (JOHANNESBURG, "Johannesburg"),
        (KIGALI, "Kigali"),
        (CASABLANCA, "Casablanca"),
        (NEWYORK, "New York"),
        (LOSANGELES, "Los Angeles"),
        (MIAMI, "Miami"),
        (LONDON, "London"),
        (PARIS, "Paris"),
        (MILAN, "Milan"),
        (SYDNEY, "Sydney"),
    ]
    AGENCY_CITY = models.CharField(max_length=20, choices=HOME_AGENCY_OFFICE_CHOICES, default=ACCRA)
    services_offered_at_office = ArrayField(ArrayField(models.CharField(max_length=60)))
    roster_tables = ArrayField(models.IntegerField())

class ScoutingInbound (models.Model):
    ACCRA = 'ACC'
    LAGOS = 'LOS'
    NAIROBI = 'NBO'
    JOHANNESBURG = 'JNB'
    KIGALI = 'KGL'
    CASABLANCA = 'CMN'
    NEWYORK = 'JFK'
    LOSANGELES = 'LAX'
    MIAMI = 'MIA'
    LONDON = 'LHR'
    PARIS = 'CDG'
    MILAN = 'MXP'
    SYDNEY = 'SYD'
    HOME_AGENCY_OFFICE_CHOICES = [
        (ACCRA, 'Accra'),
        (LAGOS, 'Lagos'),
        (NAIROBI, "Nairobi"),
        (JOHANNESBURG, "Johannesburg"),
        (KIGALI, "Kigali"),
        (CASABLANCA, "Casablanca"),
        (NEWYORK, "New York"),
        (LOSANGELES, "Los Angeles"),
        (MIAMI, "Miami"),
        (LONDON, "London"),
        (PARIS, "Paris"),
        (MILAN, "Milan"),
        (SYDNEY, "Sydney"),
    ]
    height_list = [(f"{x}cm", f"{cen2inches(x, isHeight=True)}") for x in range(152,218)]
    bust_list = [(f"{x}cm", f"{cen2inches(x, isHeight=False)}") for x in range(60,154)]
    waist_list = [(f"{x}cm", f"{cen2inches(x, isHeight=False)}") for x in range(51,101)]
    hips_list = [(f"{x}cm", f"{cen2inches(x, isHeight=False)}") for x in range(40,150)]
    women_shoe_size_list =


    # Need to look up the djano documentation for file upload and what needs to be adjsuted in the settings.py file
    # for a remote server like amazon s3 or cloudinary
    close_up_image = models.ImageField()
    profile_up_image = models.ImageField()
    waist_up_image = models.ImageField()
    full_length_image = models.ImageField()

    closest_home_agency = models.CharField(max_length=20, choices=HOME_AGENCY_OFFICE_CHOICES, default=ACCRA)
    services_offered_at_office = ArrayField(ArrayField(models.CharField(max_length=60)))
    modeling_board_gender = ModelingBoards






class ModelTalent(models.Model):
    first_name =  models.CharField(max_length=45, blank=False)
    last_name =  models.CharField(max_length=45, blank=False)
    roster_headshot_url = models.URLField(max_length=500)
    ig_username =  models.CharField(max_length=45)
    ig_followers_count = models.IntegerField()
    pinterest_username =  models.CharField(max_length=45)
    cdn_portfolio_images = ArrayField(models.URLField(max_length=400))
    cdn_portfolio_videos = ArrayField(models.URLField(max_length=300))
    skills = ArrayField(models.CharField(max_length=70))


    projects = ArrayField(ArrayField(models.TextField()))
    type_of_model = ArrayField(ModelingBoards)

    model_phone_number = PhoneNumberField(blank=False)
    model_email = models.EmailField(blank=False)
    password = models.
    height = models.IntegerField()
    bust = models.IntegerField()
    waist = models.IntegerField()
    hips = models.IntegerField()
    shoe_size = models.IntegerField()
    date_of_birth = models.DateField(blank=False)
    tik_tok_handle = models.CharField(max_length=70)
    twitter_handle = models.CharField(max_length=70)
    youtube_channel_handle = models.URLField(max_length=400)
    facebook_


    EYE_COLOR_CHOICES = [
        ('BR', 'BROWN'),
        ('BL', 'BLUE'),
        ('GR', 'GREEN'),
        ('GA', 'GRAY'),
        ('AM', 'AMBER'),
        ('HA', 'HAZEL'),
    ]
    eye_color = models.CharField(max_length=2, choices=EYE_COLOR_CHOICES, default='BR')
    hair_color = models.IntegerField()


