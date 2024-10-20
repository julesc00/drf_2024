from django.db import models
from django.utils.http import escape_leading_slashes
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.styles import get_all_styles


LEXERS = [l for l in get_all_lexers() if l[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(style, style) for style in get_all_styles()])


class Snippet(models.Model):
    owner = models.ForeignKey("auth.User", related_name="snippets", on_delete=models.CASCADE)
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python", max_length=100)
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, default="friendly")

    class Meta:
        ordering = ("created",)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML representation
        of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style,
            linenos=linenos,
            full=True,
            **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)



    def __str__(self):
        return self.title
