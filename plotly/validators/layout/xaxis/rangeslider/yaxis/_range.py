import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self,
        plotly_name='range',
        parent_name='layout.xaxis.rangeslider.yaxis',
        **kwargs
    ):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            items=[
                {
                    'editType': 'plot',
                    'valType': 'any'
                }, {
                    'editType': 'plot',
                    'valType': 'any'
                }
            ],
            role='style',
            **kwargs
        )