from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Website(models.Model):
    """
    This models holds the details of the
    website and other additional website
     informations are related to it. It
     is expected to have only one entry
     per website"""

    name = models.CharField(max_length = 200)
    url = models.URLField()

    def __str__(self):
        return self.name 


class WebMaster(models.Model):
    """
    Model for Webmaster(s) incharge of a
    website"""

    website = models.ForeignKey(
        Website,
        related_name='webmasters',
        on_delete=models.CASCADE)

    user = models.ForeignKey(
        User, 
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username


class PhoneNumber(models.Model):
    """
    Model for storing phone numbers"""

    number =  models.CharField(max_length=20)

    def __str__(self):
        return self.number


class EmailAddress(models.Model):
    """
    Model for storing Email addresses"""

    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Email Addresses"

    

class SocialAccount(models.Model):
    """
    This model stores links to
    social websites"""

    websites = (
        ('facebook','Facebook'),
        ('twitter','Twitter'),
        ('instagram','Instagram'),
        ('github','GitHub'),
        ('telegram','Telegram'),
        ('discord','Discord'),
        ('twitch','Twitch'),
        ('whatsapp','WhatsApp'),
        ('snapchat','Snapchat'),
        ('skype','Skpye'),
        ('tik_tok','Tik Tok'),
        ('hangout','Hangout')
    )

    account = models.CharField(
        max_length = 20, 
        choices = websites)

    link = models.URLField()

    def __str__(self):
        return self.account


class TextContent(models.Model):
    """
    This model stores text content
    as the name implies. It is used
    by other models to help organize
    all text contents to one uniform
    location"""

    content_for = models.CharField(max_length = 25)
    content = models.TextField()

    def __str__(self):
        return self.content_for


class AdditionalInfo(models.Model):
    """
    This models help to add additional
    site informations to the site. They
    are customizable to meet with the
    site's requirement"""
    
    website = models.OneToOneField(
        Website, 
        related_name = 'additional_info',
        on_delete=models.CASCADE)

    about = models.OneToOneField(
        TextContent, 
        related_name = 'about',
        on_delete=models.CASCADE, 
        blank = True)

    mission = models.OneToOneField(
        TextContent, 
        related_name = 'mission',
        on_delete=models.CASCADE, 
        blank = True)

    vision = models.OneToOneField(
        TextContent, 
        related_name = 'vision',
        on_delete=models.CASCADE, 
        blank = True)

    address = models.OneToOneField(
        TextContent, 
        related_name = 'address',
        on_delete=models.CASCADE, 
        blank = True)


    tab_icon = models.ImageField(
        upload_to = 'website/images', 
        blank = True)

    apple_icon = models.ImageField(
        upload_to = 'website/images', 
        blank = True)

    logo = models.ImageField(
        upload_to = 'website/images',
        blank=True)


    def __str__(self):
        return self.website.name

    class Meta:
        verbose_name_plural = "Website's additional infomations"


class WebsitePhoneNumber(PhoneNumber):
    """
    This models inherits from the
    PhoneNumber model and servesmodel = Website
    as the model for storing
    phone numbers related to the
    website"""
    website = models.ForeignKey(
        AdditionalInfo, 
        related_name="contact_numbers",
        on_delete = models.CASCADE)


class WebsiteEmailAddress(EmailAddress):
    """
    This models inherits from the
    EmailAddress model and serves
    as the model for storing
    email addresses related to the
    website"""

    website = models.ForeignKey(
        AdditionalInfo,
        related_name="email_addresses",
        on_delete=models.CASCADE)


class WebsiteSocialAccount(SocialAccount):
    """ This models extends the SocialAccount
    model for use by the Website model"""
    website = models.ForeignKey(
        AdditionalInfo, 
        on_delete=models.CASCADE)


class FAQ(models.Model):
    """
    Some websites might also need
    to display frequently asked
    questions. this model help to
    do just that"""

    website = models.ForeignKey(
        AdditionalInfo,
        related_name="faqs",
        on_delete=models.CASCADE)

    question = models.CharField(
        max_length = 200)
    answer = models.TextField()

    def __str__(self):
        return self.question


class TeamMember(models.Model):
    """
    Some websites, mostly business websites,
    usually love to display team members
    if their organization. This model
    helps to store team member details"""

    website = models.ForeignKey(
        AdditionalInfo,
        related_name="team_members",
        on_delete=models.CASCADE)

    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    email = models.ForeignKey(
        EmailAddress, 
        on_delete= models.CASCADE)
    phone_number = models.ForeignKey(
        PhoneNumber, 
        on_delete= models.CASCADE)
    photo = models.ImageField(upload_to='team/images')

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return self.get_fullname()


class TeamMemberSocialAccount(SocialAccount):
    """
    This models extends the SocialAccount model
    for use by the TeamMember Model"""

    TeamMember = models.ForeignKey(
        TeamMember, 
        on_delete= models.CASCADE)


class Message(models.Model):
    """
    This model saves messages sent by
    users users from the contact us view
    for further processing or to be accessed
    by the WebSite's WebMaster/Admin"""

    website = models.ForeignKey(
        AdditionalInfo, 
        related_name='messages', 
        on_delete= models.CASCADE)  # Not really
        # necessary but will allow me access this
        # model from the Website Models in template
        # rendering.

    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=100 )
    message = models.TextField()
    timestamp = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.fullname


class Testimonial(models.Model):
    """
    Some websites also require getting
    feedbacks form their customers via
    testimonials. This model saves such
    data"""
    
    website = models.ForeignKey(
        AdditionalInfo, 
        related_name='testimonials', 
        on_delete= models.CASCADE)  # Not really
        # necessary but will allow me access this
        # model from the Website Models in template
        # rendering.
    can_display = models.BooleanField() # Some replies need to be reviewed before displaying on site.
    fullname = models.CharField(max_length = 200)
    email = models.EmailField(blank = True)
    phone_number = models.CharField(max_length=20, blank=True)
    occupation = models.CharField(max_length=200, blank=True)
    feedback = models.TextField()
    timestamp = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.fullname

class Member(models.Model):
    gender_options = (
        ('m','Male'),
        ('f','Female')
    )

    service_options = (
        ('member',"Member"),
        ('choir',"Choir"),
        ('media',"Media"),
    )

    surname = models.CharField(max_length=14)
    firstname = models.CharField(max_length=14)
    address= models.TextField()
    phone_no = models.CharField(max_length=14)
    gender  = models.CharField(max_length=1, choices=gender_options)
    email = models.EmailField()
    service = models.CharField(max_length=14, choices=service_options)
    photo = models.ImageField(upload_to = 'members/images')

    def __str__(self):
        return f"{self.surname} {self.firstname}"

    def male(self):
        """Filters all male members"""
        pass

    def female(self):
        """Filters all female members"""
        pass


class PrayerRequest(models.Model):
    name = models.CharField(max_length=20, null=True, default='Anonymous', blank=True)
    prayer_request = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
