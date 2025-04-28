from settings.models import Setting



def get_context_process(request):
    data=Setting.objects.last()
   
    return {'data':data}