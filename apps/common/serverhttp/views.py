from django.views.generic import TemplateView


class HttpRequestAttakView(TemplateView):
    template_name = 'setup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['n'] = [i for i in range(1000)]
        return context
