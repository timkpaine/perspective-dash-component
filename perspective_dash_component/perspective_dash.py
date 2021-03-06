# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class perspective_dash(Component):
    """A perspective_dash component."""
    @_explicitize_args
    def __init__(self,
                 id=Component.UNDEFINED,
                 data=Component.REQUIRED,
                 view=Component.UNDEFINED,
                 schema=Component.UNDEFINED,
                 columns=Component.UNDEFINED,
                 rowpivots=Component.UNDEFINED,
                 columnpivots=Component.UNDEFINED,
                 aggregates=Component.UNDEFINED,
                 sort=Component.UNDEFINED,
                 index=Component.UNDEFINED,
                 limit=Component.UNDEFINED,
                 computedcolumns=Component.UNDEFINED,
                 filters=Component.UNDEFINED,
                 plugin_config=Component.UNDEFINED,
                 settings=Component.UNDEFINED,
                 embed=Component.UNDEFINED,
                 dark=Component.UNDEFINED,
                 transfer_as_arrow=Component.UNDEFINED,
                 **kwargs):
        self._prop_names = ['id', 'data', 'view', 'schema', 'columns', 'rowpivots', 'columnpivots', 'aggregates', 'sort', 'index',
                            'limit', 'computedcolumns', 'filters', 'plugin_config', 'settings', 'embed', 'dark', 'transfer_as_arrow']
        self._type = 'perspective_dash'
        self._namespace = 'perspective_dash_component'
        self._valid_wildcard_attributes = []
        self.available_events = []
        self.available_properties = ['id', 'data', 'view', 'schema', 'columns', 'rowpivots', 'columnpivots', 'aggregates', 'sort', 'index',
                                     'limit', 'computedcolumns', 'filters', 'plugin_config', 'settings', 'embed', 'dark', 'transfer_as_arrow']
        self.available_wildcard_properties = []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(perspective_dash, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
            or any(getattr(self, c, None) is not None
                   for c in self.__dict__.keys()
                   if any(c.startswith(wc_attr)
                   for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                             for wc_attr in
                                             self._valid_wildcard_attributes])])
            return ('perspective_dash(' + props_string +
                    (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'perspective_dash(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
