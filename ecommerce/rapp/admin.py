from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from myapp.models import User
from .models import Retailer
from .models import Dealer
from .models import Company
from .models import FieldStaff
# Register your models here.

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "retailer":
            kwargs["queryset"] = User.objects.filter(groups__name='retailer', added_by=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            retailer_user = User.objects.filter(groups__name='retailer', added_by=request.user)
            queryset = Retailer.objects.filter(retailer__in=retailer_user)
        return queryset
            
    list_display = ('id','first_name', 'last_name', 'email_id', 'retailer', 'phone_number','address', 'nationality', 'state', 'city', 'zipcode',  'fieldstaff', 'loyalty_points',)
    exclude=('fieldstaff', )
    search_fields = ('first_name', 'last_name','phone_number','address', 'nationality', 'state', 'city')
    list_filter = ('fieldstaff', 'state',)

    def save_model(self, request, obj, form, change):
        if not obj.fieldstaff:
            obj.fieldstaff = request.user
        obj.save()


    def orders_summary(self, obj):
        aggregated_orders = obj.get_aggregated_orders()
        summary = ""
        for order in aggregated_orders:
            summary += f"Order ID: {order['order__id']}, Date: {order['order__order_date']}, Total Amount: {order['total_amount']}, Total Quantity: {order['total_quantity']}\n"
        return summary

    orders_summary.short_description = "Orders Summary"


    def view_loyalty_points(self, obj):
        url = reverse('view_loyalty_points')
        return format_html('<a href="{}">View Loyalty Points</a>', url)
    view_loyalty_points.short_description = 'Loyalty Points'

