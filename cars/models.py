from django.db import models
from datetime import datetime


class Car(models.Model):
    
    STATE_CHOICES = (
        ("AL","Alabama"),
        ("AK","Alaska"),
        ("AS","American Samoa"),
        ("AZ","Arizona"),
        ("AR","Arkansas"),
        ("CA","California"),
        ("CO","Colorado"),
        ("CT","Connecticut"),
        ("DE","Delaware"),
        ("DC","District Of Columbia"),
        ("FM","Federated States Of Micronesia"),
        ("FL","Florida"),
        ("GA","Georgia"),
        ("GU","Guam"),
        ("HI","Hawaii"),
        ("ID","Idaho"),
        ("IL","Illinois"),
        ("IN","Indiana"),
        ("IA","Iowa"),
        ("KS","Kansas"),
        ("KY","Kentucky"),
        ("LA","Louisiana"),
        ("ME","Maine"),
        ("MH","Marshall Islands"),
        ("MD","Maryland"),
        ("MA","Massachusetts"),
        ("MI","Michigan"),
        ("MN","Minnesota"),
        ("MS","Mississippi"),
        ("MO","Missouri"),
        ("MT","Montana"),
        ("NE","Nebraska"),
        ("NV","Nevada"),
        ("NH","New Hampshire"),
        ("NJ","New Jersey"),
        ("NM","New Mexico"),
        ("NY","New York"),
        ("NC","North Carolina"),
        ("ND","North Dakota"),
        ("MP","Northern Mariana Islands"),
        ("OH","Ohio"),
        ("OK","Oklahoma"),
        ("OR","Oregon"),
        ("PW","Palau"),
        ("PA","Pennsylvania"),
        ("PR","Puerto Rico"),
        ("RI","Rhode Island"),
        ("SC","South Carolina"),
        ("SD","South Dakota"),
        ("TN","Tennessee"),
        ("TX","Texas"),
        ("UT","Utah"),
        ("VT","Vermont"),
        ("VI","Virgin Islands"),
        ("VA","Virginia"),
        ("WA","Washington"),
        ("WV","West Virginia"),
        ("WI","Wisconsin"),
        ("WY", "Wyoming"),
    )
    
    YEAR_CHOICES = []
    for r in range(2000, (datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))
        
        
    FEATURES_CHOICES = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    
    DOOR_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    
    
    car_title = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    car_photo = models.ImageField(upload_to='photos/car_photos')
    car_photo1 = models.ImageField(upload_to='photos/car_photos', blank=True)
    car_photo2 = models.ImageField(upload_to='photos/car_photos', blank=True)
    car_photo3 = models.ImageField(upload_to='photos/car_photos', blank=True)
    car_photo4 = models.ImageField(upload_to='photos/car_photos', blank=True)
    features = models.CharField(choices=FEATURES_CHOICES, max_length=100)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    running = models.IntegerField()
    doors = models.CharField(choices=DOOR_CHOICES, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)