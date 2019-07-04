import autocomplete_light

from .mode import movies

autocomplete_light.register(movies,search_fields = ('Search_names',),autocomplete_js_attributes = {'placeholder' : 'movie name ...'})