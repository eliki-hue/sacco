from django.contrib import admin
from .models import MemberProfile, Contribution, Loan, Repayment

@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'national_id', 'phone', 'joined_at')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'national_id', 'phone')

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.middle_name} {obj.user.last_name}"
    get_full_name.short_description = 'Full Name'

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount', 'date')
    list_filter = ('date',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('member__user__username', 'member__national_id')

@admin.register(Repayment)
class RepaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'amount', 'paid_at')
    list_filter = ('paid_at',)
