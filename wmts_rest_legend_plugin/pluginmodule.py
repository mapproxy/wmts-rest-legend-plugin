from mapproxy.wsgiapp import register_request_interceptor
from .wmts_legend_interceptor import wmts_legend_interceptor


def plugin_entrypoint():
    register_request_interceptor(wmts_legend_interceptor)
