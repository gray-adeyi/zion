from django.contrib import admin
from .models import (
    Website,
    WebMaster,
    PhoneNumber,
    WebsitePhoneNumber,
    EmailAddress,
    WebsiteEmailAddress,
    SocialAccount,
    WebsiteSocialAccount,
    TextContent,
    TeamMember,
    TeamMemberSocialAccount,
    FAQ,
    AdditionalInfo,
    Message,
    Testimonial,
    PrayerRequest,
)


####################### INLINES ######################

class WebsitePhoneNumberInline(admin.StackedInline):
    model = WebsitePhoneNumber
    extra = 1

class WebsiteEmailAddressInline(admin.StackedInline):
    model = WebsiteEmailAddress
    extra = 1

class WebsiteSocialAccountInline(admin.StackedInline):
    model = WebsiteSocialAccount
    extra = 1

class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 1

class FAQInline(admin.StackedInline):
    model = FAQ
    extra = 1

class AdditionalInfoInline(admin.StackedInline):
    model = AdditionalInfo
    extra = 0

class TeamMemberSocialAccountInline(admin.StackedInline):
    model = TeamMemberSocialAccount
    extra = 1

###################### MODEL ADMINS ########################### 

class AdditionalInfoAdmin(admin.ModelAdmin):
    
    inlines = [
        WebsitePhoneNumberInline,
        WebsiteEmailAddressInline,
        WebsiteSocialAccountInline,
        TeamMemberInline,
        FAQInline,
    ]

class WebsiteInline(admin.ModelAdmin):

    inlines = [
        AdditionalInfoInline,
    ]
class TeamMemberAdmin(admin.ModelAdmin):

    inlines = [
        TeamMemberSocialAccountInline,
    ]

############### Register your models here. ############################

admin.site.register(
    AdditionalInfo, 
    AdditionalInfoAdmin)

admin.site.register(
    Website,
    WebsiteInline)

admin.site.register(FAQ)
admin.site.register(
    TeamMember,
    TeamMemberAdmin)

admin.site.register(TextContent)
admin.site.register(PhoneNumber)
admin.site.register(EmailAddress)
admin.site.register(SocialAccount)
admin.site.register(Message)
admin.site.register(Testimonial)
admin.site.register(PrayerRequest)