from django.contrib import admin
from .models import Order, OrderLineItem, OrderFeedback


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderFeedbackAdminInline(admin.TabularInline):
    model = OrderFeedback
    readonly_fields = ('like', 'dislike',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, OrderFeedbackAdminInline)

    readonly_fields = ('order_number', 'created',
                       'delivery_fee', 'order_total',
                       'final_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'created', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_fee',
              'order_total', 'final_total', 'original_bag',
              'stripe_pid', 'user_profile')

    list_display = ('order_number', 'created', 'full_name',
                    'order_total', 'delivery_fee',
                    'final_total',)

    ordering = ('-created',)


admin.site.register(Order, OrderAdmin)
