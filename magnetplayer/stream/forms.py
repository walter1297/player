from __future__ import annotations

from django import forms


class MagnetForm(forms.Form):
    """Simple form that validates a magnet link."""

    magnet_link = forms.CharField(
        label="磁力链接",
        widget=forms.TextInput(
            attrs={
                "placeholder": "请输入磁力链接，例如 magnet:?xt=...",
                "class": "magnet-input",
            }
        ),
    )

    def clean_magnet_link(self) -> str:
        link = self.cleaned_data["magnet_link"].strip()
        if not link.startswith("magnet:?"):
            raise forms.ValidationError("请输入有效的磁力链接（以 magnet:? 开头）。")
        return link
