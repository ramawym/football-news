from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406426012',
        'name': 'Walyulahdi Maulana Ramadhan',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
