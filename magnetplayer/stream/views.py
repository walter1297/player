from __future__ import annotations

from urllib.parse import quote_plus, unquote_plus

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView

from .forms import MagnetForm


class IndexView(FormView):
    """Homepage that accepts magnet links and renders the Webtor player."""

    template_name = "stream/index.html"
    form_class = MagnetForm

    def get_initial(self) -> dict[str, str]:
        initial = super().get_initial()
        magnet = self.request.GET.get("magnet")
        if magnet:
            initial["magnet_link"] = unquote_plus(magnet)
        return initial

    def get_context_data(self, **kwargs: object) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        magnet_link = context.get("magnet_link")
        if not magnet_link:
            magnet_param = self.request.GET.get("magnet")
            magnet_link = unquote_plus(magnet_param) if magnet_param else None
        if magnet_link:
            context.update(self._build_stream_context(magnet_link))
        return context

    def form_valid(self, form: MagnetForm) -> HttpResponse:
        magnet_link = form.cleaned_data["magnet_link"]
        encoded = quote_plus(magnet_link)
        return HttpResponseRedirect(f"{self.request.path}?magnet={encoded}")

    def form_invalid(self, form: MagnetForm) -> HttpResponse:
        return self.render_to_response(self.get_context_data(form=form))

    def _build_stream_context(self, magnet_link: str) -> dict[str, object]:
        encoded = quote_plus(magnet_link)
        return {
            "magnet_link": magnet_link,
            "magnet_link_encoded": encoded,
            "webtor_embed_url": f"https://webtor.io/embed?magnet={encoded}",
            "webtor_watch_url": f"https://webtor.io/#/show?magnet={encoded}",
            "download_link": magnet_link,
        }
