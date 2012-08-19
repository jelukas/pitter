from django.http import HttpResponseForbidden

def ajax_required(f):
    """
    AJAX request required decorator
    use it in your views:

    @ajax_required
    def my_view(request):
        ....
    """

    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseForbidden()
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap