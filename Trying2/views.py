
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from.models import lesson,details
# Create your views here.
def base(request):
    ac=lesson.objects.all()
    template=loader.get_template('Trying2/base.html')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context,request))

def temp1(request,lesson_id):
    
        cour=get_object_or_404(lesson,pk=lesson_id)
    
        return render(request,'Trying2/temp1.html',{'cour':cour})


def super(request,lesson_id):
    cour=get_object_or_404(lesson, pk=lesson_id)
    
    try:
        selected_tb=cour.details.set_get(pk=request.POST['choice'])
    except (KeyError, lesson.DoesNotExist ): 
        return render(request, 'Trying2/temp1.html', {'cour':cour, 'error_message':"select valid option"})
    else:
        selected_tb.super=True
        selected_tb.save()
        return render(request, 'Trying2/temp1.html', {'cour':cour})