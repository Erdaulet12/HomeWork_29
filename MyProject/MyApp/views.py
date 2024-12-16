from django.shortcuts import render, redirect
from .forms import BBCodeForm
from bbcode import Parser

# Create your views here.



def process_bbcode(request):
    if request.method == "POST":
        form = BBCodeForm(request.POST)
        if form.is_valid():
            parser = Parser()
            bbcode_content = form.cleaned_data['bbcode_content']
            html_content = parser.format(bbcode_content)

            bbcode_entry = form.save(commit=False)
            bbcode_entry.html_content = html_content
            bbcode_entry.save()

            return redirect('bbcode_success')
    else:
        form = BBCodeForm()

    return render(request, 'process_bbcode.html', {'form': form})
