from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.




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
    closest_home_agency = models.CharField(max_length=20, choices=HOME_AGENCY_OFFICE_CHOICES, default=ACCRA)
    services_offered_at_office = ArrayField(ArrayField(models.CharField(max_length=60)))
    modeling_board_gender = ModelingBoards






class ModelTalent(models.Model):
    first_name =  models.CharField(max_length=45)
    last_name =  models.CharField(max_length=45)
    roster_headshot_url = models.URLField(max_length=500)
    ig_username =  models.CharField(max_length=45)
    ig_followers_count = models.IntegerField()
    pinterest_username =  models.CharField(max_length=45)
    cdn_portfolio_images = ArrayField(models.URLField(max_length=400))
    cdn_portfolio_videos = ArrayField(models.URLField(max_length=300))
    skills = ArrayField(models.CharField(max_length=70))


    projects = ArrayField(ArrayField(models.TextField()))
    type_of_model = ArrayField(ModelingBoards)


    height = models.IntegerField()
    bust = models.IntegerField()
    waist = models.IntegerField()
    hips = models.IntegerField()
    shoe_size = models.IntegerField()
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


