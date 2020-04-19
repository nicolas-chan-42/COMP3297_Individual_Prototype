from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from trans19.models import Patient, Location, Visit


# Create your views here.
class Login(TemplateView):
    template_name = "trans19_login.html"


class Homepage(ListView):
    template_name = "trans19_homepage.html"
    model = Patient


class PatientDetails(TemplateView):
    template_name = "trans19_patient_details.html"

    def get_context_data(self, **kwargs):
        patient_pk = self.kwargs["patient_pk"]

        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=patient_pk)
        context["visit_list"] = (
            Visit.objects
            .filter(patient__pk=patient_pk)
            .order_by("-date_to")
        )

        return context
