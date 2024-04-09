from django.db import models

from PC_shop_backend.common.models import Product


class Computer(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'computer'

    NETWORK_CHOICES = [
        ('ethernet', 'Ethernet'),
        ('wifi', 'Wi-Fi'),
        ('bluetooth', 'Bluetooth'),
    ]

    COOLING_CHOICES = [
        ('air', 'Air Cooling'),
        ('liquid', 'Liquid Cooling'),
        ('passive', 'Passive Cooling'),
    ]

    processor = models.CharField(max_length=50)
    graphics = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)

    # Additional specifications
    cooler = models.CharField(max_length=200, blank=True, null=True)
    motherboard = models.CharField(max_length=200, blank=True, null=True)
    power_supply = models.CharField(max_length=200, blank=True, null=True)
    operating_system = models.CharField(max_length=200, blank=True, null=True)
    case = models.CharField(max_length=200, blank=True, null=True)
    cooling_solution = models.CharField(max_length=20, choices=COOLING_CHOICES, blank=True, null=True)
    network = models.CharField(max_length=20, choices=NETWORK_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.processor} - {self.memory} - {self.storage}"


class Monitor(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'monitor'

    resolution = models.CharField(max_length=20)
    refresh_rate = models.CharField(max_length=10)
    panel_type = models.CharField(max_length=20)
    size = models.CharField(max_length=5)

    # Additional specifications
    aspect_ratio = models.CharField(max_length=10, blank=True, null=True)
    response_time = models.CharField(max_length=10, blank=True, null=True)
    curvature = models.BooleanField(default=False)
    adjustable_stand = models.BooleanField(default=False)
    built_in_speakers = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.size} - {self.refresh_rate}"


class Keyboard(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'keyboard'

    key_switch_type = models.CharField(
        max_length=30,
        choices=[
            ('membrane', 'Membrane'),
            ('mechanical', 'Mechanical'),
            ('scissor', 'Scissor'),
        ]
    )
    backlight = models.BooleanField(default=False)
    color = models.CharField(max_length=20, blank=True, null=True)
    wireless = models.BooleanField(default=False)
    format = models.CharField(
        max_length=20,
        choices=[
            ('full_size', 'Full size'),
            ('tenkeyless', 'Tenkeyless (TKL)'),
            ('compact_75', 'Compact (75%)'),
            ('compact_65', 'Compact (65%)'),
            ('mini_60', 'Mini (60%)'),
            ('keypad', 'Keypad'),
        ]
    )

    # Additional specifications
    layout = models.CharField(max_length=20, choices=[('ansi', 'ANSI'), ('iso', 'ISO')], default='ansi')
    polling_rate_hz = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                          help_text="Polling rate in Hz")
    brand = models.CharField(max_length=100, blank=True, null=True, help_text="Brand of the keyboard")
    key_rollover = models.IntegerField(blank=True, null=True, help_text="Key rollover (N-key rollover)")

    def __str__(self):
        backlight_info = 'Backlight' if self.backlight else 'Not Backlit'
        color_info = f" - Color: {self.color}" if self.color else ""
        return f"{self.name} - {self.get_key_switch_type_display()} - {backlight_info}{color_info} - {'Wireless' if self.wireless else 'Wired'}"


class Mouse(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'mouse'

    dpi = models.IntegerField(help_text="Dots per inch (DPI)")
    tracking_type = models.CharField(
        max_length=30,
        choices=[
            ('optical', 'Optical'),
            ('laser', 'Laser'),
            ('trackball', 'Trackball'),
        ]
    )
    buttons = models.IntegerField(help_text="Number of buttons")
    ergonomic = models.BooleanField(default=False)
    wireless = models.BooleanField(default=False)
    color = models.CharField(max_length=20, blank=True, null=True)
    polling_rate_hz = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                          help_text="Polling rate in Hz")
    brand = models.CharField(max_length=100, blank=True, null=True, help_text="Brand of the mouse")

    def __str__(self):
        wireless_info = 'Wireless' if self.wireless else 'Wired'
        color_info = f" - Color: {self.color}" if self.color else ""
        return f"{self.name} - DPI: {self.dpi} - {self.tracking_type} - {wireless_info} - {self.buttons} buttons{color_info}"
