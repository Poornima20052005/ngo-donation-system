from django.shortcuts import render, redirect, get_object_or_404
from .models import Campaign, Donation, Donor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Sum
from decimal import Decimal


def home(request):
    campaigns = Campaign.objects.all()
    return render(request, 'donations/home.html', {'campaigns': campaigns})


@login_required
def donate(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == "POST":
        amount = request.POST.get("amount")

        donor = Donor.objects.first()

        Donation.objects.create(
            donor=donor,
            campaign=campaign,
            amount=Decimal(amount)
        )

        campaign.collected_amount += Decimal(amount)
        campaign.save()

        return redirect("dashboard")

    return render(request, "donations/donate.html", {"campaign": campaign})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)   # automatically login
            return redirect('dashboard')

    else:
        form = UserCreationForm()

    return render(request, 'donations/register.html', {'form': form})


@login_required
def dashboard(request):
    campaigns = Campaign.objects.all()

    total_donations = Donation.objects.aggregate(total=Sum('amount'))['total'] or 0

    top_campaign = Campaign.objects.order_by('-collected_amount').first()

    return render(request, 'donations/dashboard.html', {
        'campaigns': campaigns,
        'total_donations': total_donations,
        'top_campaign': top_campaign
    })