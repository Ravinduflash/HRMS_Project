from django.contrib import admin
<<<<<<< Updated upstream
from .models import PendingRequest, Leave, RejectedLeave, CanceledLeave

admin.site.register(PendingRequest)
admin.site.register(Leave)
admin.site.register(RejectedLeave)
admin.site.register(CanceledLeave)
from django.contrib import admin
from .models import PendingRequest, Leave, RejectedLeave, CanceledLeave

admin.site.register(PendingRequest)
=======
from .models import PendingLeaveRequest, Leave, RejectedLeave, CanceledLeave

admin.site.register(PendingLeaveRequest)
>>>>>>> Stashed changes
admin.site.register(Leave)
admin.site.register(RejectedLeave)
admin.site.register(CanceledLeave)
