from mapproxy.request.wmts import URLTemplateConverter
from mapproxy.request.base import Request
from mapproxy.wsgiapp import register_request_interceptor


class LegendURLTemplateConverter(URLTemplateConverter):
    required = {'Layer'}


def wmts_legend_interceptor(req):
    lg_template_converter = LegendURLTemplateConverter('/legend/{Layer}.png')

    match = lg_template_converter.regexp().search(req.path)
    if match:
        req_vars = match.groupdict()

        environ = req.environ.copy()
        environ['PATH_INFO'] = "/service"
        environ['QUERY_STRING'] = (f"service=WMS&request=GetLegendGraphic&version=1.3.0&"
                                   f"format=image/png&layer={req_vars['Layer']}")

        return Request(environ)

    return req
