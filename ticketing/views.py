from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from ticketing.models import TicketNumGenerator
from .forms import TicketCreationForm, MessageCreationForm


@login_required
def home(request):
    tickets = request.user.profile.tickets
    return render(request, 'ticketing/home.html', context={'tickets': tickets, 'main_page': True})


def about(request):
    return render(request, 'ticketing/about.html')


def new_ticket(request):
    if request.method == 'GET':
        form = TicketCreationForm()
    else:
        form = TicketCreationForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Ticket Created Successfully.')
            request.user.profile.tickets.insert(0,
                                                {
                                                    'ticket_num': get_ticket_num(),
                                                    'priority': form.cleaned_data['priority'],
                                                    'title': form.cleaned_data['title'],
                                                    'chat': [
                                                        {
                                                            'sender': request.user.username,
                                                            'text': form.cleaned_data['text'],
                                                            'attached_file_url': handle_file_upload(request),
                                                        }
                                                    ]
                                                })
            request.user.save()
            return redirect('ticketing:home')
    return render(request, 'ticketing/new_ticket.html', context={'form': form})


def ticket_detail(request, ticket_num):
    if request.method == 'GET':
        form = MessageCreationForm()
    else:
        form = MessageCreationForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.tickets[ticket_num]['chat'].append(
                {
                    'sender': request.user.username,
                    'text': form.cleaned_data['text'],
                    'attached_file_url': handle_file_upload(request)
                }
            )
            request.user.save()
            return redirect('ticketing:ticket_detail', ticket_num)
    context = {
        'ticket': request.user.profile.tickets[ticket_num],
        'ticket_num': ticket_num,
        'new_message_form': form,
        'any_ticket_selected': True,
        'main_page': True,
        'tickets': request.user.profile.tickets,
    }
    return render(request, 'ticketing/home.html', context=context)


def handle_file_upload(request):
    if 'attachment' in request.FILES:
        file = request.FILES['attachment']
        fs = FileSystemStorage(location='media/attachments')
        return '/media/attachments/' + fs.save(file.name, file)


def get_ticket_num():
    instance = TicketNumGenerator.objects.filter().first()
    instance.ticket_num += 1
    instance.save()
    return instance.ticket_num
