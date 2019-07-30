from pyramid.view import view_config
import blue_yellow_app.utils


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return extend_model({'project': 'blue_yellow_app'})


def extend_model(model_dict):
    model_dict['build_cache_id'] = blue_yellow_app.utils.build_cache_id
    return model_dict
