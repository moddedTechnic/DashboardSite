from django import template
from django.templatetags.static import static
from django.utils.html import format_html
from sass_processor.processor import sass_processor

register = template.Library()


chart_init_snippet = '''
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>
<script src="{chart_src}"></script>
<link href="{style_src}" rel="stylesheet" type="text/css">
'''

pie_chart_snippet = '''
<div class="graph pie">
    <p>{title}</p>
    <canvas id="{id}" data-url="{data_url}" role="img" width="640" height="640"></canvas>
    <script>pie_chart('{id}', {prepare_data}, {label_factory})</script>
</div>
'''


@register.simple_tag
def chart_init() -> str:
    return format_html(
        chart_init_snippet,
        chart_src=static('scripts/graphs.js'),
        style_src=sass_processor('sass/graphs/graphs.scss')
    )


@register.simple_tag
def pie_chart(id: str, title: str, data_url: str, prepare_data: str, label_factory: str = 'undefined') -> str:
    return format_html(
        pie_chart_snippet, id=id, data_url=data_url, title=title, prepare_data=prepare_data, label_factory=label_factory
    )
