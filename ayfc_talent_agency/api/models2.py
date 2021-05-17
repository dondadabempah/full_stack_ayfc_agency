from django.db import models
from phonenumber_field.modelfields import PhoneNumberField






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
    AGENCY_CITY = models.CharField(max_length=20, choices= HOME_AGENCY_OFFICE_CHOICES, default= ACCRA)
    ag

class AgencyDivision(models.Model):
    division_name = models.CharField(max_length=30, default="WOMEN")
    agency_office = models.ForeignKey(AgencyOffice, on_delete=models.CASCADE)
    division_rosters =

class AgencyDivisionModelingBoard(models.Model):
    GENDER_CHOICES = [
        ("W", "Women"),
        ("M", "Men")
    ]
    BOARD_CHOICES = [
        ("WGW", "WOMEN"),
        ("WDE", "DEVELOPMENT"),
        ("WDI", "DIRECT"),
        ("WCU", "CURVE"),
        ("WSR", "SHOWROOM"),
        ("MGM", "MEN"),
        ("MDE", "DEVELOPMENT"),
        ("MDI", "DIRECT"),
        ("MBT", "BIG & TALL"),
        ("MSR", "SHOWROOM")
    ]
    agency_division = models.ForeignKey(AgencyDivision, on_delete=models.CASCADE)
    type_of_board = models.CharField(max_length=4, choices=BOARD_CHOICES, default='WGW')
    board_model_roster = models.ForeignKey
    agency_office = models.ForeignKey(AgencyOffice)


class ModelTalent(models.Model):
    agency_office = models.ForeignKey(AgencyOffice, on_delete=models.cascade)
    modeling_boards = models.ManyToManyField(AgencyDivisionModelingBoard)

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