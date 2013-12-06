from httplib import HTTPResponse
from django.core.context_processors import request
from django.views.generic.base import TemplateView
from django.utils.log import getLogger

logger = getLogger(__name__)

class HomeView(TemplateView):
    
    def get_context_data(self, **kwargs):
        
        logger.debug('Entro in get_context_data di '+__name__)
        ctx = super(HomeView, self).get_context_data(**kwargs)
        return ctx