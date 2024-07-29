WMTS Rest Legend Plugin
=======================

This is a plugin for [MapProxy](https://github.com/mapproxy/mapproxy) that allows to serve Legends for a WMTS Rest Service
under the `/wmts` endpoint.

Quick-Start
-----------

1. `pip install git+https://github.com/mapproxy/wmts-rest-legend-plugin#egg=wmts-rest-legend-plugin`
2. add the following config to layers:
```yaml
layers:
  - name: some-name
    wmts_rest_legend_url: '{base_url}/wmts/legend/{layer_name}.png'
```

Test locally
------------

1. `pip install MapProxy` 
1. `pip install -e .`
2. `mapproxy-util serve-develop example/mapproxy.yaml`
