from django.views.generic.base import TemplateView
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponseBadRequest()
        return super(IndexView, self).dispatch(request, *args, **kwargs)
