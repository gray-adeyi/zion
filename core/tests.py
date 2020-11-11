from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import (
    Website,
    WebMaster,
    PhoneNumber,
    EmailAddress,
    SocialAccount,
    TextContent,
)

# Create your tests here.

############################################ MODEL TESTS  ######################
NAME = 'Coyote Developers'
URL = 'https://www.coyote.com'
USERNAME = 'root'
PASSWORD = 'paSsWoRd123'
EMAIL = 'coyotedeveloper@coyote.com'
PHONE_NUMBER = '09059438568'
SOCIAL_ACCOUNT = 'facebook'
SOCIAL_ACCOUNT_LINK = 'https://www/facebook.com'
CONTENT_FOR = 'textcontent'
CONTENT = """
Lorem ipsum dolor sit amet consectetur adipisicing elit. 
Accusamus porro eos quisquam saepe qui quia inventore, 
fuga ea numquam odit similique quos rem odio minus animi 
sit nemo temporibus sunt.
"""

def create_website(name, url):
    return Website.objects.create(
        name=name,
        url=url)

class CommonTests(TestCase):

    model = None

    def _assert_instance(self,model):
        model_instance = get_object_or_404(model)
        self.assertIsInstance(model_instance, model)

    def _test_create_et_fetch_model_instance(self, model):
        self._assert_instance(model)

    @classmethod
    def _get_class_name(self,cls):
        return cls.__name__

    def test_create_et_fetch_model_instance(self):
        if self.model is not None:
            self._test_create_et_fetch_model_instance(self.model)


class WebsiteModelTests(CommonTests):
    """
    This class conducts all the 
    test methods defined on the
    Website model"""

    model = Website

    def setUp(self):
        new_website_1 = create_website(NAME, URL)



class WebMasterModelTests(CommonTests):
    """
    This runs all test cases on the
    'WebMaster' models"""

    model = WebMaster
    
    def setUp(self):
        website = create_website(NAME,URL)
        webmaster_user = User.objects.create_superuser(
            username = USERNAME,
            email= EMAIL,
            password= PASSWORD

        )
        webmaster = WebMaster.objects.create(
            website = website,
            user = webmaster_user,
        )


class PhoneNumberModelTests(CommonTests):
    """This TestCase class runs tests on
    the PhoneNumber model"""

    model = PhoneNumber

    def setUp(self):
        phone_number = PhoneNumber.objects.create(
            number = PHONE_NUMBER
        )


class EmailAddressModelTests(CommonTests):

    model = EmailAddress

    def setUp(self):
        email_address = EmailAddress.objects.create(
            email = EMAIL,
        )


class SocialAccountModelTests(CommonTests):
    model = SocialAccount

    def setUp(self):
        social_account = SocialAccount.objects.create(
            account = SOCIAL_ACCOUNT,
            link = SOCIAL_ACCOUNT_LINK
        )

    def test_get_class_name(self):
        print(super()._get_class_name(SocialAccountModelTests))
    

class TextContentModelTests(CommonTests):
    pass
#################################   END MODEL TESTS ################

################################    VIEW TESTS  ####################

#################################   END MODEL TESTS ################